#!/usr/bin/env python
# pong game

import pygame

import config


class Pong:
    def __init__(self):
        self.playing = True
        pygame.display.init()

    def run(self):
        pygame.display.set_mode(config.resolution)
        # display
        while self.playing:
            # events
            # player
            # ai
            # sprites
            # check quit
            self.playing = False

    def __str__(self):
        return str(self.playing)


def main():
    p = Pong()
    p.run()

if __name__ == "__main__":
    main()
