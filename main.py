import socket
import mysql.connector

with open("domains.txt", "r") as file:
    domains = file.readlines()

db_config = {
    'host': 'localhost',  
    'user': 'root',
    'password': '1111',
    'database': 'Internet',
    'collation': "utf8mb4_general_ci"
}

def connect_to_db():
    connection = mysql.connector.connect(**db_config)
    return connection


def get_ip(domain):
    ip = socket.gethostbyname(domain)
    return ip


def insert_domain_to_db(domain, ip):
    connection = connect_to_db()
    if connection is None:
        print("MySQL server bilan bog'lanish muammosi!")
        return

    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO Domain (domain, ip) VALUES (%s, %s)", (domain, ip))
    connection.commit()
    print(f"{domain} - {ip} muvaffaqiyatli qo'shildi.")

    cursor.close()
    connection.close()