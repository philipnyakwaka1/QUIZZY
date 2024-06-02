# Quizzy

Quizzy is a specialized quiz application tailored for higher education institutions, with a focus on simplifying the administration of continuous assessment tests for educators. Built using Django and Python, Quizzy offers comprehensive functionalities to support seamless user registration, data management, and automated quiz grading.

## Features
- User Registration and Login
- Taking Quizzes
- Viewing Quiz Results
- Automated Marking Process
- Flexible Question Management:



## Technologies Used
- **Django** fro backend
- **HTML / CSS** for frontend
- **JavaScript** for interactivity

## Project Structure
### Models
- **Result**: Represents the result of a quiz taken by a user.
- **Quiz**: Represents a quiz, containing a set of questions and answers.
- **Question**: Represents a single question, tied to a specific quiz.
- **Answer**: Represents a possible answer to a question, associated with the question it belongs to.

*Each question is tied to a quiz, and each result has a quiz and a user.*


## Getting Started
1. Installation
`git clone git@github.com:philipnyakwaka1/QUIZZY.git`

2. SetUp Virtual Environment
python -m venv venv
source venv/bin/activate  # On Unix/Mac
.\venv\Scripts\activate   # On Windows

3. Install Dependencies
pip install -r requirements.txt

4. Database Migration
python manage.py migrate

5. Run the Development Server
python manage.py runserver

6. Access Quizzy
Open your web browser and navigate to http://127.0.0.1:8000/ to access Quizzy.

Contribution
Contributions are welcome through issues or pull requests for any improvements or new features.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
1. Django: I would like to thank the Django community for their exceptional web framework that made building this project possible.
2. Bootstrap: Special thanks to the Bootstrap community for providing a robust and responsive front-end framework that greatly enhanced the user interface of this application.

