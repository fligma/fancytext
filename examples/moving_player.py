from fancytext import Engine

class PlayerGame(Engine):
    def setup(self):
        self.px = 10
        self.py = 5
        self.score = 0

    def update(self, dt: float, key: str | None):
        # Movement
        if key == "w":
            self.py = max(1, self.py - 1)
        elif key == "s":
            self.py = min(self.height - 2, self.py + 1)
        elif key == "a":
            self.px = max(1, self.px - 1)
        elif key == "d":
            self.px = min(self.width - 2, self.px + 1)

    def draw(self, renderer):
        # Draw Border Frame
        renderer.draw_box(0, 0, self.width, self.height)
        
        # Draw HUD
        renderer.draw_text(2, 0, "[ FancyText Engine Demo - Press 'Q' to Quit ]")
        renderer.draw_text(2, self.height - 1, f" Position: ({self.px}, {self.py}) ")

        # Draw Player
        renderer.draw_char(self.px, self.py, "@")

if __name__ == "__main__":
    game = PlayerGame(width=60, height=18, target_fps=30)
    game.run()