from importlib.metadata import version

import flood_lens


def test_package_imports():
    assert flood_lens.__name__ == "flood_lens"


def test_package_version():
    assert version("flood-lens") == "0.1.0"
