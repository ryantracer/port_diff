import socket, threading

def port_scan(ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            r = s.connect_ex((ip, port))
            if r == 0:
                print(f'{port} OPEN')
            s.close()
        except socket.error:
            print(f'{port} ERROR')

def check_diff(old_pl, new_pl):
    # comparar scan antigo com novo.
    pass

def mail(changelist):
    # enviar as diferenças para um email.
    pass

if __name__ == '__main__':
    target_ip = '192.168.0.7'
    try:
        threads = []
        for port in range(1, 65536):
            thread = threading.Thread(target=port_scan, args=(target_ip, port))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
    except Exception as e:
        print('[!] Error/Finished [!]\n {e}')
