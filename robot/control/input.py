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

__all__ = ['input', 'IInput']

class IInput(object):
    @property
    def Name(self):
        raise NotImplementedError("Implement this")

    def update(self):
        raise NotImplementedError("Implement this")


class InputManager(object):
    def __init__(self):
        self._inputs = list()
        self._data = dict()

    def update(self):
        self._data = {x.Name : x.update() for x in self._inputs}

    def add(self, input):
        self._inputs.append(input)

    def __getitem__(self, item):
        return self._data[item]

input = InputManager()