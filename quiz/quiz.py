from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from quiz.auth import login_required
from quiz.db import get_db

bp = Blueprint('quiz', __name__)


@bp.route('/')
def index():
    return render_template('quiz/index.html')


@bp.route('/quiz', methods=['GET'])
@login_required
def take_quiz():
    db = get_db()
    questions = db.execute('SELECT * FROM question')
    return render_template('quiz/take_quiz.html', questions=questions)


@bp.route('/results', methods=['GET', 'POST'])
@login_required
def get_results():
    db = get_db()
    questions = db.execute('SELECT * FROM question')
    if request.method == 'POST':
        correct_answers = 0
        for question in questions:
            if question['correct_answer'] == request.form[questions['id']]:
                correct_answers += 1
    print(correct_answers)
    return render_template('quiz/results.html')
