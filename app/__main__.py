from rich.traceback import install

from .app import AppBase

"""
Install `rich` as the default traceback handler,
so that all uncaught exceptions will be rendered with highlighting.
"""
install()

if __name__ == "__main__":
    AppBase.run()
