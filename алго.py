from typing import Union


def algo(max_number: str) -> Union[list[int], list[str]]:
    ls: list[int] = []
    try:
        int_number: int = int(max_number)
    except ValueError:
        return ["Нельзя вводить символы отличные от числовых!"]
    for num in range(1, int_number+1):
        up = [num]*num
        ls += up
    if len(ls) == 0:
        return ["Число должно быть больше 0!"]
    return ls


if __name__ == '__main__':
    number: str = input()
    print(*algo(number))










