# input.py Documentation

## Class: InputHandler
Manages background keyboard event listening and input polling[cite: 4].

### `__init__(self)`
Initializes active keys set and configures a `pynput.keyboard.Listener` instance[cite: 4].

### `start(self)`
Starts the background listener thread for capturing keyboard events[cite: 4].

### `on_press(self, key)`
Callback invoked when a key is pressed; parses standard standard character codes or special key names and adds them to the active set[cite: 4].

### `on_release(self, key)`
Callback invoked when a key is released; removes the corresponding key string from the active set[cite: 4].

### `poll_keys(self) -> set[str]`
Returns a thread-safe set copy of all currently held keys[cite: 4].

### `stop(self)`
Terminates the background keyboard listener thread safely[cite: 4].