from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def post_list(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'pirostagram/post_list.html', {'posts': posts})

@csrf_exempt
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pirostagram:post_list')
    else:
        form = PostForm()
    return render(request, 'pirostagram/post_form.html', {'form': form})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('pirostagram:post_list')

@csrf_exempt
def post_like(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        post.like_count += 1
        post.save()
        return JsonResponse({'like_count': post.like_count})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def comment_create(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        content = request.POST.get('content')
        if not post_id or not content:
            return JsonResponse({'error': 'Missing fields'}, status=400)
        post = get_object_or_404(Post, pk=post_id)
        comment = Comment.objects.create(post=post, content=content)
        return JsonResponse({
            'id': comment.id,
            'content': comment.content,
        })
    return JsonResponse({'error': 'Invalid request'}, status=400)


@csrf_exempt
def comment_delete(request, comment_id):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        return JsonResponse({'status': 'deleted'})
    return JsonResponse({'error': 'Invalid request'}, status=400)
