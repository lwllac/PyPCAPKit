#!/usr/bin/python3
# -*- coding: utf-8 -*-


# Internet Protocol version 6
# Analyser for IPv6 header


from .ip import IP
from ..protocol import Info


# IPv6 Extension Header Types
EXT_HDR = (
    'HOPOPT',       # IPv6 Hop-by-Hop Option
    'IPv6-Route',   # Routing Header for IPv6
    'IPv6-Frag',    # Fragment Header for IPv6
    'ESP',          # Encapsulating Security Payload
    'AH',           # Authentication Header
    'IPv6-NoNxt',   # No Next Header for IPv6
    'IPv6-Opts',    # Destination Options for IPv6 (before routing / upper-layer header)
    'Mobility',     # Mobility Extension Header for IPv6 (currently without upper-layer header)
    'HIP',          # Host Identity Protocol
    'Shim6',        # Site Multihoming by IPv6 Intermediation
)

class IPv6(IP):

    ##########################################################################
    # Properties.
    ##########################################################################

    @property
    def name(self):
        return 'Internet Protocol version 6'

    @property
    def length(self):
        return self._info.len

    @property
    def protocol(self):
        return self._info.next

    ##########################################################################
    # Data models.
    ##########################################################################

    def __init__(self, _file):
        self._file = _file
        self._info = Info(self.read_ipv6())

    def __len__(self):
        return self._info.len

    def __length_hint__(self):
        return 40

    ##########################################################################
    # Utilities.
    ##########################################################################

    def read_ipv6(self):
        """Read Internet Protocol version 6 (IPv6).

        Structure of IPv6 header [RFC 2460]:

             0                   1                   2                   3
            0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
           +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
           |Version| Traffic Class |           Flow Label                  |
           +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
           |         Payload Length        |  Next Header  |   Hop Limit   |
           +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
           |                                                               |
           +                                                               +
           |                                                               |
           +                         Source Address                        +
           |                                                               |
           +                                                               +
           |                                                               |
           +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
           |                                                               |
           +                                                               +
           |                                                               |
           +                      Destination Address                      +
           |                                                               |
           +                                                               +
           |                                                               |
           +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

            Octets          Bits          Name                Discription
              0              0          ip.version        Version (6)
              0              4          ip.class          Traffic Class
              1              12         ip.label          Flow Label
              4              32         ip.len            Payload Length
              6              48         ip.next           Next Header
              7              56         ip.limit          Hop Limit
              8              64         ip.src            Source Address
              24             192        ip.dst            Destination Address

        """
        _htet = self._read_ip_hextet()
        _plen = self._read_unpack(2)
        _next = self._read_protos(1)
        _hlmt = self._read_unpack(1)
        _srca = self._read_ip_addr()
        _dsta = self._read_ip_addr()

        ipv6 = dict(
            version = _htet[0],
            tclass = _htet[1],
            label = _htet[2],
            len = _plen,
            next = _next,
            limit = _hlmt,
            src = _srca,
            dst = _dsta,
        )

        return self._read_next_layer(ipv6, _next)

    def _read_ip_hextet(self):
        _htet = self._read_fileng(4).hex()
        _vers = _htet[0]                    # version number (6)
        _tcls = int(_htet[0:2], base=16)    # traffic class
        _flow = int(_htet[2:], base=16)     # flow label

        return (_vers, _tcls, _flow)

    def _read_ip_addr(self):
        adlt = []       # list of IPv6 hexadecimal address
        ctr_ = {}       # counter for consecutive groups of zero value
        ptr_ = 0        # start pointer of consecutive groups of zero value
        last = False    # if last hextet/group is zero value
        ommt = False    # ommitted flag, since IPv6 address can ommit to `::` only once

        for _ in range(8):
            hex_ = self._read_fileng(2).hex().lstrip('0')

            if hex_:    # if hextet is not '', directly append
                adlt.append(hex_)
                last = False
            else:       # if hextet is '', append '0'
                adlt.append('0')
                if last:    # if last hextet is '', ascend counter
                    ctr_[ptr_] += 1
                else:       # if last hextet is not '', record pointer
                    ptr_ = _
                    last = True
                    ctr_[ptr_] = 1

        ptr_ = max(ctr_, key=ctr_.get)  # fetch start pointer with longest zero values
        end_ = ptr_ + ctr_[ptr_]        # calculate end pointer

        if ctr_[ptr_] > 1:      # only ommit if zero values are in a consecutive group
            del adlt[ptr_:end_] # remove zero values

            if ptr_ == 0 and end_ == 8:     # insert `::` if IPv6 unspecified address (::)
                adlt.insert(ptr_, '::')
            elif ptr_ == 0 or end_ == 8:    # insert `:` if zero values are from start or at end
                adlt.insert(ptr_, ':')
            else:                           # insert '' otherwise
                adlt.insert(ptr_, '')

        addr = ':'.join(adlt)
        return addr

    def _read_next_layer(self, dict_, proto=None):
        # recurse if next header is an extensive header
        ext_len = 0
        while proto in EXT_HDR:
            name_ = proto.replace('IPv6-', '').lower()
            next_ = self._import_next_layer(proto)
            dict_[name_] = next_[0]
            proto = next_[0].next
            ext_len += next_[2]

        # record real payload length (all headers exclude)
        hdr_len = 40 + ext_len
        raw_len = dict_['len'] - ext_len
        dict_['hdr_len'] = hdr_len
        dict_['raw_len'] = raw_len

        # keep original data after fragment header
        if proto == 'IPv6-Frag':
            dict_['header'] = self._read_ip_header(hdr_len)
            dict_['raw'] = self._read_fileng(raw_len)

        dict_['proto'] = proto
        return super()._read_next_layer(dict_, proto)
