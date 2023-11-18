import pygame as pg

class Frog(pg.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.width = 128
        self.height = 64
        self.sprites = []
        total_sprites = 10
        for i in range(total_sprites):
            self.sprites.append(pg.image.load(f"assets/frog_{i + 1}.png"))
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.current_sprite = 0
        self.animation_speed = 0.01
        self.animation_time = 0
        self.animation_frames = total_sprites
        self.animation_frame = 0

    def act(self):
        self.animation_time = self.animation_frames

    def update(self):
        if self.animation_time >= self.animation_speed:
            self.animation_time = self.animation_time - self.animation_speed
            self.animation_frame = int(self.animation_time)
            self.image = self.sprites[self.animation_frame]