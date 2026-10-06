# utils.py Documentation

## Class: Colors
ANSI escape code constants for text formatting and color styling[cite: 7].

## Standalone Functions

### `colorize(text: str, color_code: str) -> str`
Wraps a string with a given ANSI escape code sequence and appends a reset code[cite: 7].

### `clamp(val: float, min_val: float, max_val: float) -> float`
Restricts a value between minimum and maximum bounds[cite: 7].

### `lerp(start: float, end: float, t: float) -> float`
Performs linear interpolation between `start` and `end` with `t` clamped to `[0.0, 1.0]`[cite: 7].