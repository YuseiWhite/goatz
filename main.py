#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from game_app.controller.apps import StartGame


def main():
    app = StartGame()
    app.start_game()


if __name__ == '__main__':
    main()