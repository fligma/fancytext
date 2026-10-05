import sys

class TerminalRenderer:
    def __init__(self, width: int = 80, height: int = 24):
        self.width = width
        self.height = height
        self.buffer = [[" " for _ in range(width)] for _ in range(height)]

        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

    def clear(self):
        """Resets the internal screen buffer to blank spaces."""
        for y in range(self.height):
            for x in range(self.width):
                self.buffer[y][x] = " "

    def draw_char(self, x: int, y: int, char: str):
        """Draws a single character at grid coordinates (x, y)."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.buffer[y][x] = char[0] if char else " "

    def draw_text(self, x: int, y: int, text: str):
        """Draws a string starting at (x, y)."""
        for i, char in enumerate(text):
            if x + i >= self.width:
                break
            self.draw_char(x + i, y, char)

    def draw_box(self, x: int, y: int, width: int, height: int):
        """Draws a border rectangle using ASCII characters."""
        for bx in range(x, x + width):
            self.draw_char(bx, y, "─")
            self.draw_char(bx, y + height - 1, "─")
        for by in range(y, y + height):
            self.draw_char(x, by, "│")
            self.draw_char(x + width - 1, by, "│")

        self.draw_char(x, y, "┌")
        self.draw_char(x + width - 1, y, "┐")
        self.draw_char(x, y + height - 1, "└")
        self.draw_char(x + width - 1, y + height - 1, "┘")

    def render(self):
        """Flushes the buffer to the terminal screen in one write call."""
        frame_str = ["\033[H"] 
        for row in self.buffer:
            frame_str.append("".join(row) + "\n")
        
        sys.stdout.write("".join(frame_str))
        sys.stdout.flush()

    def cleanup(self):
        """Restores cursor visibility and clears the terminal upon exit."""
        sys.stdout.write("\033[?25h\033[2J\033[H")
        sys.stdout.flush()