# core.py Documentation

## Class: Engine
Manages core game execution, timing, and lifecycle[cite: 2].

### `__init__(self, width: int = 80, height: int = 24, target_fps: int = 30)`
Initializes the game engine parameters, target frame rate, frame duration, terminal renderer, and input handler[cite: 2].

### `setup(self)`
Lifecycle hook intended for subclass override to initialize custom game objects and state[cite: 2].

### `update(self, dt: float, keys: set[str])`
Lifecycle hook intended for subclass override to handle frame-by-frame entity and state updates given delta time (`dt`) and active keys (`keys`)[cite: 2].

### `draw(self, renderer: TerminalRenderer)`
Lifecycle hook intended for subclass override to perform rendering operations[cite: 2].

### `run(self)`
Starts the main engine loop, handles input polling, frame time delta calculations, update cycles, buffer rendering, frame-rate regulation, and cleanup upon exit[cite: 2].