from src.connection_pool import ConnectionPool

class Client:
    """ Simula um cliente que solicita conexões do pool """
    
    def __init__(self, pool):
        self.pool = pool

    def request_connection(self, query):
        connection = self.pool.get_connection()
        connection.execute_query(query)
        self.pool.release_connection(connection)
