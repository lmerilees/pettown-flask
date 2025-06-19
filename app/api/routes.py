from flask import Blueprint, request
from ..services.pet_service import (
    create_pet,
    delete_pet,
    get_most_recent_pets,
    get_my_pets,
    get_pet_details,
    update_pet,
    get_all_pets,
)

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/pets", methods=["GET"])
def get_pets():
    return get_all_pets()


@bp.route("/pets/latest", methods=["GET"])
def get_recent_pets():
    return get_most_recent_pets()


@bp.route("/pets/<petId>", methods=["PUT"])
def update_my_pet(petId):
    data = request.get_json()
    return update_pet(petId, data)


@bp.route("/pets", methods=["POST"])
def add_pet():
    data = request.get_json()
    return create_pet(data)

@bp.route("/pets/<petId>", methods=["DELETE"])
def delete_my_pet(petId):
    return delete_pet(petId)

@bp.route("/pets/my-pets/<userId>", methods=["GET"])
def get_my_pets_by_userId(userId):
    return get_my_pets(userId)


@bp.route("/pets/<petId>", methods=["GET"])
def get_pet_details_by_id(petId):
    return get_pet_details(petId)
