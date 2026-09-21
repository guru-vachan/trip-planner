from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, model_validator

from datetime import date

from app.schemas.preferences import TravelPreferences

class TripRequest(BaseModel):
    
    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )

    source: str = Field(
        min_length=2
    )

    destination: str = Field(
        min_length=2
    )

    start_date: date
    end_date: date

    travelers: int = Field(
        default=1,
        ge=1,
        le=20
    )

    budget: float | None = Field(
        default=None,
        ge=0
    )

    currency: str = Field(
        default="INR",
        ge=3,
        le=3,
    )

    preferences: TravelPreferences = Field(
        default_factory=TravelPreferences
    )


    @model_validator(mode="after")
    def validate_dates(self) -> "TripRequest":
        if self.end_date < self.start_date:
            raise ValueError(
                "end date must be on after start date."
            )
        
        return self
    

    @property
    def duration_days(self) -> int:
        return(
            self.end_date - self.start_date
        ).days + 1
