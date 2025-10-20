from flask import Blueprint, request
from models import db, Task
from schemas import TaskSchema

bp = Blueprint('tasks', __name__, url_prefix='/api')
task_schema = TaskSchema()

@bp.route('/tasks', methods=['GET'])
def list_tasks():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return task_schema.dump(tasks, many=True), 200

@bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json() or {}
    errors = task_schema.validate(data)
    if errors:
        return {'errors': errors}, 400
    task = Task(title=data['title'], description=data.get('description', ''))
    db.session.add(task)
    db.session.commit()
    return task_schema.dump(task), 201

@bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get_or_404(task_id)
    return task_schema.dump(task)

@bp.route('/tasks/<int:task_id>', methods=['PUT', 'PATCH'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json() or {}
    errors = task_schema.validate(data, partial=True)
    if errors:
        return {'errors': errors}, 400
    if 'title' in data:
        task.title = data['title']
    if 'description' in data:
        task.description = data.get('description', '')
    db.session.commit()
    return task_schema.dump(task)

@bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return '', 204
