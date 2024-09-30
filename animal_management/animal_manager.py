from typing import Optional, List, Dict
from wildlife_tracker.animal_management.animal import Animal

class AnimalManager:

    def __init__(self) -> None:
        self.animals: Dict[int, Animal] = {}

    def get_animal_by_id(self, animal_id: int) -> Optional[Animal]:
        return self.animals.get(animal_id)


    def register_animal(self, animal: Animal) -> None: #should create an 
        #unused animal_id and add that animal to the dictionary.
        animal_id = max(self.animals.keys(), default=0) + 1  # Generate unique animal_id
        self.animals[animal_id] = animal
        pass

    def remove_animal(self, animal_id: int) -> None:
        if animal_id in self.animals:
            del self.animals[animal_id]
        pass