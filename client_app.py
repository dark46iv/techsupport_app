import socket
import sys

HOST, PORT = "localhost", 55555
# data = " ".join(sys.argv[1:])  # данные передаются из первого(и единственного) аргумента при запуске с консоли
data = 'kreved'

if __name__ == '__main__':
    # Создает сокет (SOCK_STREAM означает TCP сокет)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Соединяется с сервером и отсылает данные(data)
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data + "\n", "utf-8"))

        # Получает данные с сервера и отключается
        received = str(sock.recv(1024), "utf-8")

    print("Sent:     {}".format(data))
    print("Received: {}".format(received))

