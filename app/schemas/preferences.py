from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from app.enum import TravelPlace


class TravelPreferences(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )

    interests: list[str] = Field(
        default=None,
        ge=1,
        le=5,
        description="prefered hotel star category"
    )

    pace: TravelPlace = TravelPlace.MODERATE

    dietary_preferences: list[str] = Field(
        default_factory=list
    )

    preferred_trasport: list[str] = Field(
        default_factory=list
    )
