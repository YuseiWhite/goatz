#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pywebio.platform.tornado import start_server
from pywebio.session import hold

from game_app.controller.apps import StartGame


def main():
    app = StartGame()
    app.start_game()
    start_server(main, port=8000)
    hold()


if __name__ == '__main__':
    main()