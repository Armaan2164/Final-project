import pygame
import random
import math
from noise import pnoise2

WIDTH, HEIGHT = 900, 700
PARTICLE_COUNT = 1000
NOISE_SCALE = 0.005

x_offset = random.uniform(0, 1000)
y_offset = random.uniform(0, 1000)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Generative Flow Field Art")
clock = pygame.time.Clock()

screen.fill((10, 10, 15))


class Particle:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)

        self.speed = random.uniform(0.5, 3)
        self.size = random.randint(1, 3)

        self.color = (
            random.randint(100, 255),
            random.randint(100, 255),
            random.randint(100, 255)
        )

        self.angle_multiplier = random.uniform(2, 8)

    def move(self):
        angle = pnoise2(
            self.x * NOISE_SCALE + x_offset,
            self.y * NOISE_SCALE + y_offset
        ) * math.pi * self.angle_multiplier

        self.x += math.cos(angle) * self.speed
        self.y += math.sin(angle) * self.speed

        self.x %= WIDTH
        self.y %= HEIGHT

    def draw(self, surface):
        pygame.draw.circle(
            surface,
            self.color,
            (int(self.x), int(self.y)),
            self.size
        )


particles = [Particle() for _ in range(PARTICLE_COUNT)]

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                pygame.image.save(screen, "flow_field_art.png")
                print("Saved image!")

            if event.key == pygame.K_r:
                screen.fill((10, 10, 15))

                x_offset = random.uniform(0, 1000)
                y_offset = random.uniform(0, 1000)

                particles = [Particle() for _ in range(PARTICLE_COUNT)]
                print("Reset with new randomized particles!")

    for particle in particles:
        particle.move()
        particle.draw(screen)

    pygame.display.flip()

pygame.quit()


