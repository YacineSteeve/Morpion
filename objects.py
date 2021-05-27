from constants import *
import pygame

pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption("Morpion 2021")
window_surface = pygame.display.set_mode(window_resolution)

background_img = pygame.image.load("Pictures/grass2.jpeg")
background_img.convert_alpha()

loading_img = pygame.image.load("Pictures/start_3.jpg")
loading_img.convert_alpha()

title_font = pygame.font.Font("Fonts/ADELIA.otf", title_size)
loading_font = pygame.font.Font("Fonts/Sunday Morning.otf", loading_size)
copyright_font = pygame.font.Font("Fonts/AppleGaramond.ttf", copyright_size)

title_surface = title_font.render("MORPION", True, title_color)
loading_surface = loading_font.render("Chargement...", True, loading_color)
copyright_surface = copyright_font.render("Copyright©2021 | All rights reserved | BTAYS", True, copyright_color)
