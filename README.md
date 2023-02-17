# Minesweeper

<p>
<a href="https://github.com/Anthony-de-cruz/Minesweeper/blob/main/LICENSE"><img alt="Code style: black" src="https://img.shields.io/badge/license-MIT-9F2B68"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000"></a>
</p>

Python 3.10, Pygame 2.1.2

Systems to implement:

- Dedicated input handler

        - Review
        - Implement

- Dedicated event handler

        - Review
        - Implement

- Particle system

---
## UML Class Diagram (unfinished)

```mermaid
classDiagram

class Game {
        SceneHandler scene_handler
        AudioHandler audio_handler
        InputHandler input_handler
        EventHandler event_handler

        Game()

        mainloop()
}


class PygameLibrary {
        ...
}

class Sprite {
        ...
}

PygameLibrary -- Sprite

class SpriteGroup {
        ...
}

PygameLibrary -- SpriteGroup

class SceneHandler {
        Scene[] scenes
        Scene[] focused_scene

        SceneHandler()

        create_scene()
        remove_scene()
        set_focus()
        update_focus()
        render_focus()
        get_focused()
}

Game *-- SceneHandler : 1
Scene o-- SceneHandler : *

class AudioHandler {

        int volume

        AudioHandler()

        play(Sound)
}

Game *-- AudioHandler : 1
PygameLibrary -- AudioHandler

class InputHandler {
        
        InputHandler(Device)

        handle_inputs()
}

Game *-- InputHandler : 1
PygameLibrary -- InputHandler

class EventHandler {

        Event[] events

        EventHandler()

        handle_events()
}

PygameLibrary -- EventHandler

Game *-- EventHandler : 1

class Scene {
        pygame.Image image
        pygame.Rect rect
        int width
        int height
        pygame.sprite.AbstractGroup[] sprite_groups

        Scene(AudioHandler, InputHandler)

        create_group()
        update()
        render()
}

SpriteGroup o-- Scene : *
AudioHandler <.. Scene : 1
InputHandler <.. Scene : 1


class GameObject {

        pygame.Image image
        pygame.Rect rect

        GameObject(pygame.Sprite.Group *groups)

        update()
        render()
}

Sprite <|-- GameObject
Scene o-- GameObject : *

```