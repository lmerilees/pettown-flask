from pydantic import BaseModel, Field
from typing import Optional


class AddPetDTO(BaseModel):
    name: str
    species: str
    age: int
    breed: Optional[str] = None
    location: str
    description: str
    imageUrl: str
    gender: str
    listedById: int
