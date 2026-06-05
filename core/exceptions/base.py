from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


class AppException(Exception):
    def __init__(self, message: str, code: str = "error"):
        self.message = message
        self.code = code
        super().__init__(self.message)


class NotFoundException(AppException):
    def __init__(self, message: str = "Registro não encontrado"):
        super().__init__(message, code="not_found")


class ConflictException(AppException):
    def __init__(self, message: str = "Conflito de dados"):
        super().__init__(message, code="conflict")


class BusinessRuleException(AppException):
    def __init__(self, message: str = "Regra de negócio violada"):
        super().__init__(message, code="business_rule")


class InvalidOperationException(AppException):
    def __init__(self, message: str = "Operação inválida"):
        super().__init__(message, code="invalid_operation")


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, AppException):
        return Response(
            {"detail": exc.message, "code": exc.code},
            status=status.HTTP_400_BAD_REQUEST,
        )

    return response
