"""
MIT License

Copyright (c) 2024 Mukund

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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
