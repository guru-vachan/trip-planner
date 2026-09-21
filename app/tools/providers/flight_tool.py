from __future__ import annotations

from typing import Protocol

from pydantic import ValidationError

from app.schemas.flight  import (
    FlightOption,
    FlightSearchRequest,
    FlightSearchResult
)
from app.schemas.tool import (
    ToolErrorType,
    ToolInput,
    ToolResult
)
from app.tools.interfaces.base_tool import BaseTool
from app.tools.tool_registry import ToolRegistry

class FlightProviderclient (Protocol):
    """
        Contract for external flight providers

        FlightTool -> Amadeus Flight Client -> Flight Provider Client
    """

    async def search_flights(
            self,
            request: FlightSearchRequest,
    ) -> list[FlightOption] :
        # call Amadeus ApI
        # parse response
        # return Flight option list
        ...


@ToolRegistry.register
class FlightTool(BaseTool):

    def __init__(
            self,
            client: FlightProviderclient,    
        ) -> None:
        
        self._client = client

    @classmethod
    def name (cls) -> str:
        return "flight_search"
    

    async def execute(
            self,
            tool_input: ToolInput,
    ) -> ToolResult:
        
        try:
            request = FlightSearchRequest.model_validate(
                tool_input.arguments
            )

        except ValidationError as exc:
            return ToolResult(
                tool_name=self.name(),
                success=False,
                error=str(exc),
                error_type=ToolErrorType.VALIDATION_ERROR,
            )
        
        try:

            flights = await self._client.search_flights(
                request
            )

            result = FlightSearchResult(
                flights=flights
            )

            return ToolResult(
                tool_name=self.name(),
                success=True,
                data=result.model_dump(mode="json")
            )
        
        except Exception as ex:
            return ToolResult(
                tool_name=self.name(),
                success=False,
                error=str(exc),
                error_type=ToolErrorType.PROVIDER_ERROR,
            ) 
