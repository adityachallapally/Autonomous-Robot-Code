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


class PID(object):
    """
    A simple PID controller class
    """

    def __init__(self, kP, kI, kD, target):
        self._kP, self._kI, self._kD = kP, kI, kD
        self._target = target

        self._total_error = 0
        self._last_error = 0

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        self._target = value
        self._last_error = 0
        self._total_error = 0

    @property
    def kP(self):
        return self._kP

    @kP.setter
    def kP(self, value):
        self._kP = value

    @property
    def kI(self):
        return self._kI

    @kI.setter
    def kI(self, value):
        self._kI = value

    @property
    def kD(self):
        return self._kD

    @property.setter
    def kD(self, value):
        self._kD = value

    def update(self, current):
        """

        :param current: Current value
        :return: A PID adjusted value
        """

        error = self._target - current
        delta_error = self._last_error - error

        self._total_error += error
        self._last_error = error

        return  self._kP*error + self._kI*self._total_error+self._kD*delta_error


