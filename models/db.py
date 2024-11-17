from models.models import Sheep
from typing import Dict


class FakeDB:
    def __init__(self):
        self.data: Dict[int, Sheep] = {}

    def get_sheep(self, id: int) -> Sheep:
        return self.data.get(id)



db = FakeDB()
db.data = {
    1: Sheep(id=1, name="Spice", breed="Gotland", sex="ewe"),
    2: Sheep(id=2, name="Blondie", breed="Polypay", sex="ram"),
    3: Sheep(id=3, name="Deedee", breed="Jacobs Four Horns", sex="ram"),
    4: Sheep(id=4, name="Rommy", breed="Romney", sex="ewe"),
    5: Sheep(id=5, name="Vala", breed="Valais Blacknose", sex="ewe"),
    6: Sheep(id=6, name="Esther", breed="Border Leicester", sex="ewe")
}

def add_sheep(self, sheep: Sheep) -> Sheep:
    # Check if the sheep ID already exists
    if sheep.id in self.data:
        raise ValueError("Sheep with this ID already exists")
    # Add the new sheep to the database
    self.data[sheep.id] = sheep
    return sheep

def delete_sheep(self, id: int) -> Sheep:
    # Check if the sheep ID already exists
    if id in self.data:
        # Remove the sheep from the database
        sheep = self.data[id]
        del self.data[id]
        return sheep
    else:
        # Raise an error if the sheep does not exist
        raise ValueError("Sheep with this ID does not exist")

def update_sheep(self, id: int, sheep: Sheep) -> Sheep:
    # Check if the sheep ID already exists
    if id in self.data:
        # Update the sheep in the database
        self.data[id] = sheep
        return sheep
    else:
        # Raise an error if the sheep does not exist
        raise ValueError("Sheep with this ID does not exist")
