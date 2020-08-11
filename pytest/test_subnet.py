import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/')

from netutils.ipaddress import IPaddress
from netutils.ipcalculator import IPcalculator

from ipaddress import IPv4Network, IPv4Address


def test_c24():
    ip_strs = ["192.168.1.1", "192.168.1.24", "192.168.1.131", "192.168.1.36", "192.168.1.75", "192.168.1.80"]

    ips = [IPaddress.from_string(ip) for ip in ip_strs]
    net = IPcalculator.get_net(ips)

    assert str(net) == "192.168.1.0/24"

    # The addresses are really belong to the found network
    ipnet = IPv4Network(net)
    for ip in ip_strs:
        assert IPv4Address(ip) in ipnet



def test_c29():
    ip_strs = ["192.168.29.32", "192.168.29.37", "192.168.29.36"]

    ips = [IPaddress.from_string(ip) for ip in ip_strs]
    net = IPcalculator.get_net(ips)

    assert str(net) == "192.168.29.32/29"


def test_c28():
    ip_strs = ["192.168.28.35", "192.168.28.40", "192.168.28.45"]

    ips = [IPaddress.from_string(ip) for ip in ip_strs]
    net = IPcalculator.get_net(ips)

    assert str(net) == "192.168.28.32/28"


def test_c27():
    ip_strs = ["192.168.27.129", "192.168.27.149"]

    ips = [IPaddress.from_string(ip) for ip in ip_strs]
    net = IPcalculator.get_net(ips)

    assert str(net) == "192.168.27.128/27"


def test_c26():
    ip_strs = ["192.168.26.129", "192.168.26.169"]

    ips = [IPaddress.from_string(ip) for ip in ip_strs]
    net = IPcalculator.get_net(ips)

    assert str(net) == "192.168.26.128/26"


def test_c25():
    ip_strs = ["192.168.25.128", "192.168.25.255"]

    ips = [IPaddress.from_string(ip) for ip in ip_strs]
    net = IPcalculator.get_net(ips)

    assert str(net) == "192.168.25.128/25"


def test_c20():
    ip_strs = ["192.168.20.20", "192.168.30.30"]

    ips = [IPaddress.from_string(ip) for ip in ip_strs]
    net = IPcalculator.get_net(ips)

    assert str(net) == "192.168.16.0/20"


def test_b16():
    ip_strs = ["10.10.1.16", "10.10.255.16"]

    ips = [IPaddress.from_string(ip) for ip in ip_strs]
    net = IPcalculator.get_net(ips)

    assert str(net) == "10.10.0.0/16"


def test_a8():
    ip_strs = ["8.0.1.2", "8.255.3.4"]

    ips = [IPaddress.from_string(ip) for ip in ip_strs]
    net = IPcalculator.get_net(ips)

    assert str(net) == "8.0.0.0/8"


def test_a1():
    ip_strs = ["8.0.1.2", "66.255.3.4"]

    ips = [IPaddress.from_string(ip) for ip in ip_strs]
    net = IPcalculator.get_net(ips)

    assert str(net) == "0.0.0.0/1"


def test_a0():
    ip_strs = ["127.0.1.2", "128.255.3.4"]

    ips = [IPaddress.from_string(ip) for ip in ip_strs]
    net = IPcalculator.get_net(ips)

    assert str(net) == "0.0.0.0/0"


def test_same():
    ip_strs = ["192.168.1.1", "192.168.1.1", "192.168.1.1", "192.168.1.1", "192.168.1.1", "192.168.1.1"]

    ips = [IPaddress.from_string(ip) for ip in ip_strs]
    net = IPcalculator.get_net(ips)

    assert str(net) == "192.168.1.1/32"


def test_singl():
    ip_strs = ["192.168.1.1"]

    ips = [IPaddress.from_string(ip) for ip in ip_strs]
    net = IPcalculator.get_net(ips)

    assert str(net) == "192.168.1.1/32"


def test_empty():
    ip_strs = []

    ips = [IPaddress.from_string(ip) for ip in ip_strs]
    net = IPcalculator.get_net(ips)

    assert net == None


def test_wrong_ip():
    try:
        ip_strs = ["192.333.1.1"]

        ips = [IPaddress.from_string(ip) for ip in ip_strs]
        net = IPcalculator.get_net(ips)
    except Exception as error:
        assert str(error) == "The octet value is invalid: 333"

