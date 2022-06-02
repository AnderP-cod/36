
class MycastomError(Exception):
    def __str__(self):
        return "айайай делить на ноль нельзя"


def examination(a, b):
    """Проверка деление на 0"""
    if a > 0 and b > 0:
        print(int(a / b))
        return int(a / b)
    elif b == 0:
        raise MycastomError

