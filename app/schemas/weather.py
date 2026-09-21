from __future__ import annotations

from datetime import date

from pydantic import BaseModel, ConfigDict, Field

class WeatherSearchRequest (BaseModel):
    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )
    location: str = Field(min_length=2)
    start_date: date
    end_date: date


class Dailyweather (BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )
    date: date
    min_temperature_c: float
    max_temperature_c: float
    condition: str

    precipitation_probability: float | None = Field(
        default=None,
        ge=0,
        le=100,
    )


class WeatherSearchResult (BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )

    location: str

    forecast: list[Dailyweather] = Field(
        default_factory=list,
    )