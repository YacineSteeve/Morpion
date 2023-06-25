"""objs"""
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'


import pygame
from constants import *

pygame.init()

clock = pygame.time.Clock()

window_surface = pygame.display.set_mode(window_resolution)

icon_img = pygame.image.load("./Pictures/noughts-and-crosses.png")
icon_img.convert_alpha()

background_img_2 = pygame.image.load("./Pictures/wood_4.jpg")
background_img_2.convert_alpha()

loading_img = pygame.image.load("./Pictures/start_3.jpg")
loading_img.convert_alpha()

pygame.display.set_caption("Morpion")
pygame.display.set_icon(icon_img)

title_font = pygame.font.Font("./Fonts/ADELIA.otf", title_size)
playing_title_font = pygame.font.Font("./Fonts/ADELIA.otf", playing_title_size)
loading_font = pygame.font.Font("./Fonts/Sunday Morning.otf", loading_size)
copyright_font = pygame.font.Font("./Fonts/AppleGaramond.ttf", copyright_size)
winner_font = pygame.font.Font("./Fonts/Asdonuts.otf", winner_size)
start_font = pygame.font.Font("./Fonts/Sunday Morning.otf", start_text_size)
turn_font = pygame.font.Font(None, turn_text_size)

title_surface = title_font.render("MORPION", True, title_color)
playing_title_surface = playing_title_font.render("MORPION", False, playing_title_color)
loading_surface = loading_font.render("Chargement...", True, loading_color)
copyright_surface = copyright_font.render(
    "Copyright©2021 | All rights reserved | BTAYS", True, 
    copyright_color
)
equality_surface = winner_font.render("Match nul !", True, winner_color)
start_text_surface = start_font.render("Jouer", True, start_text_color)

start_box = pygame.Rect(start_box_position, start_box_dimensions)
