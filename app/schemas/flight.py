from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class FlightSearchRequest (BaseModel):
    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )

    origin: str = Field(
        min_length=3, 
        max_length=3
    )
    destination: str = Field(
        min_length=3, 
        max_length=3
    )

    departure_date: str

    adults: int= Field(
        default=1, 
        ge=1
    )
    currency: str =Field(
        default="INR", 
        min_length=3, 
        max_length=3
    )


class FlightOption (BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )

    flight_id: str
    airline: str
    flight_number: str | None = None
    origin: str
    destination: str

    departure_at: datetime
    arrival_at: datetime

    duration_minutes: int = Field(
        gt=0
    )
    stops: int = Field(
        default=0, 
        ge=0
    )

    price: float = Field(gt=0)
    currency: str


class FlightSearchResult (BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )

    flights: list [FlightOption] = Field(
        default_factory=list
    ) 
