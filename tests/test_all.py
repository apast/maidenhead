import pytest
from pytest import approx

import maidenhead


def test_latlon2maiden(location):
    m = maidenhead.toMaiden(*location.latlon)
    assert m == location.maiden[:6]


def test_maiden2latlon(location):
    lat, lon = maidenhead.toLoc(location.maiden)
    assert lat == approx(location.latlon[0], rel=0.0001)
    assert lon == approx(location.latlon[1], rel=0.0001)


@pytest.mark.parametrize("invalid_str", [None, 1, True, False])
def test_invalid_maiden(invalid_str):
    with pytest.raises(TypeError):
        maidenhead.to_location(maiden=invalid_str)


def test_invalid_maiden_len():
    with pytest.raises(ValueError):
        maidenhead.to_location(maiden="GG52qjjjjj")
