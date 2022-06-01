class MycastomError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b == 0:
            print("айайай делить на 0 не нельзя")

def examination(a, b):
    """Проверка деление на 0"""
    try:
        print(int(a / b))
    except ZeroDivisionError:
        print("айайай делить на 0 не нельзя")

