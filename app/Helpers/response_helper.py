from flask import jsonify
from typing import Any, Optional, Union, Dict


def success_response(
    message: str = "Operation successful",
    data: Optional[Any] = None,
    status_code: int = 200,
) -> tuple[Any, int]:
    """
    Create a standardized success response

    Args:
        message: Success message
        data: Optional data to include in response
        status_code: HTTP status code (default: 200)

    Returns:
        Tuple of (jsonify response, status_code)
    """
    response_data = {"status": "success", "message": message}

    if data is not None:
        response_data["data"] = data

    return jsonify(response_data), status_code


def error_response(
    message: str = "An error occurred",
    error_code: Optional[str] = None,
    status_code: int = 400,
) -> tuple[Any, int]:
    """
    Create a standardized error response

    Args:
        message: Error message
        error_code: Optional error code for client handling
        status_code: HTTP status code (default: 400)

    Returns:
        Tuple of (jsonify response, status_code)
    """
    response_data = {"status": "error", "message": message}

    if error_code:
        response_data["error_code"] = error_code

    return jsonify(response_data), status_code


def validation_error_response(
    message: str = "Validation failed", errors: Optional[Dict[str, Any]] = None
) -> tuple[Any, int]:
    """
    Create a standardized validation error response

    Args:
        message: Validation error message
        errors: Dictionary of field-specific validation errors

    Returns:
        Tuple of (jsonify response, status_code)
    """
    response_data = {
        "status": "error",
        "message": message,
        "error_code": "VALIDATION_ERROR",
    }

    if errors:
        response_data["errors"] = errors

    return jsonify(response_data), 422


def not_found_response(resource: str = "Resource") -> tuple[Any, int]:
    """
    Create a standardized not found response

    Args:
        resource: Name of the resource that was not found

    Returns:
        Tuple of (jsonify response, status_code)
    """
    return error_response(
        message=f"{resource} not found", error_code="NOT_FOUND", status_code=404
    )


def unauthorized_response(message: str = "Unauthorized access") -> tuple[Any, int]:
    """
    Create a standardized unauthorized response

    Args:
        message: Unauthorized message

    Returns:
        Tuple of (jsonify response, status_code)
    """
    return error_response(message=message, error_code="UNAUTHORIZED", status_code=401)


def forbidden_response(message: str = "Access forbidden") -> tuple[Any, int]:
    """
    Create a standardized forbidden response

    Args:
        message: Forbidden message

    Returns:
        Tuple of (jsonify response, status_code)
    """
    return error_response(message=message, error_code="FORBIDDEN", status_code=403)


def server_error_response(message: str = "Internal server error") -> tuple[Any, int]:
    """
    Create a standardized server error response

    Args:
        message: Server error message

    Returns:
        Tuple of (jsonify response, status_code)
    """
    return error_response(message=message, error_code="SERVER_ERROR", status_code=500)
