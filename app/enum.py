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

class ToolErrorType(str, Enum):
    TIMEOUT = "Timeout"
    PROVIDER_ERROR = "provider_error"
    VALIDATION_ERROR = "validation_error"
    NOT_FOUND = "nor_found"
    UNKNOWN = "unknown"