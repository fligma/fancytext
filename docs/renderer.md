# renderer.py Documentation

## Class: TerminalRenderer
Handles double-buffered character terminal rendering[cite: 6].

### `__init__(self, width: int = 80, height: int = 24)`
Initializes grid buffer dimensions, fills buffer with spaces, and hides cursor[cite: 6].

### `clear(self)`
Clears internal buffer contents back to empty spaces[cite: 6].

### `draw_char(self, x: int, y: int, char: str)`
Places a character into the buffer at designated grid bounds[cite: 6].

### `draw_text(self, x: int, y: int, text: str)`
Writes a string horizontally starting from coordinate `(x, y)`[cite: 6].

### `draw_box(self, x: int, y: int, width: int, height: int)`
Renders a border frame using ASCII line-drawing characters[cite: 6].

### `render(self)`
Flushes complete buffer to terminal output in a single frame write[cite: 6].

### `cleanup(self)`
Restores terminal cursor visibility and clears stdout[cite: 6].