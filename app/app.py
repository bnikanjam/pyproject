"""
"""
from devutls.debug import trace


class AppBase:

    # Entry point to the whole application
    @staticmethod
    @trace
    def run():
        raise Exception("Not Implemented Yet")
