import threading
import random
from src.connection_pool import ConnectionPool

def process_order(pool, order_id):
    """ Simula o processamento de um pedido no e-commerce """
    conn = pool.get_connection()
    print(f"[Pedido {order_id}] Processando...")
    conn.execute_query(f"UPDATE orders SET status='completed' WHERE order_id={order_id}")
    pool.release_connection(conn)
    print(f"[Pedido {order_id}] Finalizado.")

if __name__ == "__main__":
    pool = ConnectionPool(max_connections=3)

    threads = []
    for i in range(6):
        t = threading.Thread(target=process_order, args=(pool, random.randint(1000, 9999)))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print("🛒 Todos os pedidos foram processados!")
