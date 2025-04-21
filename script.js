let quiz = [];
let current = 0;
let score = 0;

const questionEl = document.getElementById("question");
const choicesEl = document.getElementById("choices");
const messageEl = document.getElementById("message");
const explanationEl = document.getElementById("explanation");
const scoreEl = document.getElementById("score");
const correctSound = document.getElementById("correct-sound");
const wrongSound = document.getElementById("wrong-sound");

fetch("questions.json")
  .then((res) => res.json())
  .then((data) => {
    quiz = data;
    showQuestion();
  });

function showQuestion() {
  const q = quiz[current];
  questionEl.textContent = `Q${current + 1}. ${q.question}`;
  messageEl.textContent = "";
  explanationEl.textContent = "";
  choicesEl.innerHTML = "";

  q.choices.forEach((choice, index) => {
    const btn = document.createElement("button");
    btn.textContent = choice;
    btn.onclick = () => checkAnswer(index);
    choicesEl.appendChild(btn);
  });
}

function checkAnswer(selected) {
  const q = quiz[current];
  choicesEl.innerHTML = "";

  if (selected === q.answer) {
    messageEl.textContent = "まりさ「おおっ！正解だぜぇ！」";
    correctSound.play();
    score++;
  } else {
    messageEl.textContent = "まりさ「どわぁ〜っ！？そっちかよ！」";
    wrongSound.play();
  }

  explanationEl.textContent = q.explanation;

  const nextBtn = document.createElement("button");
  nextBtn.textContent = "次へすすむ";
  nextBtn.onclick = () => {
    current++;
    if (current < quiz.length) {
      showQuestion();
    } else {
      showScore();
    }
  };
  choicesEl.appendChild(nextBtn);
}

function showScore() {
  questionEl.textContent = "";
  choicesEl.innerHTML = "";
  messageEl.textContent = "";
  explanationEl.textContent = "";
  scoreEl.textContent = `スコア: ${score} / ${quiz.length} だぜ！`;
}
