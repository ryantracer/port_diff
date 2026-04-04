import socket
import subprocess
import ipaddress

def port_scan(ip):
    # escanear portas e adicionar os resultados para um arquivo.
    try:
        with open('ports.txt', 'w') as f:
            f.write(f'[!] Open ports on {ip} [!]')
            s = socket.socket(socket.AF_INET, socket.SOCK_steam)
            for p in range(1, 65535):
                r = s.connect_ex((ip, p))
                if r == 0:
                    f.write(f'=> {p}')
    except Exception as e:
        print(f'[!] {e} [!]')

def check_diff(old_pl, new_pl):
    # comparar scan antigo com novo.
    pass

def mail(changelist):
    # enviar as diferenças para um email.

if __name__ == '__main__':
    port_scan('192.168.0.4')
