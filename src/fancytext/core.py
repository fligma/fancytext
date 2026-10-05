import time
from .renderer import TerminalRenderer
from .input import InputHandler

class Engine:
    def __init__(self, width: int = 80, height: int = 24, target_fps: int = 30):
        self.width = width
        self.height = height
        self.target_fps = target_fps
        self.frame_duration = 1.0 / target_fps
        
        self.renderer = TerminalRenderer(width, height)
        self.input = InputHandler()
        self.running = False

    def setup(self):
        pass

    # UPDATE SIGNATURE CHANGED: Now accepts a set of held strings
    def update(self, dt: float, keys: set[str]):
        pass

    def draw(self, renderer: TerminalRenderer):
        pass

    def run(self):
        self.running = True
        self.setup()
        self.input.start()

        last_time = time.time()

        try:
            while self.running:
                current_time = time.time()
                dt = current_time - last_time
                last_time = current_time

                # 1. Input Processing (Now retrieves multiple keys)
                keys = self.input.poll_keys()
                if "esc" in keys:  # Use Escape to quit universally
                    self.running = False
                    break

                # 2. Game State Update
                self.update(dt, keys)

                # 3. Render Frame
                self.renderer.clear()
                self.draw(self.renderer)
                self.renderer.render()

                # 4. Frame Rate Regulation
                elapsed = time.time() - current_time
                sleep_time = self.frame_duration - elapsed
                if sleep_time > 0:
                    time.sleep(sleep_time)

        finally:
            self.input.stop()
            self.renderer.cleanup()