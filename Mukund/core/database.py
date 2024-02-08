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

import json, re
from pathlib import Path
from Mukund.errors.exceptions import KeyAlreadyExistsError
from typing import Any, Callable, Dict, List, Optional, Union

class Base:
    def __init__(self, collection_path: Path) -> None:
        """
        Initialize the Base class with a specified collection path.

        Parameters:
        - collection_path: Path to the JSON collection file.
        """
        self.collection_path = collection_path
        if not self.collection_path.exists():
            self._save_data({})

    def _load_data(self) -> Dict[str, Any]:
        """
        Load data from the collection file.

        Returns:
        - Dict[str, Any]: Loaded data as a dictionary.
        """
        with open(self.collection_path, 'r') as file:
            data = json.load(file)
        return data

    def _save_data(self, data: Dict[str, Any]) -> None:
        """
        Save data to the collection file.

        Parameters:
        - data: Data to be saved as a dictionary.
        """
        with open(self.collection_path, 'w') as file:
            json.dump(data, file, indent=2)
          
    def put(self, key: str, value: dict = None) -> None:
        """
        Add a new key-value pair to the collection.

        Parameters:
        - key: Key for the new entry.
        - value: Dictionary representing the values associated with the key.

        Raises:
        - KeyAlreadyExistsError: If the key already exists in the collection.
        """
        if value is None:
            return
        data = self._load_data()
        if key in data:
            raise KeyAlreadyExistsError(key)
        data[key] = value
        self._save_data(data)

    def get(self, key: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve the values associated with a key from the collection.

        Parameters:
        - key: Key to retrieve values for.

        Returns:
        - Optional[Dict[str, Any]]: Values associated with the key, or None if the key is not found.
        """
        data = self._load_data()
        return data.get(key)
    def delete(self, key: str) -> None:
        """
        Delete a key-value pair from the collection.

        Parameters:
        - key: Key to be deleted from the collection.
        """
        data = self._load_data()
        if key in data:
            del data[key]
            self._save_data(data)

    def all(self) -> Dict[str, Any]:
        """
        Retrieve all key-value pairs from the collection.

        Returns:
        - Dict[str, Any]: All key-value pairs in the collection.
        """
        return self._load_data()

    def query(self, condition_func: Callable[[Dict[str, Any]], bool] = None, query_str: str = None,limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """
        Query the collection based on a given condition function.

        Parameters:
        - condition_func: Callable function defining the condition for filtering.
        - limit: Optional limit for the number of results to be returned.
        - query_str: Regular expression string for matching values in the collection.

        Returns:
        - List[Dict[str, Any]]: Query results that meet the specified condition.
        """
        data = self._load_data()
        query_result = [item for item in data.values() if condition_func(item)]

        if limit is not None:
            query_result = query_result[:limit]

        return query_result

    def update(self, key: str, updated_values):
        """
        Update values for a specific key in the collection.

        Parameters:
        - key: Key to be updated.
        - updated_values: New values to update for the key.

        Raises:
        - KeyError: If the specified key is not found in the collection.
        """
        data = self._load_data()
        if key in data:
            current_values = data[key]
            current_values.update(updated_values)
            data[key] = current_values
            self._save_data(data)
        else:
            raise KeyError(f"Key '{key}' not found in the collection.")

    def increment(self, key: str, increment_by: int = 1):
        """
        Increment numeric values associated with a key in the collection.

        Parameters:
        - key: Key for which numeric values will be incremented.
        - increment_by: Amount by which to increment the numeric values.

        Raises:
        - ValueError: If the key does not exist or if the value is not numeric.
        """
        current_data = self.get(key)
        if current_data is not None:
            updated_data = {k: v + increment_by if isinstance(v, (int, float)) else v for k, v in current_data.items()}
            self.update(key, updated_data)
        else:
            raise ValueError(f"The key '{key}' does not exist in the database or their is no integer field")

    def decrement(self, key: str, decrement_by: int = 1) -> None:
        """
        Decrement a numeric value associated with a key in the collection.

        Parameters:
        - key: Key for which a numeric value will be decremented.
        - decrement_by: Amount by which to decrement the numeric value.

        Raises:
        - ValueError: If the key does not exist or if the value is not numeric.
        """
        current_data = self.get(key)

        if current_data is not None:
            # Increment all numeric values in the dictionary
            updated_data = {k: v - decrement_by if isinstance(v, (int, float)) else v for k, v in current_data.items()}
            # Update the data in the database
            self.update(key, updated_data)
        else:
            raise ValueError(f"The key '{key}' does not exist in the database or their is no integer field")

    def count(self) -> int:
        """
        Count the number of key-value pairs in the collection.

        Returns:
        - int: Number of key-value pairs in the collection.
        """
        data = self._load_data()
        return len(data)

    def wquery(self, query_str: str) -> Dict[str, Any]:
        """
        Query the collection using a regular expression.

        Parameters:
        - query_str: Regular expression string for matching values in the collection.

        Returns:
        - Dict[str, Any]: Key-value pairs that match the specified regular expression.
        """
        data = self._load_data()
        query = re.compile(query_str, re.IGNORECASE)
        return [{"key": key, "value": value} for key, value in data.items() if query.search(str(value))]
    
    def fetch(self, query_params: Optional[Dict[str, Union[str, int]]] = None) -> List[Dict[str, Any]]:
        """
        Fetch key-value pairs from the collection based on query parameters.

        Parameters:
        - query_params: Optional query parameters for filtering.

        Returns:
        - List[Dict[str, Any]]: Key-value pairs that match the specified query parameters.
        """
        data = self._load_data()

        if query_params is None:
            return list(data.values())

        query_result = [
            item for item in data.values() if self._apply_query_condition(item, query_params)
        ]
        return query_result

    def _apply_query_condition(self, item: Dict[str, Any], query_params: Dict[str, Union[str, int]]) -> bool:
        """
        Apply a query condition to filter key-value pairs.

        Parameters:
        - item: Key-value pair to be checked against the query condition.
        - query_params: Query parameters defining the condition.

        Returns:
        - bool: True if the item satisfies the query condition, False otherwise.
        """
        for key, condition in query_params.items():
            if key.endswith("?contains") and isinstance(item.get(key[:-9]), str) and isinstance(
                condition, str
            ):
                if condition.lower() not in item[key[:-9]].lower():
                    return False
            elif item.get(key) != condition:
                return False
        return True

    def flush(self) -> None:
        """
        Clear all key-value pairs from the collection.
        """
        self._save_data({})
