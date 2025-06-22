from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from server.app import db
from server.models.episode import Episode

episode_bp = Blueprint('episode_bp', __name__)

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
        return jsonify({"message": "Deleted"}), 200
