import sys
import pygame
from time import sleep
from pygame.sprite import Group
import shelve

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_func as gf

def run_game():
    pygame.init()

    #настройки
    ai_settings = Settings()

    #экран
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
        )
    pygame.display.set_caption("Kolyan Invasion")

    #кнопка
    play_button = Button(ai_settings, screen, "ФЛОТ КОЛЯНОВ АТАКУЕТ!")

    #статистика
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #цвет фона
    bg_color = (255, 136, 77)

    #создание корабля, пуль и пришельцев
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
     
    #создание первого флота
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #запуск игрового цикла
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()