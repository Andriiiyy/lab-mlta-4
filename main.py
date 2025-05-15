import os
import sys
import textwrap
from pprint import pprint

from tasks import *

sys.setrecursionlimit(1005)


menu: str = (
    "1. Динамічне програмування\n"
    "2. Жадібні алгоритми\n"
)

tasks: dict[str, str] = {
    "ДП": "Кенгуру хоче перебратися на іншу сторону річки. Він знає, що через річку є стежка з n-рівновіддалених "
           "купин (2 <= n <= 30) Кенгуру може стрибати на наступну купину, або через одну купину. "
           "Визначте максимальну кількість маршрутів, якими кенгуру може подолати річку.",
    "ЖА": "У Вас є k куп піску з дорогоцінними каменями. Кожна купа має вагу m_i (1 <= m_i <= 100) та вартість "
           "одиниці піску v_i (1 <= v_i <= 1000). Ви маєте рюкзак, що вміщує n кілограмів. Визначте, як заповнити "
           "рюкзак піском так, щоб вартість піску була максимальною. Ви можете брати дробову частину піску."
}

def main():
    jump_size: list[int] = [1, 2]
    task_input: int = 0
    wrap_width = 70

    print(menu)
    menu_item: int = int(input("Виберіть пункт меню: "))
    match menu_item:
        case 1:
            print(textwrap.fill(tasks["ДП"], wrap_width))
            task_input = int(input("Введіть кількість купин: "))
            pprint(f"Для {task_input} купин є {kangaro(task_input, jump_size)} комбінацій стрибків")
        case 2:
            print(textwrap.fill(tasks["ЖА"], wrap_width))
            n = int(input("Введіть максимальну вагу рюкзака: "))
            k = int(input("Введіть кількість куп піску: "))
            piles = []
            for i in range(k):
                m = int(input(f"Вага купи {i+1}: "))
                v = int(input(f"Вартість купи {i+1}: "))
                piles.append((m, v))
            pprint(f"Максимальна вартість піску в рюкзаку: {max_sand_value(n, piles):.2f} грн")
    to_main()

def to_main():
    input("Натисніть ентер")
    os.system('clear')
    main()

if __name__ == '__main__':
    main()
