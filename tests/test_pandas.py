import pxrd
from pxrd.convert import to_pandas
import pandas as pd
import pytest


@pytest.fixture
def px_with_languages():
    return pxrd.read("tests/samples/PX_112311_cindus_ind01.px")

def test_convert(px_with_languages):
    df = to_pandas(px_with_languages)
    assert isinstance(df, pd.DataFrame)
