# -*- coding: utf-8 -*-

from GUI.constants import DEFAULT_FOLDER, DEFAULT_EXTENTION, SOUND_FOLDER, MUSICS, SOUNDS
from GUI.__init import *

class Sounds:
    def __init__(self, path, musics=MUSICS, sounds=SOUNDS) -> None:
        self.not_load_musics = musics
        self.not_load_sounds = sounds
        self.audio = {}
        self.audio["sounds"] = {}
        self.audio["musics"] = {}
        self.init_audio(path)
        self.load_not_found()
    
    def init_audio(self, path) -> None:
        for file in pathlib.Path(path).iterdir():
            if file.is_dir():
                self.init_audio(file)
            else:
                name = os.path.splitext(file.name)[0]
                self.load_audio(name, file)
        

    def load_not_found(self) -> None:
        for sound in self.not_load_sounds + self.not_load_musics:
            name = os.path.splitext(pathlib.Path(sound).name)[0]
            print("/!\ fichier \"{}\" manquant ou introuvable.".format(name))
            path = SOUND_FOLDER + DEFAULT_FOLDER + sound + DEFAULT_EXTENTION
            self.load_audio(name, path)

    def load_audio(self, name, path) -> None:
        m = [name in i for i in self.not_load_musics]
        s = [name in i for i in self.not_load_sounds]
        is_music = any(m)
        is_sound = any(s)
        if is_music: 
            self.audio["musics"][name] = os.path.normpath(path)
            del self.not_load_musics[m.index(True)]
        if is_sound: 
            self.audio["sounds"][name] = pygame.mixer.Sound(path)
            del self.not_load_sounds[s.index(True)]
    
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
    
    @staticmethod
    def set_volum_music(volum) -> None:
        pygame.mixer.music.set_volume(volum)
    
    @staticmethod
    def stop_music() -> None:
        pygame.mixer.music.stop()

if __name__ == "__main__":
    Sounds("data/sound/" + DEFAULT_FOLDER)