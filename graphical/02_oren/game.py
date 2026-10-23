"""Your program goes in this file."""

from dataclasses import dataclass

import pygame

app_size = (640, 480)

STEP = 30
RADIUS = 70
line_thickness = 5

@dataclass
class State:
    x: float = 320


def setup():
    return State()


def on_key_down(state: State, key):
    if key == pygame.K_LEFT:
        state.x -= STEP
    if key == pygame.K_RIGHT:
        state.x += STEP


def draw(screen: pygame.Surface, state: State):
    screen.fill("white")
    pygame.draw.circle(screen, "black", (state.x, 240), RADIUS, 5)
    pygame.draw.circle(screen, "black", (290, 240), 10, 3)
    pygame.draw.circle(screen, "black", (340,240), 10, 3)
    pygame.draw.line(screen, "black", (315,250), (325,260), 3)
    pygame.draw.line(screen, "black", (315,260), (325,260), 3)
    pygame.draw.line(screen, "black", (310,270), (330,270), 3)
