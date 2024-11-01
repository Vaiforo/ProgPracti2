import numpy as np
from sympy import log, sqrt

"""
1) Используйте функцию и отрезок ([a, b]) из вашего варианта задания 2
(которые вы использовали для интегрирования). Разбейте отрезок на
столько частей, сколько считаете нужным. Вычислите значение
функции для всех точек получившегося массива.
"""
print("\n\t\tЗадание 1\n")

y = lambda x: log(sqrt(x))
a = 1
b = 6
x0 = 2

x_parts: np.array = np.linspace(a, b, 100)
y_values: np.array = np.array(list(map(y, x_parts)))
print(f"Значение функции для всех точек X:\n{y_values}")

"""
2) Используя множество точек и множество значений функции в этих
точках, постройте простой график функции (метод plot()). Задайте
графику название. Подпишите оси. Установите желаемые размеры
шрифта для названия и подписей. Добавьте на график легенду.
"""
print("\n\t\tЗадание 2\n")

