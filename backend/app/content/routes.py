from flask import request, Blueprint, jsonify, Request, url_for, redirect

from app.models.user_account_model import User
from app.models.content_model import Post

from app.extensions import db

post_bp = Blueprint('post', __name__)

@post_bp.route('/all-posts', methods=['GET'])
def get_all_posts():
    all_posts = Post.query.all()
    return jsonify([post.to_dict() for post in all_posts]), 200

@post_bp.route('/new', methods=['POST'])
def create_new_post():
    if request.method == 'POST':
        new_post_data = request.get_json()
        new_post = Post(
            text = new_post_data['text'],
            user_id = new_post_data['user_id']
        )
        db.session.add(new_post)
        db.session.commit()
        return jsonify({'message': 'New post saved successfully!'}), 201


@post_bp.route('view/<int:post_id>', methods=['GET'])
def view_post_detail(post_id):
    if request.method == 'GET':
        fetched_post = db.session.get(Post, post_id)
        if not fetched_post:
            return jsonify({'error': f"Post with id {post_id} not found"}), 404
    
        return jsonify({
            "id": fetched_post.id,
            "text": fetched_post.text,
            "user_id": fetched_post.user_id,
            "created_at": fetched_post.created_at
        }), 200


@post_bp.route('edit/<int:post_id>', methods=['PUT'])
def edit_post(post_id):
    if request.method == 'PUT':
        fetched_post = db.session.get(Post, post_id)
        if not fetched_post:
            return jsonify({'error': f"Post with id {post_id} not found"}), 404
        
        modified_post_data = request.get_json()
        if not modified_post_data:
            return jsonify({"error": "Invalid data!"}), 400

        fetched_post.text = modified_post_data['text']
        db.session.commit()

        return jsonify({'message': 'Post updated successfully!'}), 200

@post_bp.route('delete/<int:post_id>', methods=['DELETE'])
def modify_post(post_id):
    if request.method == 'DELETE':
        fetched_post = db.session.get(Post, post_id)
        if not fetched_post:
            return jsonify({'error': f"Post with id {post_id} not found"}), 404
        
        db.session.delete(fetched_post)
        db.session.commit()

        return jsonify({'message': 'Post deleted successfully!'}), 200
    