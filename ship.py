import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, setting, screen):
        # initlize ship image and location
        super(Ship, self).__init__()
        self.screen = screen
        self.setting = setting

        # load ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # specify location of ship
        self.rect.centerx = self.screen_rect.centerx
        # self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        self.centerx = float(self.rect.centerx)
        # self.centery = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        # self.moving_up = False
        # self.moving_down = False

    def update(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.setting.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.centerx -= self.setting.ship_speed
        # elif self.moving_up and self.screen_rect.top > 0:
        #     self.centery -= self.setting.ship_speed
        # elif self.moving_down and self.screen_rect.bottom < self.screen_rect.bottom:
        #     self.centery += self.setting.ship_speed

        self.rect.centerx = self.centerx
        # self.rect.centery = self.centery

    def blitme(self):
        # draw ship
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
