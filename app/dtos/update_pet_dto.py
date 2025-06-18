from pydantic import BaseModel
from typing import Optional


class UpdatePetDTO(BaseModel):
    name: str
    species: str
    age: int
    breed: Optional[str] = None
    location: str
    description: str
    imageUrl: str
    gender: str
    listedById: int
