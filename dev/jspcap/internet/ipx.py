#!/usr/bin/python3
# -*- coding: utf-8 -*-


# Internetwork Packet Exchange
# Analyser for IPX header


from .internet import Internet
from ..protocols import Info


# IPX Packet Types
TYPE = {
    0 : 'Unknown',
    1 : 'RIP',          # Routing Information Protocol [RFC 1582][RFC 2091]
    2 : 'Echo Packet',
    3 : 'Error Packet',
    4 : 'PEP',          # Packet Exchange Protocol, used for SAP (Service Advertising Protocol)
    5 : 'SPX',          # Sequenced Packet Exchange
    6 : 'NCP',          # NetWare Core Protocol
}


# Socket Types
SOCK = {
    '0001' : 'Routing Information Packet',
    '0002' : 'Echo Protocol Packet',
    '0003' : 'Error Handling Packet',
    '0451' : 'NCP',                         # Netware Core Protocol - used by Novell Netware servers
    '0452' : 'SAP',                         # Service Advertising Protocol
    '0453' : 'RIP',                         # Routing Information Protocol
    '0455' : 'NetBIOS',
    '0456' : 'Diagnostic Packet',
    '0457' : 'Serialization Packet',        # used for NCP as well
    '4003' : 'Novell Netware Client',       # Used by Novell Netware Client
    '8060' : 'IPX',
    '9091' : 'TCP',                         # TCP over IPXF
    '9092' : 'UDP',                         # UDP over IPXF
    '9093' : 'IPXF',                        # IPX Fragmentation Protocol
}


class IPX(Internet):

    __all__ = ['name', 'info', 'length', 'src', 'dst', 'layer', 'protocol']

    ##########################################################################
    # Properties.
    ##########################################################################

    @property
    def name(self):
        return 'Internetwork Packet Exchange'

    @property
    def info(self):
        return self._info

    @property
    def length(self):
        return 30

    @property
    def src(self):
        return self._info.src.addr

    @property
    def dst(self):
        return self._info.dst.addr

    @property
    def layer(self):
        return self.__layer__

    @property
    def protocol(self):
        return self._info.type

    ##########################################################################
    # Data models.
    ##########################################################################

    def __init__(self, _file):
        self._file = _file
        self._info = Info(self.read_ipx())

    def __len__(self):
        return 30

    def __length_hint__(self):
        return 30

    ##########################################################################
    # Utilities.
    ##########################################################################

    def read_ipx(self):
        """Read Internetwork Packet Exchange.

        Structure of IPX header [RFC 1132]:
            Octets          Bits          Name                Discription
              0              0          ipx.cksum        Checksum
              2              16         ipx.len          Packet Length (header includes)
              4              32         ipx.count        Transport Control (hop count)
              5              40         ipx.type         Packet Type
              6              48         ipx.dst          Destination Address
              18             144        ipx.src          Source Address

        """
        _csum = self._read_fileng(2)
        _tlen = self._read_unpack(2)
        _ctrl = self._read_unpack(1)
        _type = self._read_unpack(1)
        _dsta = self._read_ipx_address()
        _srca = self._read_ipx_address()

        ipx = dict(
            chksum = _csum,
            len = _tlen,
            count = _ctrl,
            type = TYPE.get(_type),
            dst = _dsta,
            src = _srca,
        )

        return ipx

    def _read_ipx_address(self):
        """Read IPX address field.

        Structure of IPX address:
            Octets          Bits          Name                Discription
              0              0          ipx.addr.network Network Number
              4              32         ipx.addr.node    Node Number
              10             80         ipx.addr.socket  Socket Number

        """
        # Adress Number
        _byte = self._read_fileng(4)
        _ntwk = ':'.join(textwrap.wrap(_byte.hex(), 2))

        # Node Number (MAC)
        _byte = self._read_fileng(6)
        _node = ':'.join(textwrap.wrap(_byte.hex(), 2))
        _maca = '-'.join(textwrap.wrap(_byte.hex(), 2))

        # Socket Number
        _sock = self._read_fileng(2)

        # Whole Address
        _list = [_ntwk, _node, _sock.hex()]
        _addr = ':'.join(_list)

        addr = dict(
            network = _ntwk,
            node = _maca,
            socket = SOCK.get(_sock.hex()) or _sock,
            addr = _addr,
        )

        return addr
