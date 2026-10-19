import pytest

from flood_lens.cli import main


@pytest.mark.parametrize("location", ["Belfast", "London"])
def test_location(location, capsys):
    main(["--location", location])

    assert capsys.readouterr().out == (f"Checking flood risk for {location}\n")


def test_missing_location():
    with pytest.raises(SystemExit) as error:
        main([])

    assert error.value.code == 2
