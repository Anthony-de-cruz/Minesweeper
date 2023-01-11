import pygame

class GameObject(pygame.sprite.Sprite):

    def __init__(self, x_coord: int, y_coord: int, image: pygame.Surface, *group: pygame.sprite.Group):

        