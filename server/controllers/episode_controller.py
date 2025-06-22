from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from server.app import db
from server.models.episode import Episode

episode_bp = Blueprint('episode_bp', __name__)

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
        return jsonify({"message": "Deleted"}), 200

@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    from server.models.episode import Episode

    episodes = Episode.query.all()
    episode_list = [
        {"id": e.id, "date": e.date.strftime("%Y-%m-%d"), "number": e.number}
        for e in episodes
    ]
    return jsonify(episode_list), 200

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    from server.models.episode import Episode
    from server.models.appearance import Appearance
    from server.models.guest import Guest

    episode = Episode.query.get_or_404(id)

    appearances = [
        {
            "id": a.id,
            "rating": a.rating,
            "guest": {
                "id": a.guest.id,
                "name": a.guest.name,
                "occupation": a.guest.occupation,
            },
        }
        for a in episode.appearances
    ]

    return jsonify({
        "id": episode.id,
        "date": episode.date.strftime("%Y-%m-%d"),
        "number": episode.number,
        "appearances": appearances
    }), 200
