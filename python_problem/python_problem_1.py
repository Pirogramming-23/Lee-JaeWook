# baskinrabin31 스타트
# 1. 변수 num을 아래와 같이 선언하여라.
# 그냥 num 선언 및 초기화
num = 0

# 2. input() 함수를 이용하여 1에서 3사이의 정수를 입력 받는 코드를 작성하여라.

# 3. input 값이 0보다 작을 시 정수를 입력하라고 출력/123을 입력하지 않은 경우
# 1, 2, 3 중 하나를 입력하세요를 출력 올바른 값이 입력될때 까지 반복
# 올바른 조건이 들어올 때까지 while문으로 반복
while(True):
    ans = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
    if(ans <= 0):
        print("정수를 입력하세요")
    elif(ans >= 4):
        print("1, 2, 3 중 하나를 입력하세요")
    else:
        break
# 4. 변수 num 을 이용하여, 2단계에서 입력한 수만큼 숫자를 출력하는 코드를 작성하여라.
# 예를 들어, 2단계에서 playerA가 3을 입력했다면, 1,2,3을 아래와 같은 형식으로 출력하여라.
# playerA : 1
# playerA : 2
# playerA : 3

for _ in range(ans):
    num += 1
    print(f"playerA : {num}")