from src.utils import transaction_returner


def test_transaction_returner_empty():
    assert transaction_returner('C:\\Users\\user\\PycharmProjects\\PythonProject1\\data\\empty.json') == []


def test_transaction_returner_not_list():
    assert (transaction_returner('C:\\Users\\user\\PycharmProjects\\PythonProject1\\data\\onedict.json') ==
            [])


def test_transaction_returner_incorrect_path():
    assert (transaction_returner('C:\\Users\\user\\PycharmProjects\\PythonProject1\\data\\somename.json')
            == [])
