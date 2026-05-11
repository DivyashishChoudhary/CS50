import pytest
from fuel2 import convert, gauge

def test_convert_valid():
    assert convert("1/4")== 25
    assert convert("3/4")== 75
    assert convert("1/3")== 33
    assert convert("2/3")==67
    assert convert("0/5")== 0
    assert convert("5/5")==100

def test_convert_not_integer():
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ValueError):
        convert("1.5/4")
def test_convert_x_greater_y():
    with pytest.raises(ValueError):
        convert("4/2")

def test_convert_y_0():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    


def test_gauge_empty():
    assert gauge(0) =="E"
    assert gauge(1) =="E"

def test_guage_full():
    assert gauge(99)=="F"
    assert gauge(100)=="F"

def test_guage_middle():
    assert gauge(50)=="50%"
    assert gauge(2)=="2%"
    assert gauge(97)=="97%"
