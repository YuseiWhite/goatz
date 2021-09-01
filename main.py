#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pywebio.platform.tornado import start_server
from pywebio.session import hold

from game_app.controller.apps import StartGame


def main():
    app = StartGame()
    more_game = app.start_game()

    while more_game:
        more_game = app.start_game()


if __name__ == '__main__':
    start_server(main, port=9200)