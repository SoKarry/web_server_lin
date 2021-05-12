import socket
from datetime import date


def st_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8787))
    server.listen()
    print('Сервер успешно запущен...')
    while True:
        try:
            client_sock, address = server.accept()
            data = client_sock.recv(1024).decode('utf—8')
            content = get_page(data)
            client_sock.send(content)
            client_sock.shutdown(socket.SHUT_RDWR)
        except:
            server.close()
            print('Выключаю сервер')
            break


def get_page(request_data):
    today = date.today()
    path = request_data.split(' ')[1]
    try:
        if path == '/':
            path = "/index.html"
        with open('templates' + path, 'rb') as file:
            response = file.read()
        HDRS = f'HTTP/1.1 200 0K\r\nDate: {today}\r\nContent-Type: text/html; charset=utf-8\r\nServer: Python\r\nContent-length: {len(response)}\r\nConnection: close\r\n\r\n'
        res = HDRS.encode('utf—8') + response
    except FileNotFoundError:
        response = "<H1>This page not found.</H1>"
        HDRS_404 = f'HTTP/1.1 404 0K\r\nDate: {today}\r\nContent-Type: text/html; charset=utf-8\r\nServer: Python\r\nContent-length: {len(response)}\r\nConnection: close\r\n\r\n'
        res = (HDRS_404 + response).encode('utf—8')
    return res


if __name__ == "__main__":
    st_server()
