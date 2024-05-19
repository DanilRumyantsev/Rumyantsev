# Приложение ВЫДАЧА КРЕДИТОВ для некоторой организации. БД должна
# содержать таблицу Клиент со следующей структурой записи: ФИО клиента, ФИО
# сотрудника банка, срок кредита, процент кредита, сумма кредита.

import sqlite3

db_file = 'выдача_кредитов.db'

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Credit (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fio_client TEXT NOT NULL,
            fio_employee TEXT NOT NULL,
            prichina TEXT NOT NULL,
            summa REAL NOT NULL
        )
    ''')
    conn.commit()

def insert_data(conn, fio_client, fio_employee, prichina, summa):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Credit (fio_client, fio_employee, prichina, summa)
        VALUES (?, ?, ?, ?)
    """, (fio_client, fio_employee, prichina, summa))
    conn.commit()

def delete_all_data(conn):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Credit")
    conn.commit()

def delete_credit_by_id(conn, credit_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Credit WHERE id=?", (credit_id,))
    conn.commit()

def update_credit_by_id(conn, credit_id, fio_client, fio_employee, prichina, summa):
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Credit SET fio_client=?, fio_employee=?, prichina=?, summa=? WHERE id=?
    """, (fio_client, fio_employee, prichina, summa, credit_id))
    conn.commit()

def fetch_all_credits(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Credit")
    rows = cursor.fetchall()

    print("{:<10} {:<20} {:<20} {:<10} {:<20}".format("ID", "FIO of client", "FIO of employee", "Prichina","Summa"))
    print("-" * 80)

    for row in rows:
        print("{:<10} {:<20} {:<20} {:<10} {:<20}".format(*row))

def main():
    conn = create_connection()
    create_table(conn)

    while True:
        print("-" * 42)
        print('| Выберите действие:', " " * 19, "|")
        print("-" * 42)
        print('| 1. Просмотреть таблицу', " " * 15, "|")
        print("-" * 42)
        print('| 2. Очистить данные', " " * 19, "|")
        print("-" * 42)
        print('| 3. Добавить новую строку', " " * 13, "|")
        print("-" * 42)
        print('| 4. Удалить строку по ID', " " * 14, "|")
        print("-" * 42)
        print('| 5. Изменить строку по ID', " " * 13, "|")
        print("-" * 42)
        print('| 6. Выйти', " " * 29, "|")
        print("-" * 42)

        choice = int(input("Выберите действие: "))

        if choice == 1:
            fetch_all_credits(conn)
        elif choice == 2:
            delete_all_data(conn)
            print("Все данные очищены.")
        elif choice == 3:
            fio_client = input("Введите ФИО клиента: ")
            fio_employee = input("Введите ФИО сотрудника: ")
            prichina = input("Введите причину: ")
            summa = float(input("Введите кол-во денежных средств: "))
            insert_data(conn, fio_client, fio_employee, prichina, summa)
        elif choice == 4:
            credit_id = int(input("Введите ID строки, которую хотите удалить: "))
            delete_credit_by_id(conn, credit_id)
            print(f"Строка №{credit_id} удалена.")
        elif choice == 5:
            credit_id = int(input("Введите ID строки, которую хотите изменить: "))
            fio_client = input("Введите новое ФИО клиента: ")
            fio_employee = input("Введите новое ФИО сотрудника: ")
            prichina = input("Введите новую причину: ")
            summa = float(input("Введите новое кол-во денежных средств: "))
            update_credit_by_id(conn, credit_id, fio_client, fio_employee, prichina, summa)
            print("Credit updated.")
        elif choice == 6:
            break
        else:
            print("Нет такого действия, введите 1, 2, 3, 4, 5 или 6.")

    conn.close()

main()