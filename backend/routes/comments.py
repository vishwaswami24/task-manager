from flask import Blueprint, request, jsonify
from models import db, Task, Comment
from schemas import CommentSchema

bp = Blueprint('comments', __name__, url_prefix='/api')

comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)

@bp.route('/tasks/<int:task_id>/comments', methods=['POST'])
def create_comment(task_id):
    task = Task.query.get_or_404(task_id)
    json_data = request.get_json() or {}
    json_data['task_id'] = task_id
    errors = comment_schema.validate(json_data)
    if errors:
        return jsonify({'errors': errors}), 400
    comment = Comment(task_id=task_id, author=json_data['author'], content=json_data['content'])
    db.session.add(comment)
    db.session.commit()
    return comment_schema.dump(comment), 201

@bp.route('/tasks/<int:task_id>/comments', methods=['GET'])
def list_comments(task_id):
    Task.query.get_or_404(task_id)
    q = Comment.query.filter_by(task_id=task_id).order_by(Comment.created_at.asc())
    return comments_schema.dump(q.all())

@bp.route('/tasks/<int:task_id>/comments/<int:comment_id>', methods=['GET'])
def get_comment(task_id, comment_id):
    Task.query.get_or_404(task_id)
    comment = Comment.query.filter_by(task_id=task_id, id=comment_id).first_or_404()
    return comment_schema.dump(comment)

@bp.route('/tasks/<int:task_id>/comments/<int:comment_id>', methods=['PUT', 'PATCH'])
def update_comment(task_id, comment_id):
    Task.query.get_or_404(task_id)
    comment = Comment.query.filter_by(task_id=task_id, id=comment_id).first_or_404()
    json_data = request.get_json() or {}
    errors = comment_schema.validate({**json_data, 'task_id': task_id})
    if errors:
        return jsonify({'errors': errors}), 400
    if 'author' in json_data:
        comment.author = json_data['author']
    if 'content' in json_data:
        comment.content = json_data['content']
    db.session.commit()
    return comment_schema.dump(comment)

@bp.route('/tasks/<int:task_id>/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(task_id, comment_id):
    Task.query.get_or_404(task_id)
    comment = Comment.query.filter_by(task_id=task_id, id=comment_id).first_or_404()
    db.session.delete(comment)
    db.session.commit()
    return '', 204
