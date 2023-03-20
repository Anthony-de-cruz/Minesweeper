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
I suck at UML diagrams so bare with me.

```mermaid
classDiagram

class Game {
        SceneHandler scene_handler
        AudioHandler audio_handler
        InputHandler input_handler
        EventHandler event_handler

        Game()

        fetch_config()
        fetch_events()
        mainloop()
}


class PygameLibrary {
        ...
}

note for PygameLibrary "...refer to the corrosponding\ndocumentation."

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
        update_focus(Event[] event_list)
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

class PlayerData {

        String[] Data

        PlayerData()

        write_data()
        get_data()
}

Game *-- PlayerData : 1

class Scene {
        pygame.Image image
        pygame.Rect rect
        int width
        int height
        pygame.sprite.AbstractGroup[] sprite_groups

        Scene(AudioHandler, InputHandler, PlayerData)

        create_group()
        update(Event[] event_list)
        render()
}

SpriteGroup o-- Scene : *
GameObject o-- Scene : *
AudioHandler <-- Scene : 1
PlayerData <-- Scene : 1

class GameObject {

        pygame.Image image
        pygame.Rect rect

        GameObject(pygame.sprite.Group *groups)

        update()
        render()
}

Sprite <|-- GameObject

class ExampleObject {

        pygame.Vector2 velocity

        ExampleObject(int x, int y, pygame.sprite.Group *groups)

        shoot()
        explode()
}

GameObject <|-- ExampleObject

class SpriteCamera {

        bool dirty
        int[] _offset_vector

        SpriteCamera(pygame.Sprite *sprites, bool dirty)

        move(int x, int y)
        set_offset(int x, int y)
}

SpriteGroup <|-- SpriteCamera

```