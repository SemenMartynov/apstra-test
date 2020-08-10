import functools
from typing import Tuple
from netutils.ipaddress import IPaddress, IPmask, IPnet


class IPcalculator:
    """Useful utilities for working with network abstractions.
    """

    @staticmethod
    def minmax(ips: list) -> Tuple[IPaddress, IPaddress]:
        """Finds the minimum and maximum IP address in the list.

        Args:
            ips (list): List with IP addresses.

        Returns:
            Tuple[IPaddress, IPaddress]: the minimum and maximum IP address in the list
        """
        # I'm a big fan of the functional approach,
        # but if the team thinks it makes the code harder to understand,
        # I can write more explicitly.
        if len(ips) < 1:
            return None, None
        return functools.reduce(lambda mem, it: (min(mem[0], it), max(mem[1], it)), ips, (ips[0], ips[0]))

    @staticmethod
    def get_net(ips: list) -> IPnet:
        """Finds the IP subnet for the list of IP addresses.

        Args:
            ips (list): List with IP addresses.

        Returns:
            IPnet: The smallest common subnet.
        """
        if len(ips) < 1:
            return None

        min_ip, max_ip = IPcalculator.minmax(ips)

        mask_octets = min_ip ^ max_ip
        # Classless Inter-Domain Routing
        cidr = 32
        # most significant bit
        msb = 0
        for i in range(4):
            if msb != 0:
                # If we have already found the
                # most significant bit, then
                # all other octets should be 0.
                mask_octets[i] = 0
                continue

            if mask_octets[i] == 0:
                # If we haven't found the most
                # significant bit yet, then the
                # octet should be 255.
                mask_octets[i] = 255
                continue

            while (mask_octets[i] > 0):
                # I can make this more efficient
                # but less readable
                mask_octets[i] = int(mask_octets[i] / 2)
                msb += 1

            # Since we know the most significant
            # bit and the octet number, we can
            # calculate CIDR
            cidr -= msb + (3 - i) * 8
            mask_octets[i] = 256 - (1 << msb)

        mask = IPmask(mask_octets)
        net_octets = min_ip & mask
        net = IPnet(net_octets, cidr)

        return net
