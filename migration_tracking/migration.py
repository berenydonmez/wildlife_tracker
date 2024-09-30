from typing import Any, Optional
from wildlife_tracker.habitat_management.habitat import Habitat

class Migration:
    def __init__(self,
                 migration_id: int,
                 species: str,
                 current_location: str,
                 destination: Habitat,
                 health_status: Optional[str] = None,
                 start_date: Optional[str] = None,
                 status: str = "Scheduled") -> None:
        self.migration_id = migration_id
        self.species = species
        self.current_location = current_location
        self.destination = destination
        self.health_status = health_status
        self.start_date = start_date
        self.status = status

    def update_migration_details(self, **kwargs: dict[str, Any]) -> None:
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def get_migration_details(self) -> dict:
        return {
            "migration_id": self.migration_id,
            "species": self.species,
            "current_location": self.current_location,
            "destination": self.destination.get_habitat_details() if self.destination else None,
            "health_status": self.health_status,
            "start_date": self.start_date,
            "status": self.status,
        }
