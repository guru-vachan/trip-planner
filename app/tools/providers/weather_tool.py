from __future__ import annotations

from typing import Protocol

from pydantic import ValidationError

from app.schemas.weather  import (
    WeatherSearchRequest,
    WeatherSearchResult,
    Dailyweather
)
from app.schemas.tool import (
    ToolErrorType,
    ToolInput,
    ToolResult
)
from app.tools.interfaces.base_tool import BaseTool
from app.tools.tool_registry import ToolRegistry

class WeatherProviderClient (Protocol):

    async def get_forecast(
            self,
            request: WeatherSearchRequest,
    ) -> list[Dailyweather] :
        # call Amadeus ApI
        # parse response
        # return Flight option list
        ...


@ToolRegistry.register
class weatherTool (BaseTool):

    def __init__(
            self,
            client: WeatherProviderClient,    
        ) -> None:
        
        self._client = client

    @classmethod
    def name (cls) -> str:
        return "weather_search"
    

    async def execute(
            self,
            tool_input: ToolInput,
    ) -> ToolResult:
        
        try:

            request = WeatherSearchRequest.model_validate(
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

            forcast = await self._client.get_forecast(
                request
            )

            result = WeatherSearchResult(
                location=request.location,
                forecast=forcast
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