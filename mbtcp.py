#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" ModBus/TCP. """
import dpkt

__author__ = 'Anthony GELIBERT'
__version__ = '1.0.0'


class ModBusTCP(dpkt.Packet):
    """ ModBus/TCP packets. """

    __hdr__ = (('id', 'H', 0),
               ('proto', 'H', 0),
               ('len', 'H', 0),
               ('ui', 'B', 0))

    def unpack(self, buf):
        dpkt.Packet.unpack(self, buf)
