import pygame
import random
import math
from noise import pnoise2

WIDTH, HEIGHT = 900, 700
PARTICLE_COUNT = 1000
NOISE_SCALE = 0.005
SPEED = 2

# Random offsets make the artwork different every run
x_offset = random.uniform(0, 1000)
y_offset = random.uniform(0, 1000)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Generative Flow Field Art")
clock = pygame.time.Clock()

screen.fill((10, 10, 15))


