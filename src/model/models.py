from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from data.database import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password_hash = Column(String(255))
    created_at = Column(DateTime)


class Note(Base):
    __tablename__ = "notes"
    note_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    content = Column(String(255))
    is_completed = Column(Boolean, default=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    user = relationship("User", back_populates="notes")

class Label(Base):
    __tablename__ = "labels"
    label_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class NoteLabel(Base):
    __tablename__ = "note_labels"
    note_id = Column(Integer, ForeignKey("notes.note_id"), primary_key=True)
    label_id = Column(Integer, ForeignKey("labels.label_id"), primary_key=True)

    note = relationship("Note", back_populates="labels")
    label = relationship("Label", back_populates="notes")