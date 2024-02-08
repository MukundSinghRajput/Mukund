from pathlib import Path
from Mukund.core.database import *

class Mukund:
    def __init__(self, Name: str = "Storage") -> None:
        """
        Initialize the Mukund class with a specified database name.

        Parameters:
        - Name: Name of the Storage.
        """
        self.db_name = Name
        self.db_path = Path(Name)
        self.db_path.mkdir(exist_ok=True)
        print(
            """
                        █▀▄▀█ █░█ █▄▀ █░█ █▄░█ █▀▄
                        █░▀░█ █▄█ █░█ █▄█ █░▀█ █▄▀

                Visit @ItzMukund for updates!! (Telegram)
"""
        )

    def database(self, collection_name: str) -> Base:
        """
        Create or access a database collection.

        Parameters:
        - collection_name: Name of the collection within the database.

        Returns:
        - Base: An instance of the Base class representing the specified collection.
        """
        collection_path = self.db_path / f"{collection_name}.json"
        return Base(collection_path)