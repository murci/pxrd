import pxrd
import pytest


@pytest.fixture
def px_with_languages():
    return pxrd.read("tests/samples/PX_112311_cindus_ind01.px")

def test_read_languages(px_with_languages):
    assert px_with_languages.language() in px_with_languages.languages()

def test_keyword_default_language(px_with_languages):
    assert px_with_languages.keyword("TITLE") == px_with_languages.keyword("TITLE", language=px_with_languages.language())