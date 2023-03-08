#!/usr/bin/python3
"""Class BaseModel."""

import uuid
from datetime import datetime


class BaseModel:
    """Class that defines all common attributes/methods for other classes."""

    def __init__(self):
        """Instances of the base model class.

        Args:
            id: unique identification.
            created_at: datetime - datetime when an instance is created.
            updated_at: datetime - datetime when an instance is modified.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Print class name, id, and dictionary representation."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Update attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary representation of the instance's attributes."""
        dict = self.__dict__.copy()
        dict['__class__'] = type(self).__name__
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()
        return dict