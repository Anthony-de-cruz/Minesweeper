class SceneHandler:

    def __init__(self):

        self.scenes = {}
    
    def create_scene(self, name: str, scene_type: str):

        if self.scenes.__contains__(name):
            raise ValueError("Scene already exists")
        
        else:
            self.scenes[name] = scene_type

    def remove_scene(self, name: str):

        """Removes a scene from the set, throws ValueError """

        if self.scenes.__contains__(name):
            self.scenes.pop(name)
        
        else:
            raise ValueError("Not a valid scene name")
