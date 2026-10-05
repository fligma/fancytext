import math

class Vector2:
    """Represents a 2D vector for positions, velocities, and grid coordinates."""
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other: "Vector2") -> "Vector2":
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector2") -> "Vector2":
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vector2":
        return Vector2(self.x * scalar, self.y * scalar)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector2):
            return False
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)

    def __repr__(self) -> str:
        return f"Vector2({self.x:.2f}, {self.y:.2f})"

    @property
    def int_x(self) -> int:
        return int(round(self.x))

    @property
    def int_y(self) -> int:
        return int(round(self.y))

    def magnitude(self) -> float:
        return math.hypot(self.x, self.y)

    def distance_to(self, other: "Vector2") -> float:
        return (other - self).magnitude()

    def copy(self) -> "Vector2":
        return Vector2(self.x, self.y)


class Rect:
    """Represents an axis-aligned bounding box (AABB) for collisions."""
    def __init__(self, x: float, y: float, width: float, height: float):
        self.x = float(x)
        self.y = float(y)
        self.width = float(width)
        self.height = float(height)

    @property
    def left(self) -> float: return self.x

    @property
    def right(self) -> float: return self.x + self.width

    @property
    def top(self) -> float: return self.y

    @property
    def bottom(self) -> float: return self.y + self.height

    def contains(self, point: Vector2) -> bool:
        """Checks if a point lies inside this rectangle."""
        return (self.left <= point.x < self.right) and (self.top <= point.y < self.bottom)

    def intersects(self, other: "Rect") -> bool:
        """Checks AABB collision between two rectangles."""
        return not (
            self.right <= other.left or
            self.left >= other.right or
            self.bottom <= other.top or
            self.top >= other.bottom
        )