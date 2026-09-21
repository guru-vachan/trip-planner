from __future__ import annotations

from enum import Enum

class TravelPlace(str, Enum):
    RELAXED = "relaxed"
    MODERATE = "moderate"
    FAST = "fast"

class StepStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED="failed"
    SKIPPED="skipped"