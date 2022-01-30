#!/usr/bin/python3
"""
model Review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Public class attributes:
    place_id: empty string
    user_id: empty string
    text: empty string
    """

    place_id = ""
    user_id = ""
    text = ""
