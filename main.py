import sys
import pygame
from settings import Settings
from ship import Ship
import function as f
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run():
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode((setting.width, setting.height))
    pygame.display.set_caption("Alien Invasion Project")

    play_button = Button(setting, screen, "Click mouse button to play")

    stats = GameStats(setting)
    sb = Scoreboard(setting, screen, stats)

    ship = Ship(setting, screen)
    bullets = Group()
    aliens = Group()

    f.create_fleet(setting, screen, ship, aliens)
    WIN = pygame.display.set_mode((setting.width, setting.height))

    while True:

        f.check_event(setting, screen, stats, sb,
                      play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            WIN.blit(setting.bg, (0, 0))

            f.update_bullets(setting, screen, stats, sb, ship, aliens, bullets)
            f.update_aliens(setting,  screen, stats, sb, ship, aliens, bullets)

        f.update_event(setting, screen, stats, sb, ship,
                       aliens, bullets, play_button)


run()
