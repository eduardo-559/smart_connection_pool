import threading
import queue
from src.database_connection import DatabaseConnection

class ConnectionPool:
    """ Gerencia um conjunto limitado de conexões """
    
    def __init__(self, max_connections=3):
        self.pool = queue.Queue(max_connections)
        for i in range(max_connections):
            self.pool.put(DatabaseConnection(i + 1))
        self.lock = threading.Lock()

    def get_connection(self):
        with self.lock:
            if self.pool.empty():
                print("Nenhuma conexão disponível. Aguardando...")
            conn = self.pool.get()
            print(f"[Pool] Conexão {conn.conn_id} fornecida")
            return conn

    def release_connection(self, conn):
        with self.lock:
            self.pool.put(conn)
            print(f"[Pool] Conexão {conn.conn_id} devolvida ao pool")
