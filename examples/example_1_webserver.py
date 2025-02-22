import threading
import time
from src.connection_pool import ConnectionPool

def handle_request(pool, request_id):
    """ Simula uma requisição ao servidor acessando o banco """
    conn = pool.get_connection()
    print(f"[Requisição {request_id}] Obtendo conexão...")
    conn.execute_query(f"SELECT * FROM users WHERE id={request_id}")
    time.sleep(2) 
    pool.release_connection(conn)
    print(f"[Requisição {request_id}] Conexão liberada.")

if __name__ == "__main__":
    pool = ConnectionPool(max_connections=3)
    
    threads = []
    for i in range(5):  
        t = threading.Thread(target=handle_request, args=(pool, i))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print("Todas as requisições foram processadas!")
