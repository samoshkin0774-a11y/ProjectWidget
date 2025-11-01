def pytest_configure(config):
    """Конфигурация pytest"""
    config.addinivalue_line(
        "markers", "slow: маркировка медленных тестов"
    )
