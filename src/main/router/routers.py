from flask import Blueprint, request, jsonify
from src.errors.errors_handler import handle_errors
from src.domain.validators.requests_validator.user_create_validator import user_create_validator
from src.domain.validators.requests_validator.user_update_validator import user_update_validator
from src.domain.validators.requests_validator.user_delete_validator import user_delete_validator
from src.domain.validators.requests_validator.save_address_validator import save_address_validator
from src.main.adapters.request_adapter import request_adapter
from src.main.composer.create_user_composer import create_user_composer
from src.main.composer.update_user_composer import update_user_composer
from src.main.composer.get_user_composer import get_user_composer
from src.main.composer.delete_user_composer import delete_user_composer
from src.main.composer.save_address_composer import save_address_composer
from src.main.composer.get_address_composer import get_address_composer


user_router_bp = Blueprint("user_routes", __name__)


@user_router_bp.route("/users/find", methods=['GET'])
def get_user():
    try:
        http_response = request_adapter(request, get_user_composer())
    except Exception as e:
        http_response = handle_errors(e)
    return jsonify(http_response.body), http_response.status_code


@user_router_bp.route("/users/create", methods=['POST'])
def registry_user():
    try:
        user_create_validator(request)
        http_response = request_adapter(request, create_user_composer())
    except Exception as e:
        http_response = handle_errors(e)
    return jsonify(http_response.body, http_response.status_code)


@user_router_bp.route("/users/update", methods=['PUT'])
def update_user():
    try:
        user_update_validator(request)
        http_response = request_adapter(request, update_user_composer())
    except Exception as e:
        http_response = handle_errors(e)
    return jsonify(http_response.body), http_response.status_code


@user_router_bp.route("/users/delete", methods=['DELETE'])
def delete_user():
    try:
        user_delete_validator(request)
        http_response = request_adapter(request, delete_user_composer())
    except Exception as e:
        http_response = handle_errors(e)
    return jsonify(http_response.body), http_response.status_code


@user_router_bp.route('/users/consulta_cep', methods=['GET'])
def consulta_cep():
    try:
        save_address_validator(request)
        http_response = request_adapter(request, save_address_composer())
    except Exception as e:
        http_response = handle_errors(e)
    return jsonify(http_response.body), http_response.status_code


@user_router_bp.route('/users/check_cep', methods=['GET'])
def check_cep_in_db():
    http_response = request_adapter(request, get_address_composer())
    return jsonify(http_response.body), http_response.status_code

