from typing import Any, Optional, Dict, List
from wildlife_tracker.migration_tracking.migration import Migration
from wildlife_tracker.migration_tracking.migration_path import MigrationPath

class MigrationManager:
    def __init__(self) -> None:
        self.migrations: Dict[int, Migration] = {}
        self.migration_paths: Dict[int, MigrationPath] = {}

    def register_migration(self, migration: Migration) -> None:
        self.migrations[migration.migration_id] = migration

    def get_migration_by_id(self, migration_id: int) -> Optional[Migration]:
        return self.migrations.get(migration_id)

    def remove_migration(self, migration_id: int) -> None:
        if migration_id in self.migrations:
            del self.migrations[migration_id]

    def update_migration(self, migration_id: int, **kwargs: dict[str, Any]) -> None:
        migration = self.get_migration_by_id(migration_id)
        if migration:
            migration.update_migration_details(**kwargs)

    def create_migration_path(self, path_id: int, species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> MigrationPath:
        migration_path = MigrationPath(path_id, species, start_location, destination, duration)
        self.migration_paths[path_id] = migration_path
        return migration_path

    def get_migration_path_by_id(self, path_id: int) -> Optional[MigrationPath]:
        return self.migration_paths.get(path_id)

    def remove_migration_path(self, path_id: int) -> None:
        if path_id in self.migration_paths:
            del self.migration_paths[path_id]
