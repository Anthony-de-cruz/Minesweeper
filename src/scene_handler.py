import logging

import pygame

from scenes.scene import Scene


log = logging.getLogger(__name__)


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

    def update_focus(self, event_list: list) -> None:

        """Updates the focused scene.

        Parameters
        ----------
            list[pygame.Event]: Event list to be passed to the scene."""

        self.focused.sprite.update(event_list)

    def render_focus(self) -> pygame.surface.Surface:

        """Renders the focused scene and returns the image.

        Returns
        -------
            pygame.surface.Surface: The rendered surface."""

        return self.focused.sprite.render()

    def get_focus(self) -> Scene:

        """Returns the focused Scene object.

        Returns
        -------
            Scene: The scene object."""

        return self.focused.sprite
