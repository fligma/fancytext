from pynput import keyboard

class InputHandler:
    def __init__(self):
        self.keys_pressed = set()
        self.listener = keyboard.Listener(
            on_press=self.on_press, 
            on_release=self.on_release
        )

    def start(self):
        """Starts the background keyboard listener thread."""
        self.listener.start()

    def on_press(self, key):
        """Adds a key to the pressed set."""
        try:
            self.keys_pressed.add(key.char.lower())
        except AttributeError:
            # Handles special keys by their enum name (e.g., "space", "esc", "shift")
            if key is not None:
                self.keys_pressed.add(key.name)

    def on_release(self, key):
        """Removes a key from the pressed set upon release."""
        try:
            self.keys_pressed.discard(key.char.lower())
        except AttributeError:
            if key is not None:
                self.keys_pressed.discard(key.name)

    def poll_keys(self) -> set[str]:
        """Returns a snapshot copy of all currently held keys."""
        return self.keys_pressed.copy()

    def stop(self):
        """Safely terminates the listener thread."""
        self.listener.stop()