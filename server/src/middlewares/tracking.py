import time
from datetime import datetime
from typing import Callable, Awaitable

from starlette.requests import Request
from starlette.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware

from ..services.tracking import create_tracking


class TrackingMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ):
        start_time = time.time()
        current_datetime = datetime.utcnow()

        response = await call_next(request)

        create_tracking(start_time, current_datetime, response.status_code)

        return response
