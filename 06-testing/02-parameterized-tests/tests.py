import pytest
from parentheses import matching_parentheses

@pytest.mark.parametrize('string', [
    '',
    '()'
    '()(())',
    '()((()))()'
])

def test_matching_parentheses(string):
    actual = matching_parentheses(string)
    assert actual == True, f'{string} contains no invalid parentheses'



@pytest.mark.parametrize('string', [
    ')',
    '(',
    ')(',
    '()(())(',
    '()(()))'
])

def test_invalid_parentheses(string):
    actual = matching_parentheses(string)
    assert actual == False, f'{string} contains invalid parentheses'