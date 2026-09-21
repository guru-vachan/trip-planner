from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, model_validator

from app.schemas.preferences import TravelPreferences

class PreviousTripMemory(BaseModel):
    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )

    destination: str
    summery: str

    useful_preferences: list[str] = Field(
        default_factory=list
    )


class MemoryContext(BaseModel):
    """
    memories fetch before trip planning.
    """
    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )

    user_preferences: TravelPreferences = Field(
        default_factory=TravelPreferences
    )

    previous_trips: list[PreviousTripMemory] = Field(
        default_factory=list
    )

    notes: list[str] = Field(
        default_factory=list
    )

