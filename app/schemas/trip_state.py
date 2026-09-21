from __future__ import annotations

from typing import Any
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field, model_validator


from app.schemas.budget import BudgetState
from app.schemas.preferences import TravelPreferences
from app.schemas.itinerary import Itinerary
from app.schemas.memory import MemoryContext
from app.schemas.trip_request import TripRequest
from app.schemas.plan_step import ExecutionPlan

class TripState(BaseModel):
    """
        Mutable state shared across the LangGraph trip planning workflow.
    """
    model_config = ConfigDict(
        extra="forbid"
    )

    request_id: str = Field(
        default_factory=lambda: str(uuid4())
    )

    # original user input
    raw_request: str = Field(
        min_length=1
    )
    # requirement extraction
    trip_request: TripRequest | None = None
    # fetch before planing
    memory_context: MemoryContext | None = None

    execution_plan: ExecutionPlan | None = None

    tool_results: dict[str,Any] = Field(
        default_factory=dict
    )

    budget_state: BudgetState | None = None

    validation_errors: list[str] = Field(
        default_factory=list
    )

    # replaning
    replan_count: int = Field(
        default=0,
        gt=0
    )

    # final structured plan 
    itinerary: Itinerary | None = None

    require_human_approval: bool = False

    final_response: str | None = None

    error: str | None = None


