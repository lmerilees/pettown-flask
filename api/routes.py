from flask import Blueprint, request, jsonify
from .models import Pet
from . import db

bp = Blueprint("api", __name__)


@bp.route("/api/pets", methods=["GET"])
def get_pets():
    pets = Pet.query.all()
    return jsonify([p.to_dict() for p in pets])


@bp.route("/api/pets/latest", methods=["GET"])
def get_recent_pets():
    recent_pets = Pet.query.order_by(Pet.created_at.desc()).limit(12).all()
    return jsonify([p.to_dict() for p in recent_pets])


@bp.route("/api/pets/<petId>", methods=["PUT"])
def update_pet(petId):
    pet = Pet.query.filter_by(id=petId).one()
    data = request.get_json()
    pet.name = data.get("name", pet.name)
    pet.species = data.get("species", pet.species)
    pet.age = data.get("age", pet.age)
    pet.breed = data.get("breed", pet.breed)
    pet.location = data.get("location", pet.location)
    pet.description = data.get("description", pet.description)
    pet.image_url = data.get("imageUrl", pet.image_url)
    pet.gender = data.get("gender", pet.gender)
    db.session.commit()
    return jsonify(pet.to_dict())


@bp.route("/api/pets", methods=["POST"])
def add_pet():
    data = request.get_json()
    new_pet = Pet(
        name=data["name"],
        species=data["species"],
        age=data["age"],
        breed=data["breed"],
        location=data["location"],
        description=data["description"],
        image_url=data["imageUrl"],
        gender=data["gender"],
        listed_by_id=data["listedById"],
    )
    db.session.add(new_pet)
    db.session.commit()
    return jsonify(new_pet.to_dict()), 201


@bp.route("/api/pets/my-pets/<userId>", methods=["GET"])
def get_my_pets(userId):
    my_pets = Pet.query.filter_by(listed_by_id=userId)
    return jsonify([pet.to_dict() for pet in my_pets])


@bp.route("/api/pets/<petId>", methods=["GET"])
def get_pet_details(petId):
    pet = Pet.query.filter_by(id=petId).one()
    return jsonify(pet.to_dict())
