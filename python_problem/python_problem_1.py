# baskin robbins31 스타트
# 1. 변수 num을 아래와 같이 선언하여라.
# 그냥 num 선언 및 초기화
num = 0
player = ["playerA", "playerB"]
turn = 0
# 2. input() 함수를 이용하여 1에서 3사이의 정수를 입력 받는 코드를 작성하여라.

# 3. input 값이 0보다 작을 시 정수를 입력하라고 출력/123을 입력하지 않은 경우
# 1, 2, 3 중 하나를 입력하세요를 출력 올바른 값이 입력될때 까지 반복
# 올바른 조건이 들어올 때까지 while문으로 반복

# 4. 변수 num 을 이용하여, 2단계에서 입력한 수만큼 숫자를 출력하는 코드를 작성하여라.
# 예를 들어, 2단계에서 playerA가 3을 입력했다면, 1,2,3을 아래와 같은 형식으로 출력하여라.
# playerA : 1
# playerA : 2
# playerA : 3

    
# 5. 정수 입력 안했을 때 정수를 입력하세요 출력 123 입력 안할 시, 123중 하나를 입력하세요 출력
# num을 이용해서 입력한 수만큼 숫자를 출력
# 일단 3번에서 만든 while문 가져다 쓰기 4번에서 만든 연속 출력도 같이 쓰기
# 탈출조건을 만들어야 함

# 6. 탈출조건인 num이 31을 넘길 시에 게임 종료
# 그리고 턴을 만들어야 함 playerA playerB 배열에 넣고 turn을
# 돌려야 할듯 함
while True:
    print(f"\n{player[turn]} 차례입니다.")
    while True:
        ans = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
            
        # [fix]문자열이 들어오거나 블랭크가 들어올 시 반복문이 안돌아가짐 
        if not ans.isdigit():
            print("정수를 입력하세요")
            continue
        
        ans = int(ans)
        print(ans)
        
        if ans not in [1, 2, 3]:
            print("1, 2, 3 중 하나를 입력하세요")
            continue
        else:
            break
    # 7. 탈출조건에다가 누가 이겼는지 출력하면 됨
    for _ in range(ans):
        num += 1
        print(f"{player[turn]} : {num}")
        if num == 31:
            winner = (turn + 1) % 2
            print(f"{player[winner]} win!")
            exit()
    turn = (turn + 1) % 2