import unittest
from src.connection_pool import ConnectionPool
from src.database_connection import DatabaseConnection

class TestConnectionPool(unittest.TestCase):

    def setUp(self):
        """ Configuração inicial do teste """
        self.pool = ConnectionPool(max_connections=2)

    def test_get_connection(self):
        """ Testa se conseguimos obter conexões do pool """
        conn = self.pool.get_connection()
        self.assertIsInstance(conn, DatabaseConnection)
        self.pool.release_connection(conn)

    def test_release_connection(self):
        """ Testa se conseguimos devolver conexões ao pool """
        conn = self.pool.get_connection()
        self.pool.release_connection(conn)
        self.assertFalse(self.pool.pool.empty())  # O pool não deve estar vazio

    def test_pool_limit(self):
        """ Testa se o pool respeita o limite máximo de conexões """
        conn1 = self.pool.get_connection()
        conn2 = self.pool.get_connection()
        
        with self.assertRaises(Exception):  # Deve bloquear se tentar pegar mais conexões que o limite
            self.pool.get_connection()

        self.pool.release_connection(conn1)
        self.pool.release_connection(conn2)

if __name__ == "__main__":
    unittest.main()
