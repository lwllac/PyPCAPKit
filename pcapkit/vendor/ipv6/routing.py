# -*- coding: utf-8 -*-
"""IPv6 Routing Types
========================

This module contains the vendor crawler for **IPv6 Routing Types**,
which is automatically generating :class:`pcapkit.const.ipv6.routing.Routing`.

"""

import csv
import re
import sys

from pcapkit.vendor.default import Vendor

__all__ = ['Routing']


class Routing(Vendor):
    """IPv6 Routing Types"""

    #: Value limit checker.
    FLAG = 'isinstance(value, int) and 0 <= value <= 255'
    #: Link to registry.
    LINK = 'https://www.iana.org/assignments/ipv6-parameters/ipv6-parameters-3.csv'

    def process(self, data: 'list[str]') -> 'tuple[list[str], list[str]]':
        """Process CSV data.

        Args:
            data: CSV data.

        Returns:
            Enumeration fields and missing fields.

        """
        reader = csv.reader(data)
        next(reader)  # header

        enum = []  # type: list[str]
        miss = []  # type: list[str]
        for item in reader:
            long = item[1]
            rfcs = item[2]

            split = long.split(' (')
            if len(split) == 2:
                name = re.sub(r'\[\d+\]', '', split[0]).strip()
                cmmt = f' ({split[1][:-1]})'
            else:
                name, cmmt = re.sub(r'\[\d+\]', '', long).strip(), ''

            temp = []  # type: list[str]
            for rfc in filter(None, re.split(r'\[|\]', rfcs)):
                if 'RFC' in rfc and re.match(r'\d+', rfc[3:]):
                    #temp.append(f'[{rfc[:3]} {rfc[3:]}]')
                    temp.append(f'[:rfc:`{rfc[3:]}`]')
                else:
                    temp.append(f'[{rfc}]'.replace('_', ' '))
            lrfc = f" {''.join(temp)}" if rfcs else ''
            desc = self.wrap_comment(f'{name}{cmmt}{lrfc}')

            try:
                code = int(item[0])
                renm = self.rename(name, code)  # type: ignore[arg-type]

                pres = f"{renm} = {code}"
                sufs = f"#: {desc}"

                #if len(pres) > 74:
                #    sufs = f"\n{' '*80}{sufs}"

                #enum.append(f'{pres.ljust(76)}{sufs}')
                enum.append(f'{sufs}\n    {pres}')
            except ValueError:
                start, stop = item[0].split('-')

                miss.append(f'if {start} <= value <= {stop}:')
                miss.append(f'    #: {desc}')
                miss.append(f"    extend_enum(cls, '{name}_%d' % value, value)")
                miss.append('    return cls(value)')
        return enum, miss


if __name__ == '__main__':
    sys.exit(Routing())
