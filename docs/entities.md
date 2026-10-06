# entities.py Documentation

## Class: Entity
Base class for interactive game objects with position, velocity, and multi-line ASCII sprite rendering[cite: 3].

### `__init__(self, x: float = 0.0, y: float = 0.0, sprite: str | list[str] = "@")`
Initializes positional vectors, velocity vector, activity state, and normalizes sprite inputs into a list of strings[cite: 3].

### `width(self) -> int` (Property)
Calculates and returns the length of the longest line in the entity's sprite[cite: 3].

### `height(self) -> int` (Property)
Returns the total number of lines in the entity's sprite[cite: 3].

### `get_bounds(self) -> Rect`
Generates and returns an axis-aligned bounding box (`Rect`) corresponding to the entity's current position and dimensions[cite: 3].

### `collides_with(self, other: Entity) -> bool`
Evaluates AABB collision between this entity and another entity; returns `False` if either entity is inactive[cite: 3].

### `update(self, dt: float, key: str | None = None)`
Updates position based on current velocity scaled by delta time[cite: 3].

### `draw(self, renderer: TerminalRenderer)`
Renders each line of the entity's sprite to the buffer at integer-rounded position coordinates[cite: 3].