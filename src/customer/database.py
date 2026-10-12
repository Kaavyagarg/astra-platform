import sqlite3


def create_connection(path):
    return sqlite3.connect(path)


def create_customers_table(connection):
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            city TEXT,
            age INTEGER
        )
        """
    )
    connection.commit()


def insert_customer(connection, customer):
    connection.execute(
        """
        INSERT INTO customers (name, city, age)
        VALUES (?, ?, ?)
        """,
        (
            customer["name"],
            customer["city"],
            customer["age"],
        ),
    )
    connection.commit()


def get_customers(connection):
    connection.row_factory = sqlite3.Row

    cursor = connection.execute(
        "SELECT id, name, city, age FROM customers"
    )

    return [dict(row) for row in cursor.fetchall()]


def save_customer(connection, customer):
    connection.execute(
        """
        INSERT INTO customers (name, city, age)
        VALUES (?, ?, ?)
        """,
        (
            customer["name"],
            customer["city"],
            customer["age"],
        ),
    )
    connection.commit()

def get_adult_customers_by_min_age(connection,min_age):
    connection.row_factory = sqlite3.Row
    cursor = connection.execute(
        """
        Select id, name,city, age
        from customers
        where age >= ?
        """,
        (min_age,)
    )
    return [dict(row) for row in cursor.fetchall()]

def update_customer_city(connection,name,city):
    connection.execute("""
    UPDATE customers
    SET city =?
    WHERE name =?""",
        (city,name),)
    connection.commit()

def delete_customer(connection,name):
    connection.execute(
        """DELETE FROM customers
        WHERE name =?""",
        (name,)
    )
    connection.commit()
    