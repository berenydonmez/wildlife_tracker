from typing import Optional, List
from wildlife_tracker.habitat_management.habitat import Habitat

class HabitatManager:
    def __init__(self) -> None:
        self.habitats: dict[int, Habitat] = {}

    def get_habitat_by_id(self, habitat_id: int) -> Optional[Habitat]:
        return self.habitats.get(habitat_id)

    def create_habitat(self, habitat_id: int, geographic_area: str, size: int, environment_type: str) -> Habitat:
        new_habitat = Habitat(habitat_id, geographic_area, size, environment_type)
        self.habitats[habitat_id] = new_habitat
        return new_habitat

    def remove_habitat(self, habitat_id: int) -> None:
        if habitat_id in self.habitats:
            del self.habitats[habitat_id]


    
