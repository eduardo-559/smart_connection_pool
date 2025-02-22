import threading
from src.connection_pool import ConnectionPool

def generate_report(pool, report_id):
    """ Simula a geração de um relatório que acessa o banco """
    conn = pool.get_connection()
    print(f"[Relatório {report_id}] Gerando relatório...")
    conn.execute_query(f"SELECT COUNT(*) FROM sales WHERE year=2023")
    pool.release_connection(conn)
    print(f"[Relatório {report_id}] Concluído.")

if __name__ == "__main__":
    pool = ConnectionPool(max_connections=2)

    threads = []
    for i in range(4):
        t = threading.Thread(target=generate_report, args=(pool, i))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print("Todos os relatórios foram gerados!")
