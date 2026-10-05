from .math import Vector2, Rect
from .renderer import TerminalRenderer

class Entity:
    """Base game object class with position, multi-line sprite support, and bounds."""
    def __init__(self, x: float = 0.0, y: float = 0.0, sprite: str | list[str] = "@"):
        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.active = True
        
        # Format sprite lines
        if isinstance(sprite, str):
            self.sprite = [sprite]
        else:
            self.sprite = sprite

    @property
    def width(self) -> int:
        return max((len(line) for line in self.sprite), default=0)

    @property
    def height(self) -> int:
        return len(self.sprite)

    def get_bounds(self) -> Rect:
        """Returns the bounding rectangle for collision checks."""
        return Rect(self.position.x, self.position.y, self.width, self.height)

    def collides_with(self, other: "Entity") -> bool:
        """Checks collision against another entity."""
        if not self.active or not other.active:
            return False
        return self.get_bounds().intersects(other.get_bounds())

    def update(self, dt: float, key: str | None = None):
        """Applies velocity updates and custom entity logic."""
        self.position += self.velocity * dt

    def draw(self, renderer: TerminalRenderer):
        """Draws the multi-line ASCII sprite onto the renderer buffer."""
        if not self.active:
            return

        start_x = self.position.int_x
        start_y = self.position.int_y

        for row_idx, line in enumerate(self.sprite):
            renderer.draw_text(start_x, start_y + row_idx, line)