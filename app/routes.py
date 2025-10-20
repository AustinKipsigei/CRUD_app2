from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Task
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

# 🏠 Home / Dashboard
@main.route('/')
@login_required
def index():
    # Get filter and sort options
    filter_type = request.args.get('filter', 'all')
    sort = request.args.get('sort', 'newest')

    # Only show current user's tasks
    query = Task.query.filter_by(user_id=current_user.id)

    # Apply filters
    if filter_type == 'completed':
        query = query.filter_by(completed=True)
    elif filter_type == 'pending':
        query = query.filter_by(completed=False)

    # Apply sorting
    if sort == 'oldest':
        tasks = query.order_by(Task.created_at.asc()).all()
    else:
        tasks = query.order_by(Task.created_at.desc()).all()

    # Stats
    total = query.count()
    completed = query.filter_by(completed=True).count()
    pending = total - completed

    return render_template(
        'index.html',
        tasks=tasks,
        total=total,
        completed=completed,
        pending=pending,
        filter_type=filter_type,
        sort=sort
    )


# ➕ Add new task
@main.route('/add', methods=['POST'])
@login_required
def add():
    task_content = request.form.get('task')
    if task_content:
        new_task = Task(content=task_content, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('main.index'))


# ✏️ Update task
@main.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    task = Task.query.filter_by(id=id, user_id=current_user.id).first_or_404()

    if request.method == 'POST':
        task.content = request.form['task']
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('update.html', task=task)


# 🗑 Delete task
@main.route('/delete/<int:id>')
@login_required
def delete(id):
    task = Task.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main.index'))


# 🔁 Toggle completion
@main.route('/toggle/<int:id>')
@login_required
def toggle(id):
    task = Task.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('main.index'))
