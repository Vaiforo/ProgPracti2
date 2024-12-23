import numpy as np
from sympy import log, sqrt
import matplotlib.pyplot as plt

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

_, axes1 = plt.subplots(figsize=(10, 6))
axes1.plot(x_parts, y_values, label='y = log(sqrt(x))', color='r')

axes1.set_title('График функции: y = log(sqrt(x))', fontsize=16)
axes1.set_xlabel('x', fontsize=14)
axes1.set_xlabel('y', fontsize=14)

axes1.legend(fontsize=12)

plt.show()

"""
3) Постройте точечный график функции, в качестве меток для точек
используйте любой доступный маркер. Задайте графику название. Подпишите оси. Измените
цвет точек на желаемый. Цвет задайте с помощью указания значений
красного, зеленого и синего (по модели RGB). Добавьте на график сетку.
Укажите цвет и непрозрачность линий сетки.
"""
print("\n\t\tЗадание 3\n")

plt.figure(figsize=(10, 6))
plt.scatter(x_parts, y_values, label='y = log(sqrt(x))', color=(0.9, 0, 0.1), marker='8')  # RGB color for points

plt.title('График функции: y = log(sqrt(x))', fontsize=16)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)

plt.legend(fontsize=12)

plt.grid(color='gray', alpha=0.5)

plt.show()

"""
4) Используйте выборки из равномерного и нормального распределения
(из задания 3). Постройте две гистограммы. Используйте различные
цвета для гистограмм. Установите для каждой гистограммы собственное
значение количества разбиений. Подпишите гистограммы.
"""
print("\n\t\tЗадание 4\n")

uniform_vector = np.random.uniform(0, 100, 100).astype(int)
normal_vector = np.random.normal(0, 10, 100).astype(int)

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.hist(uniform_vector, bins=20, color=(0.1, 0.5, 0.8), edgecolor='black')
plt.title('Histogram of Uniform Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(normal_vector, bins=15, color=(0.8, 0.3, 0.1), edgecolor='black')
plt.title('Histogram of Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

"""
5) Сгенерируйте выборку из равномерного распределения, состоящую из
50 целых чисел от 1 до 5 (не включая 5). Посчитайте, сколько раз
встречается каждое из чисел в выборке (без циклов!). На основе
полученной информации постройте круговую и столбчатую диаграммы.
Подпишите диаграммы. Для круговой диаграммы укажите подписи
секторов. Для столбчатой диаграммы укажите подписи столбцов. Для
обеих диаграмм укажите множество используемых цветов (для
раскраски секторов и столбцов).
"""
print("\n\t\tЗадание 5\n")

uniform_vector = np.random.uniform(1, 5, 50).astype(int)
values, counters = np.unique(uniform_vector, return_counts=True)

colors = [(0.93, 0.32, 0.32), (0.36, 0.73, 0.32), (0.32, 0.44, 0.73), (1.00, 0.98, 0.32)]

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.pie(counters, labels=values, colors=colors, autopct='%d%%')
plt.title('Pie chart of number distribution')

plt.subplot(1, 2, 2)
plt.bar(values, counters, color=colors, edgecolor='black')
plt.xticks(values)

plt.xlabel('Numbers')
plt.ylabel('Counters')
plt.title('Column chart of number distribution')

plt.tight_layout()
plt.show()

"""
6) Используя знания о разбиении отрезка на множество точек (из пункта
1), а также функцию с несколькими переменными из задания 2 (которая
использовалась для решения задачи оптимизации), постройте
трехмерный график функции. Установите цвет линии на графике.
Важно: если в вашем варианте к заданию 2 функция состояла более чем
из двух переменных - используйте только первые две переменные.
"""
print("\n\t\tЗадание 6\n")


def objective(x):
    return (x[0] - 3) ** 2 + (x[1] - 1) ** 2


a, b = 1, 6
x_parts = np.linspace(a, b, 100)
y_parts = np.linspace(a, b, 100)

x, y = np.meshgrid(x_parts, y_parts)
z = objective(np.array([x, y]))

figure = plt.figure(figsize=(10, 6))
axes = figure.add_subplot(111, projection='3d')

figure.colorbar(axes.plot_surface(x, y, z, cmap='viridis', edgecolor='black'))

axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_zlabel('Objective function values')
axes.set_title('Plot of the objective function')

plt.show()

"""
7) Используя подграфики (subplots) постройте сетку 2x2 из 4 графиков.
Установите размер сетки. Добавьте заголовок сетки, укажите размер
шрифта. В левом верхнем углу сетки разместите график из пункта 2
текущего задания, в правом верхнем - из пункта 3. В левом нижнем -
круговую диаграмму из пункта 5. В правом нижнем - трехмерный
график из пункта 6. Для любого из графиков установите цвет фона.
"""
print("\n\t\tЗадание 7\n")

# figure, axes = plt.subplots(figsize=(10, 10))
#
# figure.suptitle('Сетка графиков 2х2', fontsize=20)
# figure.add_subplot(2, 2, 1)
# figure.add_axes(axes1)
#
# plt.show()