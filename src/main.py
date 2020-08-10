import fileinput
from netutils.ipaddress import IPaddress
from netutils.ipcalculator import IPcalculator


def start():
    """
    Reads addresses from standard input
    and returns the smallest common network
    """

    # python main.py < ../samples/C24.ip
    ips = []
    for line in fileinput.input():
        if line in ['\n', '\r\n']:
            break
        ips.append(IPaddress.from_string(line))

    net = IPcalculator.get_net(ips)
    print(net)


if __name__ == "__main__":
    start()
