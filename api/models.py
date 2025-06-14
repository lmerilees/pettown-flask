from . import db


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    breed = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(255), nullable=False)
    species = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    listed_by_id = db.Column(db.Integer, nullable=False)
    availability_status = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "age": self.age,
            "name": self.name,
            "breed": self.breed,
            "description": self.description,
            "gender": self.gender,
            "species": self.species,
            "imageUrl": self.image_url,
            "location": self.location,
            "listedById": self.listed_by_id,
            "availabilityStatus": self.availability_status,
            "created_at": self.created_at,
        }
