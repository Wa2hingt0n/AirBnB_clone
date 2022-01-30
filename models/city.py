#!/usr/bin/python3
"""
model city class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    public class attribute contains empty strings with state_id and name
    """

    state_id = ""
    name = ""
