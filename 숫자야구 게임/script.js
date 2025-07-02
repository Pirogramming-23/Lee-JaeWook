// @ts-nocheck
// TODO:버튼 누르고 시도 9번 다 써버리면 게임 오버
// 정답은 임의로 설정(나중에 난수로 만들 예정)
const answer = ['4', '7', '2']
let attempts = 9;
document.getElementById("attempts").innerText = attempts;
const text = `남은 횟수: ${attempts}`;


// TODO:아이디 가져와서 변수 만들고 스트라이크, 볼, 아웃을 계산
// 스트라이크:숫자/위치 맞음 볼:숫자 맞음 아웃: 숫자 틀림
// 기회 9번 정답 맞추면 승리 기회 떨어지면 패배
// html 아이디 가져와서 변수 만들기
function check_numbers(){
    const value1 = document.getElementById("number1").value;
    const value2 = document.getElementById("number2").value;
    const value3 = document.getElementById("number3").value;

    const input = [value1, value2, value3]
    console.log(answer)
    console.log(value1, value2, value3)    
    let strike = 0;
    let ball = 0;

    for(let i = 0; i < 3; i++){
        if(input[i] === answer[i]){
            strike++;
        }else if(answer.includes(input[i]))
        {
            ball++;
        }
    }
    
    //result id를 받아서 결과출력
    const resultText = `입력한 값:${input.join("")} = ${strike}S ${ball}B\n`;
    const resultDiv = document.getElementById("results");
    resultDiv.innerText += resultText;
}
