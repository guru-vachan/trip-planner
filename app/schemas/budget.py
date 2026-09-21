from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, model_validator

class BudgetState(BaseModel):

    model_config = ConfigDict(
        extra="forbid"
    )

    total_budget: float = Field(gt=0)

    flight_cost: float = Field(
        default=0,
        gt=0
    )
    hotel_cost: float = Field(
        default=0,
        gt=0
    )
    
    activity_cost: float = Field(
        default=0,
        gt=0
    )
    transport_cost: float = Field(
        default=0,
        gt=0
    )
    food_cost: float = Field(
        default=0,
        gt=0
    )

    currency: str = Field(
        default="INR",
        ge=3,
        le=3,
    )

    @property
    def estimated_total(self) -> float:
        return (
            self.flight_cost
            + self.hotel_cost
            + self.activity_cost
            + self.transport_cost
            + self.food_cost
        )
    
    @property
    def remaining_budget(self) -> float:
        return self.total_budget - self.estimated_total
    
    @property
    def within_budget(self) -> float:
        return self.remaining_budget > 0