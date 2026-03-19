from app import *

def test_is_adjective():
    assert is_adjective("Nice") == True

def test_contains_illegal_characters():
    assert contains_illegal_characters(".") == True
    assert contains_illegal_characters("Mathias") == False