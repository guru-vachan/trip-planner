from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any

from datetime import date, time

class Activity(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )
    name: str = Field(
        min_length=1
    )

    location: str | None = None

    start_time: time | None = None

    duration_minutes: int | None = Field(
        default=None,
        gt=0
    )

    estimated_cost: float = Field(
        default=0,
        gt=0
    )

    notes: str | None = None


class ItineraryDay(BaseModel):
    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )

    day: int = Field(
        ge=1,
    )

    date: date

    activities: list[Activity] = Field(
        default_factory=list
    )


class Itinerary(BaseModel):
    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )
    destination: str 

    days: list[ItineraryDay] = Field(
        default_factory=list
    )

    estimated_total_cost: float = Field(
        default=0,
        gt=0
    )

