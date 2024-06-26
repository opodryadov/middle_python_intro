"""Генератор приветствий."""


def greetings(name: str) -> str:
    """Возвращает текст приветствия.

    Args:
        name: Имя пользователя

    Returns:
        str: Текст приветствия
    """
    return 'Привет, {0}'.format(name.title())
