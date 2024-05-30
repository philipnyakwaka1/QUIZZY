document.addEventListener('DOMContentLoaded', function() {
    const startQuizButton = document.getElementById('start-quiz');
    const submitQuizButton = document.getElementById('submit-quiz');
    const quizInfo = document.getElementById('quiz-info');
    const questionsContainer = document.getElementById('questions-container');
    const timerElement = document.getElementById('time-left');
    let timer;

    startQuizButton.addEventListener('click', function() {
        quizInfo.style.display = 'none';
        questionsContainer.style.display = 'block';
        let timeLeft = parseInt(timerElement.textContent, 10);
        timer = setInterval(function() {
            timeLeft--;
            timerElement.textContent = timeLeft;
            if (timeLeft <= 0) {
                clearInterval(timer);
                submitQuiz();
            }
        }, 1000);
    });

    submitQuizButton.addEventListener('click', function() {
        if (confirm('Are you sure you want to submit the quiz?')) {
            submitQuiz();
        }
    });

    function submitQuiz() {
        clearInterval(timer);
        let correctCount = 0;
        const questions = document.querySelectorAll('.question');
        questions.forEach(question => {
            const selectedAnswer = question.querySelector('input[type="radio"]:checked');
            if (selectedAnswer && selectedAnswer.dataset.correct === 'True') {
                correctCount++;
            }
        });
        fetch('/submit-quiz', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}'
            },
            body: JSON.stringify({ score: correctCount, total: questions.length })
        }).then(response => response.json())
          .then(data => {
              alert('You got ' + correctCount + ' correct answers out of ' + questions.length);
          }).catch(error => console.error('Error:', error));
    }
});