class BusinessException(Exception):
    """Custom exception for business logic errors."""
    pass

class InvalidInputException(BusinessException):
    """Raised when the input provided is invalid."""
    pass

class UnauthorizedAccessException(BusinessException):
    """Raised when there is an unauthorized access attempt."""
    pass

class ResourceNotFoundException(BusinessException):
    """Raised when a required resource is not found."""
    pass

class OperationNotAllowedException(BusinessException):
    """Raised when an operation is not allowed."""
    pass