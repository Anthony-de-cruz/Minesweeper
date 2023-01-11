import pygame

import logging as log
from scenes.scene import Scene


class SceneHandler:

    """A class to handle scenes."""

    def __init__(self):

        self.scenes = {}

        self.focused = pygame.sprite.GroupSingle()

    def create_scene(self, name: str, scene: Scene) -> None:

        """Creates a new scene.

        Raises
        ------
            ValueError: If a scene of that name already exists."""

        if name in self.scenes:
            raise ValueError("Scene already exists")

        else:
            self.scenes[name] = scene

    def remove_scene(self, name: str) -> None:

        """Removes a scene from the set.

        Raises
        ------
            ValueError: If the name parameter is not found."""

        if name in self.scenes:
            self.scenes.pop(name)

        else:
            raise ValueError("Not a valid scene name")

    def set_focus(self, name: str) -> None:

        """Set a scene to be focused by name.

        Raises
        ------
            ValueError: If the name is not found."""

        if name in self.scenes:
            self.focused.add(self.scenes[name])
            log.info(f"Scene: {name} focused.")

        else:
            raise ValueError("Not a valid scene name")

    def render_focus(self) -> pygame.Surface:

        """Renders the focused scene and returns the image.

        Returns
        -------
            pygame.surface.Surface: The rendered surface."""

        return self.focused.sprites()[0].render()

    def get_focus(self) -> Scene:

        """Returns the focused Scene object.

        Returns
        -------
            Scene: The scene object."""

        return self.focused.sprites()[0].rect
