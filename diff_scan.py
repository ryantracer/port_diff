import socket, threading
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--IP', help='IP address to scan for ports')
args = parser.parse_args()

def port_scan(ip, port):
    with open('open_ports.txt', 'a') as f:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            r = s.connect_ex((ip, port))
            if r == 0:
                print(f'{port} OPEN')
                f.write(f'=>{port}\n')
            s.close()
        except socket.error:
            print(f'{port} ERROR')

def check_diff(old_pl, new_pl):
    pass

def mail(changelist):
    pass

if __name__ == '__main__':
    target_ip = args.IP
    try:
        threads = []
        for port in range(1, 65536):
            thread = threading.Thread(target=port_scan, args=(target_ip, port))
            threads.append(thread)
            thread.start()

            if len(threads) >= 200:
                for thread in threads:
                    thread.join()
                    threads = []

        for thread in threads:
            thread.join()
    except Exception as e:
        print('[!] Error/Finished [!]\n {e}')
