from logging import log
from abc import ABC, abstractmethod

import pygame


class Scene(ABC):

    """A primitive scene type

    Scenes are objects that contain game "scenes", such as levels.
    Scenes handle the logic and drawing of the objects within them.

    To be used to extend new scenes that overwrite it's methods.
    
    Attributes
    ----------
        sprite_groups: dict[str, pygame.sprite.AbstractGroup]
            A container for sprite groups."""

    def __init__(self) -> None:

        self.sprite_groups = {}

    def create_group(self, name: str, group_type: type[pygame.sprite.AbstractGroup]):

        """Method to create a sprite group and add it to self.sprite_groups.

        Parameters
        ----------
            name: str
                The name of the sprite group. Used as a key for access.

            group_type: type[pygame.sprite.AbstractGroup]
                The type of sprite group you want it to be."""

        self.sprite_groups[name] = group_type()

    @abstractmethod
    def update(self, event_list: list) -> None:

        """Method to manage scene behaviour.

        Designed to be used to update the scene behaviour and handle events.

        Parameters
        ----------
        event_list : list
            An event list that is passed down for event handling."""

    @abstractmethod
    def draw(self, window: pygame.surface.Surface):

        """ to render the scene.

        Parameters
        -------
        window : pygame.surface.Surface
            The window surface to be drawn on.
        """
