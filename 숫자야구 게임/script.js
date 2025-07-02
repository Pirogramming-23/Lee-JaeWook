// @ts-nocheck
// TODO:버튼 누르고 시도 9번 다 써버리면 게임 오버
// 정답은 임의로 설정(나중에 난수로 만들 예정)
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
    
    document.getElementById("number1").value = "";
    document.getElementById("number2").value = "";
    document.getElementById("number3").value = "";

    let strike = 0;
    let ball = 0;

    //버튼을 누를 시에 attemps가 줄어듬ㄹ
    if(attempts > 0){
        attempts--;
        document.getElementById("attempts").innerText = attempts;
    }

    for(let i = 0; i < 3; i++){
        if(input[i] === answer[i]){
            strike++;
        }else if(answer.includes(input[i]))
        {
            ball++;
        }
    }
    
    // result id를 받아서 결과출력
    let resultText = `입력한 값:${input.join("")} = `;
    if(strike === 0 && ball === 0){
        resultText += `<span class = "out">O</span>`;
    }
    else{
        if (strike > 0){
            resultText += `${strike}<span class = "strike">S</span>`;
        }
        if(ball > 0)
        {
            resultText += `${ball}<span class = "ball">B</span>`;
        }
    }
    const resultDiv = document.getElementById("results");
    resultDiv.innerHTML += resultText + `<br>`;

    // TODO:attemps를 다 쓰게 될 시에 게임오버png출력 또는 스또라이크 3개일 시 승리 
    if(attempts === 0){
        console.log("패배")
        const resultImg = document.getElementById("game-result-img");
        resultImg.src = "fail.png";
        resultImg.alt = "게임 오바";
        resultImg.style.display = "block";
        document.querySelector(".submit-button").disabled = true;
        document.querySelector(".submit-button").style.backgroundColor = "gray";

    }
    else if (strike >= 3){
        console.log("승리")
        const resultImg = document.getElementById("game-result-img");
        resultImg.src = "success.png";
        resultImg.alt = "게임 승리";
        resultImg.style.display = "block";
        document.querySelector(".submit-button").disabled = true;
        document.querySelector(".submit-button").style.backgroundColor = "gray";
    }
}

// TODO:중복이 생기지 않는 난수 3개
// 포인트는 rand는 숫자, strRand는 문자열이라는 거
// includes는 값자체를 비교함
function generateAnswer(){
    const nums = [];
    while(nums.length < 3){
        const rand = Math.floor(Math.random() * 9) + 1;
        const strRand = rand.toString();
        if (!nums.includes(strRand)){
            nums.push(strRand);
        }
    }
    return nums;
}
// 함수 생성 뒤에 선언
const answer = generateAnswer();
