import socketserver
from peewee import *


class TaskListener(socketserver.BaseRequestHandler):
    """
        Класс обработчика запросов для нашего сервера.

        Он создается один раз для подключения к серверу и должен
        переопределить метод handle () для реализации связи с
        клиентом.
        """

    def handle(self):
        # self.request это TCP сокет присоедененный к клиенту
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # возвращает клиенту данные в верхнем регистре
        self.request.sendall(self.data.upper())


class AppServer(socketserver.TCPServer):
    # зашил сокет в своем классе, хз зачем (чувствую так надо)
    def __init__(self):
        self.server_address = ('localhost', 55555)
        self.RequestHandlerClass = TaskListener
        super().__init__(self.server_address, self.RequestHandlerClass)


class SelectDB(Proxy):
    def __init__(self, db_type):
        super().__init__()
        self.db_type = db_type
        self.database = self._selection()
        self.initialize(self.database)

    def _selection(self):
        # определяем с какой базой данных будем работать
        # по дефолту -  SQLite в памяти
        database = SqliteDatabase(':memory:')

        if self.db_type == 'PostgreSQL':
            database = PostgresqlDatabase('main')
        elif self.db_type == 'MySQL':
            database = MySQLDatabase('main')
        elif self.db_type == 'SQLite':
            database = SqliteDatabase('main')
        return database




class SaverToBase(Model):
    pass


class TaskManager:
    pass


if __name__ == '__main__':
    # Создает сервер.  HOST и PORT вшиты
    with AppServer() as server:
        # Запускает сервер до тех пор
        # пока не прервем нажатием Ctrl+C
        print('Сервер запущен')
        server.serve_forever()
