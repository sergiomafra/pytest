from pytest import fixture


@fixture
def this_is_available_everywhere():
    x = 44
    return x
