import mysql.connector

def db_client():
    try:
        dbname = "alumnat"
        user = "root"
        password = "ARMAN001"
        host = "localhost"
        port = "3306"
        collation = "utf8mb4_general_ci"
        
        return mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=dbname,  
            collation=collation
        )
    
    except Exception as e:
        print(f"Error de conexión: {e}")
