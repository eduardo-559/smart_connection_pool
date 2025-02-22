import time

class DatabaseConnection:
    """ Representa uma conexão individual com o banco """
    
    def __init__(self, conn_id):
        self.conn_id = conn_id

    def execute_query(self, query):
        print(f"[Conexão {self.conn_id}] Executando consulta: {query}")
        time.sleep(1)

    def close(self):
        print(f"[Conexão {self.conn_id}] Conexão fechada")
