"""
Networking UDP
"""
import socket

def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print('server started')
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print(f'Message from: {str(addr)}')
        print(f'from connected user: {data}')
        data = data.upper()
        print(f'Sending: {data}')
        s.sendto(data.encode('utf-8'), addr)
    s.close()


if __name__ == '__main__':
    main()