from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.app import db
from server.models.appearance import Appearance

appearance_bp = Blueprint('appearance_bp', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    return jsonify({"message": "Appearance created"}), 201
