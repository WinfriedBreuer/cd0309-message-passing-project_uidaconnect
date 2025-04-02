from __future__ import annotations

from datetime import datetime

from app import db  # noqa
from sqlalchemy import Column, Integer, String

class Person(db.Model):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    company_name = Column(String, nullable=False)