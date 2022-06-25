# def double(number: int) -> int:
#     # """引数の2倍を返す関数"""
#     # returun number * 2

def double(number: int) -> int:
    """引数の2倍を返す関数"""
    return number * 2


# print(double(3))
# print(double.__doc__)
# print(__name__)

def main():
    print(double(3))
    print(double.__doc__)
    print(__name__)