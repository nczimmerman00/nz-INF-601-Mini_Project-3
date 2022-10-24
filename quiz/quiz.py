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


@bp.route('/quiz', methods=['POST'])
@login_required
def take_quiz():
    return render_template('quiz/create.html')


@bp.route('/results', methods=('GET',))
@login_required
def get_results():
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    return redirect(url_for('quiz.index'))
