import pxrd


def test_read_file():
    px = pxrd.read("tests/samples/02001.px")


def test_read_string():
    with open("tests/samples/02001.px", "rt") as f:
        px = pxrd.reads(f.read())