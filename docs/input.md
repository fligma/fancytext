# input.py Documentation

## Class: InputHandler
Manages background keyboard event listening and input polling.

### `__init__(self)`
Initializes active keys set and configures a `pynput.keyboard.Listener` instance.

### `start(self)`
Starts the background listener thread for capturing keyboard events.

### `on_press(self, key)`
Callback invoked when a key is pressed; parses standard standard character codes or special key names and adds them to the active set.

### `on_release(self, key)`
Callback invoked when a key is released; removes the corresponding key string from the active set.

### `poll_keys(self) -> set[str]`
Returns a thread-safe set copy of all currently held keys.

### `stop(self)`
Terminates the background keyboard listener thread safely.
