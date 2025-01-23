import os
from unittest.mock import patch

import pandas as pd

from src.file_reader import csv_reader, excel_reader


@patch("csv.DictReader")
def test_csv_reader(mock_datafiles):
    mock_datafiles.return_value = [{"test": "1"}]
    assert (csv_reader(f"{os.path.join(os.path.dirname(__file__), os.pardir)}\\data\\transactions.csv") ==
            [{"test": "1"}])


def test_csv_reader_not_files():
    assert csv_reader(f"{os.path.join(os.path.dirname(__file__), os.pardir)}\\data\\missing.csv") == []


@patch("pandas.read_excel")
def test_excel_reader(mock_datafiles):
    mock_datafiles.return_value = pd.DataFrame({"test": ["1"]})
    assert (excel_reader(f"{os.path.join(os.path.dirname(__file__), os.pardir)}\\data\\transactions_excel.xlsx")
            == [{"test": "1"}])


def test_excel_reader_not_files():
    assert excel_reader(f"{os.path.join(os.path.dirname(__file__), os.pardir)}\\data\\missing.csv") == []
