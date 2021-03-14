import os
import pygame


class Settings():

    def __init__(self):

        self.width = 750
        self.height = 600
        self.color = (230, 230, 230)
        self.bg = pygame.transform.scale(pygame.image.load(os.path.join(
            "images", "background-black.png")), (self.width, self.height))

        self.ship_limit = 3

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullet_allowed = 5

        self.fleet_drop_speed = 10

        self.speedup_scale = 1.2
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 10
        self.bullet_speed = 10
        self.alien_speed = 5
        self.fleet_direction = 1
        self.alien_points = 100

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
