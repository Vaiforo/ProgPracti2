import sys

import numpy as np

"""
1) Создайте numpy array my_array, элементами которого будут числа из
интервала [10, 70) с шагом 2. Выведите на экран результат.
"""
print("\n\n\t1 задание\n")

my_array: np.ndarray = np.arange(10, 70, 2)
print("[10, 70) step=2: [", *my_array, "]")

"""
2) Преобразуйте полученный my_array в матрицу A (6x5).
Транспонируйте матрицу A. Далее будем работать с
транспонированной матрицей A.
"""
print("\n\n\t2 задание\n")

A: np.ndarray = my_array.reshape(6, 5).T
print("Матрица A:")
np.savetxt(sys.stdout, A, fmt="%3d")

"""
3) Умножьте все элементы матрицы на 2.5 и вычтете из каждого элемента
5 (в одной строке). Выведите новую матрицу на экран.
"""
print("\n\n\t3 задание\n")

A = A * 2.5 - 5
A = A.astype(int)
print("Матрица A*2.5 и A[0] - 5:")
np.savetxt(sys.stdout, A, fmt="%4d")

"""
4) Создайте матрицу B (6x3) заполняя каждую ячейку случайным
действительным числом от 0 до 10. Выведите матрицу на экран.
"""
print("\n\n\t4 задание\n")

B: np.ndarray = np.random.randint(0, 10, (6, 3))
print("Матрица B:")
np.savetxt(sys.stdout, B, fmt="%3d")

"""
5) Получите вектор a, элементами которого являются суммы по всем
строкам матрицы A. Получите вектор b, элементами которого являются
суммы по всем столбцам матрицы B. Выведите на экран размеры
полученных векторов.
"""
print("\n\n\t5 задание\n")

a: np.ndarray = np.sum(A, axis=1).reshape(-1, 1)
# np.savetxt(sys.stdout, a, fmt="%d")
print("Размера вектора a:", a.shape[0])

b: np.ndarray = np.sum(B, axis=0)
# np.savetxt(sys.stdout, b, fmt="%d")
print("Размера вектора b:", b.shape[0])

"""
6) Вычислите произведение матриц A и B.
"""
print("\n\n\t6 задание\n")

print("Произведение матриц A и B:")
np.savetxt(sys.stdout, np.dot(A, B), fmt="%5d")

"""
7) Удалите третий столбец из матрицы A. Добавьте три столбца из
случайных чисел от 10 до 20 к матрице B. На данном шаге у вас
должны получиться две квадратные матрицы A и B (5x5 и 6x6).
"""
print("\n\n\t7 задание\n")

A = np.delete(A, 2, axis=1)
print("Матрица A без 3-его столбца:")
np.savetxt(sys.stdout, A, fmt="%3d")

B = np.concatenate((B, np.random.randint(10, 20, (6, 3))), axis=1)
print("\nМатрица B c 3-мя новыми столбцами:")
np.savetxt(sys.stdout, B, fmt="%3d")

"""
8) Найдите определители матриц A и B. Вычислите обратные матрицы
для матриц A и B. Обратите внимание на то, что определитель может
быть равен нулю и тогда вычисление обратной матрицы невозможно.
"""
print("\n\n\t8 задание\n")

determA: float = np.linalg.det(A)
determB: float = np.linalg.det(B)
print(f"Определитель матрциы A: {determA}\nОпределитель матрцы B: {determB}\n")

if determA:
    print("Обратная матрица матрице A:")
    np.savetxt(sys.stdout, np.linalg.inv(A), fmt="%10.5f")
else:
    print("Определитель матрицы A равен нулю")

print()
if determB:
    print("Обратная матрица матрице B:")
    np.savetxt(sys.stdout, np.linalg.inv(B), fmt="%10.5f")
else:
    print("Определитель матрицы B равен нулю")

"""
9) Возведите матрицу A в 6 степень, а матрицу B – в 14.
"""
print("\n\n\t9 задание\n")

print("Матрица А в 6 степени:")
np.savetxt(sys.stdout, np.linalg.matrix_power(A, 6), fmt="%18d")

print("\nМатрица B в 14 степени:")
np.savetxt(sys.stdout, np.linalg.matrix_power(B, 14), fmt="%13d")

"""
10) Решите систему линейных уравнений для своего варианта. Вариантов
меньше, чем студентов. Ваш вариант – это остаток от деления вашего
номера в группе на количество вариантов.
"""
print("\n\n\t10 задание\n=== Вариант 2 ===")

coeff_matrix: np.array = np.array([[2, -5, 1, 0],
                                   [1, -1, -13, 0],
                                   [3, -2, -2, -4],
                                   [4, 0, 2.7, -1.3]])
values_matrix: np.array = np.array([-4, 2.6, 1, -2])
answer: np.ndarray = np.linalg.solve(coeff_matrix, values_matrix)
for i in range(1, len(answer) + 1):
    print(f"x{i} = {round(float(answer[i - 1]), 5)}")
