import math

class Colors:
    """ANSI color code helper class for terminal styling."""
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"

    # Foreground Colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # Bright Foreground Colors
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

def colorize(text: str, color_code: str) -> str:
    """Wraps text with ANSI escape sequence codes."""
    return f"{color_code}{text}{Colors.RESET}"

def clamp(val: float, min_val: float, max_val: float) -> float:
    """Clamps a value between a minimum and maximum threshold."""
    return max(min_val, min(val, max_val))

def lerp(start: float, end: float, t: float) -> float:
    """Linear interpolation between start and end values."""
    return start + (end - start) * clamp(t, 0.0, 1.0)