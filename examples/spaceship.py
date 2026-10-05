import random
from fancytext import Engine, Entity, Vector2, Colors, colorize

class Bullet(Entity):
    def __init__(self, x: float, y: float):
        super().__init__(x=x, y=y, sprite="│")
        self.speed = 35.0

    def update(self, dt: float):
        self.position.y -= self.speed * dt
        if self.position.y < 1:
            self.active = False

class Enemy(Entity):
    def __init__(self, x: float, y: float, speed: float):
        super().__init__(x=x, y=y, sprite=["/█\\", "\\█/"])
        self.speed = 5

    def update(self, dt: float):
        self.position.y += self.speed * dt

class SpaceShooter(Engine):
    def setup(self):
        self.reset_game()

    def reset_game(self):
        self.player = Entity(x=37, y=18, sprite=["  ▲  ", " /█\\ ", "<===>"])
        self.bullets: list[Bullet] = []
        self.enemies: list[Enemy] = []
        
        self.score = 0
        self.lives = 3
        
        self.spawn_timer = 0.0
        self.spawn_interval = 0.8
        
        self.fire_timer = 0.0
        self.fire_rate = 0.15 
        
        self.game_over = False

    def update(self, dt: float, keys: set[str]):
        if self.game_over:
            if "r" in keys:
                self.reset_game()
            return

        move_speed = 28.0 * dt
        if "a" in keys:
            self.player.position.x = max(1, self.player.position.x - move_speed)
        if "d" in keys:
            self.player.position.x = min(self.width - self.player.width - 1, self.player.position.x + move_speed)
        if "w" in keys:
            self.player.position.y = max(1, self.player.position.y - move_speed)
        if "s" in keys:
            self.player.position.y = min(self.height - self.player.height - 1, self.player.position.y + move_speed)

        self.fire_timer += dt
        if ("space" in keys or "f" in keys) and self.fire_timer >= self.fire_rate:
            self.fire_timer = 0.0
            self.bullets.append(Bullet(self.player.position.x + 2, self.player.position.y - 1))

        for bullet in self.bullets:
            if bullet.active: bullet.update(dt)
        self.bullets = [b for b in self.bullets if b.active]

        self.spawn_timer += dt
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_timer = 0.0
            self.enemies.append(Enemy(random.randint(2, self.width - 5), 1, random.uniform(7.0, 14.0)))

        for enemy in self.enemies:
            if enemy.active:
                enemy.update(dt)
                if enemy.position.y >= self.height - 2 or enemy.collides_with(self.player):
                    enemy.active = False
                    self.lives -= 1
                    if self.lives <= 0:
                        self.game_over = True

        for bullet in self.bullets:
            if not bullet.active: continue
            for enemy in self.enemies:
                if enemy.active and bullet.collides_with(enemy):
                    bullet.active = False
                    enemy.active = False
                    self.score += 100
                    break

        self.enemies = [e for e in self.enemies if e.active]

    def draw(self, renderer):
        renderer.draw_box(0, 0, self.width, self.height)
        
        hud = f" SCORE: {self.score} | LIVES: {'♥ ' * self.lives} "
        renderer.draw_text(2, 0, colorize(hud, Colors.BRIGHT_CYAN))
        renderer.draw_text(self.width - 22, 0, "[ WASD | SPACE | ESC ]")

        if self.game_over:
            cy = self.height // 2
            renderer.draw_text((self.width - 15) // 2, cy - 1, colorize("=== GAME OVER ===", Colors.BRIGHT_RED))
            renderer.draw_text((self.width - 15) // 2, cy, colorize(f"Final Score: {self.score}", Colors.BRIGHT_YELLOW))
            renderer.draw_text((self.width - 33) // 2, cy + 1, "Press 'R' to Restart or 'ESC' to Quit")
            return

        self.player.draw(renderer)
        for bullet in self.bullets: bullet.draw(renderer)
        for enemy in self.enemies: enemy.draw(renderer)

if __name__ == "__main__":
    game = SpaceShooter(width=80, height=24, target_fps=30)
    game.run()