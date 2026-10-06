# math.py Documentation

## Class: Vector2
Represents a 2D vector for positions, velocities, and grid geometry.

### `__init__(self, x: float = 0.0, y: float = 0.0)`
Constructs a new vector with float conversion for `x` and `y`.

### `__add__(self, other: Vector2) -> Vector2`
Returns the vector sum of this vector and another.

### `__sub__(self, other: Vector2) -> Vector2`
Returns the vector difference between this vector and another.

### `__mul__(self, scalar: float) -> Vector2`
Returns a new vector scaled by a scalar multiplier.

### `__eq__(self, other: object) -> bool`
Performs floating-point safe equality comparison with another `Vector2`.

### `__repr__(self) -> str`
Returns formatted string representation of vector coordinates.

### `int_x(self) -> int` (Property)
Returns the `x` coordinate rounded to the nearest integer.

### `int_y(self) -> int` (Property)
Returns the `y` coordinate rounded to the nearest integer.

### `magnitude(self) -> float`
Calculates and returns the scalar length of the vector.

### `distance_to(self, other: Vector2) -> float`
Calculates Euclidean distance to another vector.

### `copy(self) -> Vector2`
Returns a new `Vector2` clone with identical coordinates.

## Class: Rect
Represents an axis-aligned bounding box (AABB) for collision detection.

### `__init__(self, x: float, y: float, width: float, height: float)`
Initializes rectangle coordinates and dimensions.

### `left(self) -> float` (Property)
Returns minimum X coordinate.

### `right(self) -> float` (Property)
Returns maximum X coordinate (`x + width`).

### `top(self) -> float` (Property)
Returns minimum Y coordinate.

### `bottom(self) -> float` (Property)
Returns maximum Y coordinate (`y + height`).

### `contains(self, point: Vector2) -> bool`
Evaluates if a point vector is inside the rectangle's boundary.

### `intersects(self, other: Rect) -> bool`
Evaluates AABB overlap with another `Rect`.
