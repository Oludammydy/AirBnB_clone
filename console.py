#!/usr/bin/env python3
"""
Program entry.
"""
import cmd
import sys
# from turtle import *


class HbnbShell(cmd.Cmd):
    intro = 'Welcome to the hbnb shell.   Type help or ? to list commands.\n'
    prompt = '(hbnb) '
    file = None

    # ----- basic hbnb commands -----
    def do_EOF(self, arg):
        """Exit console"""
        return True

    def do_quit(self, arg):
        """Exit Hbnb shell"""
        print('Thank you for using Hbnb shell')
        self.close()
        return True

    # ----- record and playback -----

    def close(self):
        if self.file:
            self.file.close()
            self.file = None


if __name__ == '__main__':
    HbnbShell().cmdloop()
