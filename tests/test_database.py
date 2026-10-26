from customer.database import (create_connection,create_customers_table,insert_customer,get_customers, 
save_customer,get_adult_customers_by_min_age,update_customer_city,
delete_customer,save_customers_batch,get_table_schema,add_country_column)
import pytest 
import sqlite3
def test_create_connection(tmp_path):
    path = tmp_path/"astra.db"
    connection = create_connection(path)
    assert connection is not None
    connection.close()

def test_create_customers_table(tmp_path):
    path = tmp_path / "astra.db"
    connection = create_connection(path)
    create_customers_table(connection)
    cursor = connection.execute(
        "SELECT name FROM sqlite_master "
        "WHERE type='table' AND name='customers'"
    )
    result = cursor.fetchone()
    assert result[0] == 'customers'
    connection.close()

def test_insert_customer(tmp_path):
    path = tmp_path / "astra.db"
    connection = create_connection(path) # open database
    create_customers_table(connection)  #create customer table inside that database
    customer = {
        "name":"Alice",
        "city":"Unknown",
        "age":25
    }
    insert_customer(connection, customer)
    cursor = connection.execute(
        "SELECT name,city, age FROM customers"
    )
    result = cursor.fetchone()
    assert result == (
        "Alice",
        "Unknown",
        25
    )
    connection.close()

def test_get_customers(tmp_path):
    path = tmp_path / "astra.db"
    connection = create_connection(path)
    create_customers_table(connection)
    insert_customer(
    connection,
    {
        "name": "Alice",
        "city": "Unknown",
        "age": 25,
    },
)
    insert_customer(
    connection,
    {
        "name": "Bob",
        "city": "Unknown",
        "age": 30,
    },
)
    result = get_customers(connection)
    assert len(result) == 2
    assert result[0]["name"] == 'Alice'
    assert result[0]["age"] == 25
    assert result[1]["name"] == "Bob"
    assert result[1]["age"] == 30
    connection.close()

def test_save_customer(tmp_path):
    path = tmp_path / "astra.db"
    connection = create_connection(path)
    create_customers_table(connection)
    customer = {
    "name": "Charlie",
    "city": "Unknown",
    "age": 28,
    }
    save_customer(connection, customer)
    result = get_customers(connection)
    assert len(result) == 1
    assert result[0]["name"] == "Charlie"
    assert result[0]["city"] == "Unknown"
    assert result[0]["age"] == 28
    connection.close()

def test_get_adult_customers_min_age(tmp_path):
    path = tmp_path/"astra.db"
    connection = create_connection(path)
    create_customers_table(connection)
    insert_customer(
        connection,
        {
            "name":"Alice",
            "city":"unknown",
            "age":25
        },
    )
    insert_customer(
        connection,
        {
            "name":"Bob",
            "city":"Unknown",
            "age":16
        }
    )
    insert_customer(
        connection,
        {
            "name":"Bob",
            "city":"Unkown",
            "age":35
        }
    )
    result = get_adult_customers_by_min_age(connection,30)
    assert len(result) == 1
    assert result[0]["name"] == "Bob"
    connection.close()

def test_update_customer_city(tmp_path):
    path = tmp_path /"astra.db"
    connection = create_connection(path)
    create_customers_table(connection)
    insert_customer(
        connection,
        {
            "name":"Alice",
            "city":"Unknown",
            "age":25
        }
    )
    update_customer_city(
        connection,
        "Alice",
        "Delhi"
    )

def test_delete_customer(tmp_path):
    path = tmp_path/"astra.db"
    connection = create_connection(path)
    create_customers_table(connection)
    insert_customer(
        connection,
        {
            "name":"Alice",
            "city":"Delhi",
            "age":25
        }
    )
    delete_customer(connection,"Alice")
    result = get_customers(connection)
    assert result == []
    connection.close()

def test_save_customers_batch(tmp_path):
    path = tmp_path/"astra.db"
    connection = create_connection(path)
    create_customers_table(connection)
    customers =[
        {"name":"Alice","city":"Delhi","age":25},
        {"name":"Bob","city":"Mumbai","age":17}
    ]
    save_customers_batch(connection,customers)
    result = get_customers(connection)
    assert len(result) == 2
    assert result[0]["name"] == "Alice"
    assert result[1]["name"] == "Bob"
    connection.close()

def test_save_customers_batch_rolls_back_on_error(tmp_path):
    path = tmp_path/"astra.db"
    connection = create_connection(path)
    create_customers_table(connection)
    customers = [
        {"name":"Alice","city":"Delhi","age":25},
        {"name":"Bob","city":"Mumbai"}
    ]
    with pytest.raises(KeyError):
        save_customers_batch(connection,customers)
    assert get_customers(connection) == []
    connection.close()

def test_database_check_constraint(tmp_path):
    connection = sqlite3.connect(tmp_path/'constraints.db')
    connection.execute(
        """Create table test_customers(
        name TEXT NOT NULL,
        age INTEGER CHECK (age >= 0)
        )"""
    )
    with pytest.raises(sqlite3.IntegrityError):
        connection.execute(
            "Insert into test_customers (name,age) values (?,?)",
            ("Alice",-1)
        )

def test_database_not_null_constraint(tmp_path):
    connection = sqlite3.connect(tmp_path/"constraints.db")
    connection.execute(
        """
        Create table test_customers(
        name text not null,
        age integer
        )
        """
    )
    with pytest.raises(sqlite3.IntegrityError):
        connection.execute(
            "Insert into test_customers (name,age) values (?,?)",
            (None,25)
        )
    connection.close()

def test_get_table_schema(tmp_path):
    connection = create_connection(tmp_path/'astra.db')
    create_customers_table(connection)
    schema = get_table_schema(connection,"customers")
    column_names = [column["name"] for column in schema]
    assert column_names == ["id","name","city","age"]
    connection.close()

def test_add_country_column_preserves_data(tmp_path):
    connection = create_connection(tmp_path/'astra.db')
    create_customers_table(connection)
    insert_customer(
        connection,
        {"name":"Alice","city":"Delhi","age":25}
    )
    add_country_column(connection)

    schema = get_table_schema(connection,"customers")
    column_names = [column["name"] for column in schema]
    customers = get_customers(connection)

    assert "country" in column_names
    assert customers[0]["name"] == "Alice"
    assert customers[0]["city"] == "Delhi"
    assert customers[0]["age"] == 25
    row = connection.execute(
        "SELECT country from customers where name = ?",
        ("Alice",)
    ).fetchone()
    assert row[0] is None 

def test_add_country_column_is_safe_to_run_twice(tmp_path):
    connection = create_connection(tmp_path/'astra.db')
    create_customers_table(connection)

    add_country_column(connection)
    add_country_column(connection)

    schema = get_table_schema(connection,"customers")
    column_names = [column["name"] for column in schema]

    assert column_names.count("country") == 1
    connection.close()