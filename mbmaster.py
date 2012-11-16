#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" ModBus Master. """
import dpkt
import mberrors

__author__ = 'Anthony GELIBERT'
__version__ = '1.0.0'


class ModBusMaster(dpkt.Packet):
    """ ModBus MASTER packets. """

    __hdr__ = (('func', 'B', 0),)

    class ReadCoils(dpkt.Packet):
        """ FC 1 """

        __hdr__ = (('ref', 'H', 0), ('count', 'H', 0))

    class ReadInputDiscretes(dpkt.Packet):
        """ FC 2  """

        __hdr__ = (('ref', 'H', 0), ('count', 'H', 0))

    class ReadMultipleRegs(dpkt.Packet):
        """ FC 3 """

        __hdr__ = (('ref', 'H', 0), ('count', 'H', 0))

    class WriteMultipleRegisters(dpkt.Packet):
        """ FC 10 """

        __hdr__ = (('ref', 'H', 0), ('count', 'H', 0), ('byte', 'H', 0))

    class ReadCoilsException(dpkt.Packet):
        """ FC 81 """

        __hdr__ = (('code', 'B', 0),)

    class ReadInputDiscretesException(dpkt.Packet):
        """ FC 82 """

        __hdr__ = (('code', 'B', 0),)

    class ReadException(dpkt.Packet):
        """ FC 83 """

        __hdr__ = (('code', 'B', 0),)

    class WriteException(dpkt.Packet):
        """ FC 90 """

        __hdr__ = (('code', 'B', 0),)

    _typesw = {01: ReadCoils,
               02: ReadInputDiscretes,
               03: ReadMultipleRegs,
               10: WriteMultipleRegisters,
               81: ReadCoilsException,
               82: ReadInputDiscretesException,
               83: ReadException,
               90: WriteException}

    def unpack(self, buf):
        dpkt.Packet.unpack(self, buf)
        try:
            self.data = self._typesw[self.func](self.data)
            setattr(self, self.data.__class__.__name__.lower(), self.data)
        except (KeyError, dpkt.UnpackError):
            raise mberrors.UnknownModBusFunctionError(buf, self.func)
