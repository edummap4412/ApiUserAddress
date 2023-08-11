from src.errors import HttpUnprocessableEntityError
from src.presentation.http_types.http_response import HttpResponse
from src.errors.types.http_not_found import HttpNotFoundError
from src.errors.types.http_bad_request import HttpBadResquestError


def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpNotFoundError, HttpBadResquestError, HttpUnprocessableEntityError)):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )
