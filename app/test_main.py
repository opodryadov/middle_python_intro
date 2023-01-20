import pytest
from main import greetings


@pytest.mark.parametrize(
    'name,expected',
    [('Никита', 'Привет, Никита'), ('Ольга', 'Привет, Ольга')],
)
def test_greeting(name: str, expected: str):
    """Текст приветствия зависит от имени."""
    assert greetings(name) == expected


def test_capitalize():
    """Все слова в имени начинаются с большой буквы."""
    name = 'яндекс практикум'
    assert greetings(name) == 'Привет, Яндекс Практикум'
