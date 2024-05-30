document.addEventListener('DOMContentLoaded', function() {
    const startQuizButton = document.getElementById('start-quiz');
    const submitQuizButton = document.getElementById('submit-quiz');
    const quizInfo = document.getElementById('quiz-info');
    const questionsContainer = document.getElementById('questions-container');
    const timerElement = document.getElementById('time-left');
    const scoreInput = document.getElementById('score');
    const correctCountInput = document.getElementById('correct_count');
    const totalQuestionsInput = document.getElementById('total_questions');
    const quizForm = document.getElementById('quiz-form');
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

    submitQuizButton.addEventListener('click', function(event) {
        event.preventDefault();
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

        const totalQuestions = questions.length;
        const score = (correctCount / totalQuestions) * 100;

        scoreInput.value = score;

        quizForm.submit();
    }
});
