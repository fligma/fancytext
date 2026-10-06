# renderer.py Documentation

## Class: TerminalRenderer
Handles double-buffered character terminal rendering.

### `__init__(self, width: int = 80, height: int = 24)`
Initializes grid buffer dimensions, fills buffer with spaces, and hides cursor.

### `clear(self)`
Clears internal buffer contents back to empty spaces.

### `draw_char(self, x: int, y: int, char: str)`
Places a character into the buffer at designated grid bounds.

### `draw_text(self, x: int, y: int, text: str)`
Writes a string horizontally starting from coordinate `(x, y)`.

### `draw_box(self, x: int, y: int, width: int, height: int)`
Renders a border frame using ASCII line-drawing characters.

### `render(self)`
Flushes complete buffer to terminal output in a single frame write.

### `cleanup(self)`
Restores terminal cursor visibility and clears stdout.
