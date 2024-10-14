import numpy as np
import sympy as sp
from numpy import ndarray
from sympy import log, sqrt
from scipy.misc import derivative
import warnings
from scipy.optimize import minimize

warnings.filterwarnings("ignore", category=DeprecationWarning)

"""
1) Найдите первую и вторую производные функции y в заданной точке x0
для своего варианта с помощью scipy. Вариантов меньше, чем
студентов. Ваш вариант – это остаток от деления вашего номера в
группе на количество вариантов.
"""
print("\n\t\tЗадание 1\n")

y = lambda x: log(sqrt(x))
x0 = 2
a = 1
b = 6

print("Первая производная: ", round(derivative(y, x0), 6))
print("Вторая производная: ", round(derivative(y, x0, n=2), 6))

"""
2) Используя функцию из таблицы выше для вашего варианта и пакет
sympy выведите на экран символьное представление производной.
"""
print("\n\t\tЗадание 2\n")

x_sym = sp.symbols('x')
f_sym = log(sqrt(x_sym))
print("Символьное представление первой производной: ", sp.diff(f_sym, x_sym))
print("Символьное представление первой производной: ", sp.diff(f_sym, x_sym, n=2))

"""
3) Вычислите определенный интеграл от a до b с помощью scipy функции
для своего варианта. Интеграл вычислите методом прямоугольников.
"""
print("\n\t\tЗадание 3\n")


def f(x):
    return log(sqrt(x))


n = 1000
integral = 0
h = (b - a) / n
for i in range(n):
    integral += f(a + (i + 0.5) * h) * h

print(f"Определенный интеграл по методу прямоугольников равен: {integral}")

"""
4) С помощью sympy выведите на экран неопределенный интеграл
функции y для вашего варианта.
"""
print("\n\t\tЗадание 4\n")

print(f"Неопределенный интеграл: {sp.integrate(f_sym, x_sym)}")

"""
5) Решите задачу нелинейной оптимизации для вашего варианта.
Выведите оптимальное значение и решение.
"""
print("\n\t\tЗадание 5\n")


def equation(x):
    return (x[0] - 3) ** 2 + (x[1] - 1) ** 2


constraints = [
    {'type': 'ineq', 'fun': lambda x: -2 * x[0] + x[1] - 2},
    {'type': 'ineq', 'fun': lambda x: 3 * x[1] - 10},
    {'type': 'ineq', 'fun': lambda x: x[0]},
    {'type': 'ineq', 'fun': lambda x: x[1]},
]
bounds = [(0, None), (0, None)]
x_start = np.array([0.5, 0])
result = minimize(equation, x_start, constraints=constraints)
print("Оптимальное значение функции:", result.fun)
print("Оптимальное решение:", result.x)
# print(result)
