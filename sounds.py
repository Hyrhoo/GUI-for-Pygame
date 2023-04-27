# -*- coding: utf-8 -*-

from GUI.initialisation import *

class Sounds:
    def __init__(self, path: str, musics: dict, sounds: dict) -> None:
        self.audio = {}
        self.audio["sounds"] = {}
        self.audio["musics"] = {}
        self.__init_musics(path, musics)
        self.__init_sounds(path, sounds)

    def __init_musics(self, path: str, musics: dict):
        for name, music_path in musics.items():
            total_path = path + music_path
            if pathlib.Path(total_path).is_file():
                if not name in self.audio["musics"]:
                    self.audio["musics"] = total_path
                ValueError(f"music named '{name}' already exist")
            ValueError(f"path '{total_path}' not found")

    def __init_sounds(self, path: str, sounds: dict):
        for name, sound_path in sounds.items():
            total_path = path + sound_path
            if pathlib.Path(total_path).is_file():
                if not name in self.audio["sounds"]:
                    self.audio["sounds"] = pygame.mixer.Sound(total_path)
                ValueError(f"sound named '{name}' already exist")
            ValueError(f"path '{total_path}' not found")

    def add_sounds(self, path: str, sounds: dict):
        self.__init_sounds(path, sounds)

    def add_musics(self, path: str, musics: dict):
        self.__init_musics(path, musics)

    def play_music(self, music, repetition=0) -> None:
        pygame.mixer.music.load(self.audio["musics"][music])
        pygame.mixer.music.play(repetition)

    def play_sound(self, sound, repetition=0) -> None:
        self.audio["sounds"][sound].play(repetition)

    def set_volum_sounds(self, volum) -> None:
        for sound in self.audio["sounds"].values():
            sound.set_volume(volum)

    def stop_all_sounds(self) -> None:
        for sound in self.audio["sounds"].values():
            sound.stop()

    def stop_sound(self, name) -> None:
        self.audio["sounds"][name].stop()

    @staticmethod
    def set_volum_music(volum) -> None:
        pygame.mixer.music.set_volume(volum)

    @staticmethod
    def stop_music() -> None:
        pygame.mixer.music.stop()
