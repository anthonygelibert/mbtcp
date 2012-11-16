#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" MBTCP errors. """
__author__ = 'Anthony GELIBERT'
__version__ = '1.0.0'

class UnknownModBusFunctionError(Exception):
    """ Exception for Unknown ModBus Function code. """

    def __init__(self, packet, function):
        self.packet = packet
        self.function = function

    def __str__(self):
        return "Unknown ModBus Function \""\
               + str(self.function) + "\" in the packet: " + repr(self.packet)
