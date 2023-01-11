import pygame

import logging as log
from scenes import scene


class SceneHandler:

    """A class to handle scenes."""

    def __init__(self):

        self.scenes = {}

        self.focused = pygame.sprite.GroupSingle()

    def create_scene(self, name: str, scene: scene.Scene) -> None:

        """Creates a new scene. Throws ValueError if it already exists."""

        if name in self.scenes:
            raise ValueError("Scene already exists")

        else:
            self.scenes[name] = scene

    def remove_scene(self, name: str) -> None:

        """Removes a scene from the set. Throws ValueError if not found."""

        if name in self.scenes:
            self.scenes.pop(name)

        else:
            raise ValueError("Not a valid scene name")

    def set_focus(self, name: str) -> None:

        """Set a scene to be focused by name. Throws ValueError if the name is not found."""

        if name in self.scenes:
            self.focused.add(self.scenes[name])
            log.info("Scene: ", name, " focused.")
        
        else:
            raise ValueError("Not a valid scene name")


