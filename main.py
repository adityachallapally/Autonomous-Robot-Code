# -*- coding: utf-8 -*-

# The MIT License (MIT)
#
# Copyright (c) 2015 Björn Larsson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import time
import signal
import logging
import optparse

from robot.ui import display
from robot.ui import menu
from robot.utils import config
from robot.control import controller
from robot.application import App

class DebugMenu(menu.MenuEntry):
    def Display(self):
        return "Debug"

class DebugLog(menu.MenuEntry):
    def Display(self):
        return "Log Level"

class FrameDisplay(menu.MenuEntry):
    def __init__(self, fps):
        self._fps = fps

    def Display(self):
        return "Frame Time\n{0:4.2} ms".format(self._fps.duration*1000)

class RobotMenu(menu.MenuEntry):
    def Display(self):
        return "Root"

def main(args):
    app = App()

    app.setup(args)
    app.run()
    app.purge()

    return None

if __name__=='__main__':
    sys.exit(main(sys.argv))