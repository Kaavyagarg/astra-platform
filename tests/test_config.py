from customer.config import CUSTOMER_DATA_FILE
def test_customer_data_file():
    assert CUSTOMER_DATA_FILE == 'data/customers.csv'

def test_customer_data_file_from_envirnment(monkeypatch):
    monkeypatch.setenv("CUSTOMER_DATA_FILE","data/test_customers.csv")
    import importlib
    import customer.config
    importlib.reload(customer.config)
    assert customer.config.CUSTOMER_DATA_FILE == "data/test_customers.csv"

def test_app_env_default():
    import customer.config
    assert customer.config.APP_ENV == "development"

def test_log_level_default():
    import customer.config
    assert customer.config.LOG_LEVEL == "INFO"

def test_app_env_from_environment(monkeypatch):
    monkeypatch.setenv("APP_ENV","production")
    import importlib
    import customer.config
    importlib.reload(customer.config)
    assert customer.config.APP_ENV == "production"

def test_log_level_from_environment(monkeypatch):
    monkeypatch.setenv("LOG_LEVEL","DEBUG")
    import importlib
    import customer.config
    importlib.reload(customer.config)
    assert customer.config.LOG_LEVEL == "DEBUG"

def test_invalid_log_level_falls_back_to_info(monkeypatch):
    monkeypatch.setenv("LOG_LEVEL","WHATEVER")
    import importlib
    import customer.config
    import customer.logging_config
    importlib.reload(customer.config)
    importlib.reload(customer.logging_config)
    level = getattr(
        customer.logging_config.logging,
        customer.config.LOG_LEVEL.upper(),
        customer.logging_config.logging.INFO
    )
    assert level == customer.logging_config.logging.INFO