import socket


def scan(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        print("[O] Port " + str(port) + " opened")
        s.close()
    except:
        pass


def scan_list(target, ports):
    port_list = map(lambda p_s: int(p_s), ports.split(","))
    for p in port_list:
        scan(target, p)


def scan_range(target, n1, n2):
    for p in range(n1, n2):
        scan(target, p)


target = input("Enter Target IP addr: ")
ports = input(
    "Enter ports to scan (separated by comma), or port range(n1-n2): ")
if "-" in ports:
    n1, n2 = ports.split("-")
    scan_range(target, int(n1), int(n2))
else:
    scan_list(target, ports)
