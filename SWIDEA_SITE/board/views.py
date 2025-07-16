from django.shortcuts import render, redirect, get_object_or_404
from .forms import IdeaForm, DevToolForm
from .models import Idea, IdeaStar, DevTool
import json
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.db.models import Count
from django.contrib.auth.models import User

def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('idea_list')
    else:
        form = IdeaForm()
    return render(request, 'board/idea_form.html', {'form': form})

from django.db.models import Case, When, Value, IntegerField

def idea_list(request):
    sort = request.GET.get('sort')
    starred_ids = request.session.get('starred_ideas', [])

    if sort == 'interest':
        ideas = Idea.objects.all().order_by('-interest')
    elif sort == 'title':
        ideas = Idea.objects.all().order_by('title')
    elif sort == 'created_at':
        ideas = Idea.objects.all().order_by('created_at')  # 등록순
    elif sort == '-created_at':
        ideas = Idea.objects.all().order_by('-created_at')  # 최신순
    elif sort == 'starred':
        ideas = list(Idea.objects.all())
        ideas.sort(key=lambda idea: idea.pk not in starred_ids)
    else:
        ideas = Idea.objects.all()

    starred_ideas = Idea.objects.filter(pk__in=starred_ids)

    context = {
        'ideas': ideas,
        'starred_ideas': starred_ideas,
    }
    return render(request, 'board/idea_list.html', context)


# def idea_detail(request, pk):
#     idea = get_object_or_404(Idea, pk=pk)
#     return render(request, 'board/idea_detail.html', {'idea': idea})


def idea_detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk)

    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    starred = request.session.get('starred_ideas', [])
    is_starred = pk in starred

    context = {
        'idea': idea,
        'is_starred': is_starred,
    }
    return render(request, 'board/idea_detail.html', context)


def idea_update(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('idea_detail', pk=idea.pk)
    else:
        form = IdeaForm(instance=idea)
    return render(request, 'board/idea_form.html', {'form': form})

def idea_delete(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == "POST":
        idea.delete()
        return redirect('idea_list')

def devtool_create(request):
    if request.method == 'POST':
        form = DevToolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('devtool_list')
    else:
        form = DevToolForm()
    return render(request, 'board/devtool_create.html', {'form':form})

def devtool_list(request):
    tools = DevTool.objects.all()
    return render(request, 'board/devtool_list.html', {'tools': tools})

def devtool_detail(request, pk):
    tool = get_object_or_404(DevTool, pk=pk)
    return render(request, 'board/devtool_detail.html', {'tool': tool})

def increase_interest(request, pk):
    if request.method == 'POST':
        idea = Idea.objects.get(pk=pk)
        idea.interest += 1
        idea.save()
        return JsonResponse({'interest': idea.interest})
    return HttpResponseNotAllowed(['POST'])

def decrease_interest(request, pk):
    if request.method == 'POST':
        idea = Idea.objects.get(pk=pk)
        idea.interest = max(0, idea.interest - 1)
        idea.save()
        return JsonResponse({'interest': idea.interest})
    return HttpResponseNotAllowed(['POST'])

def toggle_star(request, pk):
    if request.method == 'POST':
        idea = Idea.objects.get(pk=pk)
        user = request.user
        if idea.starred_users.filter(id=user.id).exists():
            idea.starred_users.remove(user)
            starred = False
        else:
            idea.starred_users.add(user)
            starred = True
        return JsonResponse({'starred': starred})
    return HttpResponseNotAllowed(['POST'])

def devtool_update(request, pk):
    tool = get_object_or_404(DevTool, pk=pk)
    if request.method == "POST":
        form = DevToolForm(request.POST, request.FILES, instance=tool)
        if form.is_valid():
            form.save()
            return redirect('devtool_detail', pk=pk)
    else:
        form = DevToolForm(instance=tool)
    return render(request, 'board/devtool_form.html', {'form': form})


def devtool_delete(request, pk):
    tool = get_object_or_404(DevTool, pk=pk)
    if request.method == 'POST':
        tool.delete()
        return redirect('devtool_list')
    return render(request, 'board/devtool_confirm_delete.html', {'tool': tool})


# def update_interest(request, pk):
#     if request.method == 'POST':
#         idea = get_object_or_404(idea, pk = pk)
#         delta = int(request.POST.get('delta', 0))
#         idea.interest += delta
#         idea.save()
#         return JsonResponse({'new_interest':idea.interest})
#     return JsonResponse({'error':'Invaild request'}, status = 400)

@require_POST
@csrf_exempt  # 만약 csrf 토큰이 안 먹힐 때만 임시로 사용
def update_interest(request, pk):
    try:
        data = json.loads(request.body)
        idea = get_object_or_404(Idea, pk=pk)

        if data['action'] == 'increase':
            idea.interest += 1
        elif data['action'] == 'decrease':
            idea.interest = max(0, idea.interest - 1)

        idea.save()
        return JsonResponse({'interest': idea.interest})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def toggle_star(request, pk):
    if request.method == "POST":
        idea = get_object_or_404(Idea, pk=pk)

        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key

        if 'starred_ideas' not in request.session:
            request.session['starred_ideas'] = []

        starred = request.session['starred_ideas']

        if pk in starred:
            starred.remove(pk)
            request.session['starred_ideas'] = starred
            return JsonResponse({'starred': False})
        else:
            starred.append(pk)
            request.session['starred_ideas'] = starred
            return JsonResponse({'starred': True})

    return JsonResponse({'error': 'Invalid request'}, status=400)
