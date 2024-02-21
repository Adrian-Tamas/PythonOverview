import pytest

from assertpy import assert_that


def test_example():
    assert 1 + 1 == 2


@pytest.fixture(params=[1, 2, 3, 4, 5])
def input_data(request):
    print("Get value")
    yield request.param
    print("Do cleanup")


def test_with_fixture(input_data):
    squared_value = input_data ** 2
    assert_that(squared_value).is_equal_to(1)

