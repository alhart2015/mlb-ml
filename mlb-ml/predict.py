"""
Entry point to predict stuff.
"""
from api import gameday_api_handler

def this_is_a_test():
    return 2

def main():
    this_is_a_test()
    gameday_api_handler.test()


if __name__ == '__main__':
    main()