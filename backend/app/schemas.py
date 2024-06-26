"""
Pydantic models for the FastAPI app
"""

from datetime import date, datetime
from enum import Enum

from pydantic import BaseModel, EmailStr


class GenderEnum(str, Enum):
    male = "Male"
    female = "Female"


class GoalEnum(str, Enum):
    build_projects = "Build Projects"
    prepare_for_coding_interviews = "Prepare for Coding Interviews"
    both = "Both"


class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    bio: str | None = None
    profile_image: str | None = None
    date_of_birth: date
    gender: GenderEnum
    country: str
    city: str
    github_profile: str
    linkedin_profile: str
    skill_proficiencies: list[str]
    highest_education: str
    experience_years: int
    hobbies: list[str]
    languages: list[str]
    goal: GoalEnum
    commitment_hours: int


class User(UserBase):
    id: int | None = None
    password: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        # Pydantic ORM mode (formerly 'orm_mode')
        from_attributes = True


class UserRegister(User):
    pass


class UserPublic(UserBase):
    id: int

    class Config:
        # Pydantic ORM mode (formerly 'orm_mode')
        from_attributes = True


class UserUpdate(BaseModel):
    email: EmailStr | None = None
    full_name: str | None = None
    bio: str | None = None
    profile_image: str | None = None
    date_of_birth: date | None = None
    gender: GenderEnum | None = None
    country: str | None = None
    city: str | None = None
    github_profile: str | None = None
    linkedin_profile: str | None = None
    skill_proficiencies: list[str] | None = None
    highest_education: str | None = None
    experience_years: int | None = None
    hobbies: list[str] | None = None
    languages: list[str] | None = None
    goal: GoalEnum | None = None
    commitment_hours: int | None = None


class UserMatch(UserBase):
    id: int

    class Config:
        # Pydantic ORM mode (formerly 'orm_mode')
        from_attributes = True


# Generic message
class Message(BaseModel):
    details: str


# JSON payload containing access token
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# Contents of JWT token
class TokenPayload(BaseModel):
    sub: int | None = None
