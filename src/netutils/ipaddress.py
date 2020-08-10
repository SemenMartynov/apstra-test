class IPaddress:
    """The class represents the IP address and some methods for working with octets.
    """

    def __init__(self, octets: list):
        """Constructing an IP address class based on a list with octets.

        Args:
            octets (list): contains 4 octets of which the IP address consists.

        Raises:
            ValueError: If the wrong number of octets is transmitted.
            ValueError: If the octet value does not fall within the expected range.
        """
        if len(octets) != 4:
            raise ValueError('Incorrect octets number')

        for octet in octets:
            if 0 > octet or octet > 255:
                raise ValueError(f'The octet value is invalid: {octet}')

        self.octets = octets

    @classmethod
    def from_string(cls, address: str):
        """The fabric for build an IP address based on a string.

        Args:
            address (str): A string containing the IP address (4 octets separated by periods)

        Raises:
            ValueError: if the string has an unexpected format.

        Returns:
            IPaddress: IP address
        """
        octets = address.split('.')
        if len(octets) != 4:
            raise ValueError(f'Can\'t get IP address from the string {address}')

        octets = [int(octet) for octet in octets]  # Can rise the exception too!

        return cls(octets)

    @classmethod
    def from_ints(cls, a: int, b: int, c: int, d: int):
        """The fabric for build an IP address based on 4 integers.

        Args:
            a (int): the first octet of the IP adress
            b (int): the second octet of the IP adress
            c (int): the third octet of the IP adress
            d (int): the fourth octet of the IP adress

        Returns:
            IPaddress: IP address
        """
        octets = [a, b, c, d]
        return cls(octets)

    def __str__(self) -> str:
        """String representation of the IP address

        Returns:
            str: string with IP address
        """
        return f'{self.octets[0]}.{self.octets[1]}.{self.octets[2]}.{self.octets[3]}'

    def __gt__(self, other) -> bool:
        """Operator for comparing two IP addresses

        Args:
            other (IPaddress): Another IP address for comparison.

        Returns:
            bool: true if the first IP address is greater than the second IP address.
        """
        if not isinstance(other, IPaddress):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.octets > other.octets

    def __xor__(self, other) -> list:
        """Helper function for determining the shared subnet

        Args:
            other (IPaddress): another IP address to perform the XOR operation.

        Returns:
            list: the result of performing the XOR operation on two IP addresses.
        """
        if not isinstance(other, IPaddress):
            return NotImplemented

        xor = 4 * [None]
        for i in range(4):
            xor[i] = self.octets[i] ^ other.octets[i]

        return xor

    def __and__(self, other) -> list:
        """Helper function for determining the subnet address

        Args:
            other (IPmask): netmask for computing the subnet address.

        Returns:
            list: the result of performing the conjunction operation.
        """
        if not isinstance(other, IPmask):
            return NotImplemented

        bin_and = 4 * [None]
        for i in range(4):
            bin_and[i] = self.octets[i] & other.octets[i]

        return bin_and


class IPmask:
    """The class represents the IP mask.
    """

    def __init__(self, octets: list):
        """Constructing an IP mask class based on a list with octets.

        Args:
            octets (list): contains 4 octets of which the IP mask consists.

        Raises:
            ValueError: If the wrong number of octets is transmitted.
            ValueError: If the octet value does not fall within the expected range.
        """
        if len(octets) != 4:
            raise ValueError('Incorrect octets number')

        for octet in octets:
            if 0 > octet or octet > 255:
                raise ValueError(f'The octet value is invalid: {octet}')

        self.octets = octets

    def __str__(self) -> str:
        """String representation of the IP mask.

        Returns:
            str: string with the IP mask.
        """
        return f'{self.octets[0]}.{self.octets[1]}.{self.octets[2]}.{self.octets[3]}'


class IPnet:
    """The class represents the IP subnet.
    """

    def __init__(self, octets: list, cidr: int):
        """Constructing an IP net class based on a list of octets and CIDR.

        Args:
            octets (list): [description]
            cidr (int): [description]

        Raises:
            ValueError: If the wrong number of octets is transmitted.
            ValueError: If the octet value does not fall within the expected range.
            ValueError: If the CIDR is ouf of the expected range.
        """
        if len(octets) != 4:
            raise ValueError('Incorrect octets number')

        for octet in octets:
            if 0 > octet or octet > 255:
                raise ValueError(f'The octet value is invalid: {octet}')

        if 0 > cidr or cidr > 32:
            raise ValueError(f'The CIDR value is invalid: {cidr}')

        self.octets = octets
        self.cidr = cidr

    def __str__(self) -> str:
        """String representation of the IP subnet.

        Returns:
            str: string with the IP subnet.
        """
        return f'{self.octets[0]}.{self.octets[1]}.{self.octets[2]}.{self.octets[3]}/{self.cidr}'
