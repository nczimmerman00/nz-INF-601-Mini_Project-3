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
def get_results():
    db = get_db()
    questions = db.execute('SELECT * FROM question')
    correct_answers = -1
    if request.method == 'POST':
        correct_answers = 0
        for question in questions:
            print(request.form[str(question['id'])])
            if question['correct_answer'] == request.form[str(question['id'])]:
                correct_answers += 1
        db.execute(
            'INSERT INTO attempt (user_id, score)'
            ' VALUES (?, ?)',
            (g.user['id'], correct_answers)
        )
        db.commit()
    recent_attempts = db.execute(
        'SELECT username, score, time_taken FROM user INNER JOIN attempt on user.id = attempt.user_id ORDER BY attempt.time_taken DESC LIMIT 20')
    top_attempts = db.execute(
        'SELECT DISTINCT username, score, time_taken FROM user INNER JOIN attempt on user.id = attempt.user_id ORDER BY attempt.score DESC, attempt.time_taken LIMIT 5')
    return render_template('quiz/results.html', score=correct_answers, recent_attempts=recent_attempts, top_attempts=top_attempts)
