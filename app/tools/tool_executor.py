from __future__ import annotations

import asyncio
from time import perf_counter

from app.schemas.plan_step import PlanStep
from app.schemas.tool import ToolInput, ToolResult
from app.tools.tool_registry import ToolRegistry

from app.enum import ToolErrorType

class ToolExecutor:
    """
        Executes planner selected tools with timeout handling.
    """
    def __init__(
            self,
            timeout_secoonds: float = 15.0
        ) -> None:
        self._timeout_secoonds = timeout_secoonds

    
    async def execute(
            self,
            step: PlanStep
    ) -> ToolResult:
        
        tool_cls = ToolRegistry.get(
            step.tool_name or ""
        )

        tool = tool_cls()
        try:
            result = await asyncio.wait_for(
                tool.execute(
                    ToolInput(arguments=step.arguments)
                ),
                timeout=self._timeout_secoonds,
            )
        except asyncio.TimeoutError:
            return ToolResult(
                tool_name=step.tool_name or "unknown",
                success=False,
                error="tool execution time out",
                error_type=ToolErrorType.TIMEOUT
            )
            

        return result