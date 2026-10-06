# math.py Documentation

## Class: Vector2
Represents a 2D vector for positions, velocities, and grid geometry[cite: 5].

### `__init__(self, x: float = 0.0, y: float = 0.0)`
Constructs a new vector with float conversion for `x` and `y`[cite: 5].

### `__add__(self, other: Vector2) -> Vector2`
Returns the vector sum of this vector and another[cite: 5].

### `__sub__(self, other: Vector2) -> Vector2`
Returns the vector difference between this vector and another[cite: 5].

### `__mul__(self, scalar: float) -> Vector2`
Returns a new vector scaled by a scalar multiplier[cite: 5].

### `__eq__(self, other: object) -> bool`
Performs floating-point safe equality comparison with another `Vector2`[cite: 5].

### `__repr__(self) -> str`
Returns formatted string representation of vector coordinates[cite: 5].

### `int_x(self) -> int` (Property)
Returns the `x` coordinate rounded to the nearest integer[cite: 5].

### `int_y(self) -> int` (Property)
Returns the `y` coordinate rounded to the nearest integer[cite: 5].

### `magnitude(self) -> float`
Calculates and returns the scalar length of the vector[cite: 5].

### `distance_to(self, other: Vector2) -> float`
Calculates Euclidean distance to another vector[cite: 5].

### `copy(self) -> Vector2`
Returns a new `Vector2` clone with identical coordinates[cite: 5].

## Class: Rect
Represents an axis-aligned bounding box (AABB) for collision detection[cite: 5].

### `__init__(self, x: float, y: float, width: float, height: float)`
Initializes rectangle coordinates and dimensions[cite: 5].

### `left(self) -> float` (Property)
Returns minimum X coordinate[cite: 5].

### `right(self) -> float` (Property)
Returns maximum X coordinate (`x + width`)[cite: 5].

### `top(self) -> float` (Property)
Returns minimum Y coordinate[cite: 5].

### `bottom(self) -> float` (Property)
Returns maximum Y coordinate (`y + height`)[cite: 5].

### `contains(self, point: Vector2) -> bool`
Evaluates if a point vector is inside the rectangle's boundary[cite: 5].

### `intersects(self, other: Rect) -> bool`
Evaluates AABB overlap with another `Rect`[cite: 5].