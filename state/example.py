"""
Task:
    - Build a media player with states like "Playing", "Paused", and "Stopped",
     where each state defines its own behavior for actions like play, pause, or stop.
"""
from abc import ABC, abstractmethod


class MediaState(ABC):
    @abstractmethod
    def play(self, player: 'MediaPlayer'): ...

    @abstractmethod
    def pause(self, player: 'MediaPlayer'): ...

    @abstractmethod
    def stop(self, player: 'MediaPlayer'): ...


class PlayingState(MediaState):
    def play(self, player: 'MediaPlayer'):
        print("Media is already playing.")

    def pause(self, player: 'MediaPlayer'):
        print("Media paused.")
        player.set_state(PausedState())

    def stop(self, player: 'MediaPlayer'):
        print("Media stopped.")
        player.set_state(StoppedState())


class PausedState(MediaState):
    def play(self, player: 'MediaPlayer'):
        print("Media is playing.")
        player.set_state(PlayingState())

    def pause(self, player: 'MediaPlayer'):
        print("Media is already paused.")

    def stop(self, player: 'MediaPlayer'):
        print("Media stopped.")
        player.set_state(StoppedState())


class StoppedState(MediaState):
    def play(self, player: 'MediaPlayer'):
        print("Media is playing.")
        player.set_state(PlayingState())

    def pause(self, player: 'MediaPlayer'):
        print("Cannot pause. Media is already stopped.")

    def stop(self, player: 'MediaPlayer'):
        print("Media is already stopped.")


class MediaPlayer:
    _state = StoppedState()

    def set_state(self, state: MediaState):
        self._state = state

    def play_media(self):
        self._state.play(self)

    def pause_media(self):
        self._state.pause(self)

    def stop_media(self):
        self._state.stop(self)


def main():
    player = MediaPlayer()
    print("Media Player\nType 'play', 'pause', or 'stop' to control the player.")

    while True:
        action = input("> ").strip().lower()
        match action:
            case "play":
                player.play_media()
            case "pause":
                player.pause_media()
            case "stop":
                player.stop_media()
            case "exit":
                print("Exiting media player.")
                break
            case _:
                print("Invalid command. Type 'play', 'pause', 'stop', or 'exit'.")


if __name__ == "__main__":
    main()
