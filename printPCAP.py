#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Print a PCAP decomposition. """
import  dpkt
import  sys
import time
import mbslave
import mbtcp
import mbmaster
import mberrors

__author__ = 'Anthony GELIBERT'
__version__ = '1.0.0'


def main(prog_args):
    """ Main method """

    for arg in prog_args:
        target = open(arg)
        try:
            pcap = dpkt.pcap.Reader(target)
        except ValueError:
            continue

        print "====== ", arg, " ======"
        try:
            for timestamp, buf in pcap:
                eth = dpkt.ethernet.Ethernet(buf)
                tcp = eth.data.data

                try:
                    if len(tcp.data) > 0 and (tcp.sport == 502 or tcp.dport == 502):
                        modtcp = mbtcp.ModBusTCP(tcp.data)
                        if tcp.dport == 502:
                            text = 'query n°' + str(modtcp.id) + ' to '
                            mb = mbmaster.ModBusMaster(modtcp.data)
                        else:
                            text = 'response n°' + str(modtcp.id) + ' from '
                            mb = mbslave.ModBusSlave(modtcp.data)
                        text += str(modtcp.ui) + ': ' + repr(mb)
                        print time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(timestamp)), ': ', text
                except AttributeError:
                    pass
                except mberrors.UnknownModBusFunctionError as e:
                    print e
        except KeyboardInterrupt:
            pass
        target.close()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
