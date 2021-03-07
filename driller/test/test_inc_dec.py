import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))

from module.test_sample import decrement, increment


def test_increment():
    assert increment(3) == 4


def test_decrement():
    assert decrement((3)) == 2
