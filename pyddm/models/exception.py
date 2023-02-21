EXCEPTIONS_TO_CONVERT = (FloatingPointError, OverflowError, ZeroDivisionError, IndexError, AssertionError)
"""Catch these exceptions during Dependence.get_X_safe() and instead raise DependenceValueError."""

class DependenceValueError(ValueError):
    """Thrown when the output of a Dependence is invalid, or it would be
    invalid if the computation were to proceed.
    
    This may be thrown by the built-in get_X_safe() method of a Dependence.
    In cases where that built-in check is not sufficient, it should also
    be thrown by the get_X() method that is written for each custom
    Dependence.
    """
    pass