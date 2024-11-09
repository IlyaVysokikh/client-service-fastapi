import pytest
from faker import Faker


@pytest.fixture(scope='function', autouse=False)
def faker() -> Faker:
    """
    fixture for generating test data
    """
    return Faker(locale="ru_RU")