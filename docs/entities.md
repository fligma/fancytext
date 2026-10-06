# entities.py Documentation

## Class: Entity
Base class for interactive game objects with position, velocity, and multi-line ASCII sprite rendering.

### `__init__(self, x: float = 0.0, y: float = 0.0, sprite: str | list[str] = "@")`
Initializes positional vectors, velocity vector, activity state, and normalizes sprite inputs into a list of strings.

### `width(self) -> int` (Property)
Calculates and returns the length of the longest line in the entity's sprite.

### `height(self) -> int` (Property)
Returns the total number of lines in the entity's sprite.

### `get_bounds(self) -> Rect`
Generates and returns an axis-aligned bounding box (`Rect`) corresponding to the entity's current position and dimensions.

### `collides_with(self, other: Entity) -> bool`
Evaluates AABB collision between this entity and another entity; returns `False` if either entity is inactive.

### `update(self, dt: float, key: str | None = None)`
Updates position based on current velocity scaled by delta time.

### `draw(self, renderer: TerminalRenderer)`
Renders each line of the entity's sprite to the buffer at integer-rounded position coordinates.
