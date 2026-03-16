class FPGAError(Exception):
    """Base exception for FPGA errors."""
    pass

class FPGAConnectionError(FPGAError):
    """Connection failed or lost."""
    pass

class FPGATimeoutError(FPGAError):
    """Operation timed out."""
    pass
