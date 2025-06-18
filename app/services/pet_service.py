from flask import jsonify

from ..dtos.add_pet_dto import AddPetDTO

from ..dtos.update_pet_dto import UpdatePetDTO
from .. import db
from ..models.pet import Pet


def get_all_pets():
    pets = Pet.query.all()
    return jsonify([p.to_dict() for p in pets]), 200

def get_most_recent_pets():
    recent_pets = Pet.query.order_by(Pet.created_at.desc()).limit(12).all()
    return jsonify([p.to_dict() for p in recent_pets]), 200

def get_my_pets(userId):
    my_pets = Pet.query.filter_by(listed_by_id=userId)
    return jsonify([pet.to_dict() for pet in my_pets])

def get_pet_details(petId):
    pet = Pet.query.filter_by(id=petId).one()
    return jsonify(pet.to_dict())

def create_pet(data):
    add_pet_dto = AddPetDTO(**data)
    new_pet = Pet(
        name=add_pet_dto.name,
        species=add_pet_dto.species,
        age=add_pet_dto.age,
        breed=add_pet_dto.breed,
        location=add_pet_dto.location,
        description=add_pet_dto.description,
        image_url=add_pet_dto.imageUrl,
        gender=add_pet_dto.gender,
        listed_by_id=add_pet_dto.listedById,
    )
    db.session.add(new_pet)
    db.session.commit()
    return jsonify(new_pet.to_dict()), 201


def update_pet(petId, data):
    pet = Pet.query.filter_by(id=petId).one()
    update_pet_dto = UpdatePetDTO(**data)
    pet.name = update_pet_dto.name
    pet.species = update_pet_dto.species
    pet.age = update_pet_dto.age
    pet.breed = update_pet_dto.breed
    pet.location = update_pet_dto.location
    pet.description = update_pet_dto.description
    pet.image_url = update_pet_dto.imageUrl
    pet.gender = update_pet_dto.gender
    db.session.commit()
    return jsonify(pet.to_dict()), 200