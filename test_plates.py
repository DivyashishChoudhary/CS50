from plates2 import is_valid


def test_is_valid_length():
    assert is_valid("A") == "Invalid"
    assert is_valid("AJSJDJAD") == "Invalid"
    assert is_valid("asassaassada") == "Invalid"
    assert is_valid("ASASAS") == "Valid"


def test_is_valid_numbers():
    assert is_valid("0asas") == "Invalid"
    assert is_valid("WE0000") == "Invalid"
    assert is_valid("RT290") == "Valid"
    assert is_valid("CS50P") == "Invalid"
    assert is_valid("ASAS01") == "Invalid"

def test_is_valid_character():
    assert is_valid("") == "Invalid"
    assert is_valid("@$ADsd") == "Invalid"
    assert is_valid("PI 14") == "Invalid"