from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any

from app.enum import StepStatus

class PlanStep(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )

    step_id: str = Field(
        min_length=1
    )

    action: str = Field(
        min_length=1
    )

    tool_name: str | None = None

    arguments: dict[str,Any] = Field(
        default_factory=dict
    )

    depends_on: list[str] = Field(
        default_factory=list
    )

    status: StepStatus = StepStatus.PENDING


class ExecutionPlan(BaseModel):
    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )
    steps: list[PlanStep] = Field(
        default_factory=list
    )
