// 일단 받아올 수 있는 element들 다 받아오기
const timeDisplay = document.querySelector('.time-display');
const startBtn = document.getElementById('start');
const stopBtn = document.getElementById('stop');
const resetBtn = document.getElementById('reset');
const deleteBtn = document.getElementById('record-delete');
const recordList = document.getElementById('record-list');

// 변수들 선언 바뀌는 것들 
let startTime = 0;
let elapsedTime = 0;
let seconds = '00';
let milliseconds = '00';
let timerInterval;


// 기능구현 4가지
// 1. 스톱위치 기능 구현
// 2. 기록 추가 기능 구현
// 3. 선택 삭제 기능 구현
// 4. 전체 삭제 기능 구현

function formatTime(ms) {
  seconds = String(Math.floor(ms / 1000)).padStart(2, '0');
  milliseconds = String(ms % 1000).padStart(3, '0').slice(0, 2);
  return `${seconds}:${milliseconds}`;
}

function updateTime() {
  const now = Date.now();
  elapsedTime = now - startTime;
  timeDisplay.textContent = formatTime(elapsedTime);
}

startBtn.addEventListener('click', () => {
  if (!timerInterval) {
    startTime = Date.now() - elapsedTime;
    timerInterval = setInterval(updateTime, 10);
  }
});

stopBtn.addEventListener('click', () => {
  clearInterval(timerInterval);
  timerInterval = null;

  const recordItem = document.createElement('div');
  recordItem.classList.add('record-item');

  const checkbox = document.createElement('input');
  checkbox.type = 'checkbox';
  checkbox.classList.add('record-checkbox');

  const timeText = document.createElement('span');
  timeText.classList.add('record-time');
  timeText.textContent = `${seconds} : ${milliseconds}`;

  recordItem.appendChild(checkbox);
  recordItem.appendChild(timeText);
  recordList.appendChild(recordItem);
});

resetBtn.addEventListener('click', () => {
  clearInterval(timerInterval);
  timerInterval = null;
  elapsedTime = 0;
  timeDisplay.textContent = '00:00';
});

deleteBtn.addEventListener('click', () => {
  const checkboxes = document.querySelectorAll('.record-checkbox');
  let anyChecked = false;

  checkboxes.forEach((checkbox) => {
    if (checkbox.checked) {
      checkbox.parentElement.remove();
      anyChecked = true;
    }
  });

  if (!anyChecked) {
    recordList.innerHTML = '';
  }
});

const toggleAllBtn = document.getElementById('toggle-all');
let isAllSelected = false;

toggleAllBtn.addEventListener('click', () => {
  const checkboxes = document.querySelectorAll('.record-checkbox');

  checkboxes.forEach(checkbox => {
    checkbox.checked = !isAllSelected;
  });

  isAllSelected = !isAllSelected;
  toggleAllBtn.textContent = isAllSelected ? '전체 해제' : '전체 선택';
});
