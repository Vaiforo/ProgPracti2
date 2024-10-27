import sys

import numpy as np
from scipy.linalg import lu
from scipy.stats import mode, chisquare

"""
1) Взять свою матрицу из 1.10
"""
print("\n\t\tЗадание 1\n")

coeff_matrix: np.array = np.array([[2, -5, 1, 0],
                                   [1, -1, -13, 0],
                                   [3, -2, -2, -4],
                                   [4, 0, 2.7, -1.3]])
np.savetxt(sys.stdout, coeff_matrix, fmt="%7.1f")

"""
2) Получить LU-разложение (LUP-разложение) (факторизацию матрицы)
"""
print("\n\t\tЗадание 2\n")

P, L, U = lu(coeff_matrix)
print("P:")
np.savetxt(sys.stdout, P, fmt="%4d")
print("\nL:")
np.savetxt(sys.stdout, L, fmt="%7.4f")
print("\nU:")
np.savetxt(sys.stdout, U, fmt="%7.3f")

"""
3) Найти определитель (произведение элементов на главной диагонали L и
U, определителя обратной матрицы к P)
"""
print("\n\t\tЗадание 3\n")

det_P: float = np.linalg.det(np.linalg.inv(P))
if det_P != 0:
    det_PLU: float = np.linalg.det(np.linalg.inv(P)) * np.prod(np.diag(L)) * np.prod(np.diag(U))
    print(f"Определитель: {det_PLU}")
else:
    print(f"Определитель P равен нулю")

"""
4) Сгенерировать две выборки (вектор целых чисел из 100 элементов) в
одинаковых интервалах с разными распределениями (равномерное и
нормальное)
"""
print("\n\t\tЗадание 4\n")

uniform_vector: np.array = np.random.uniform(0, 100, 100).astype(int)
print(f"Вектор целых чисел с равномерным распределением:\n{uniform_vector}")

normal_vector: np.array = np.random.normal(0, 10, 100).astype(int)
print(f"Вектор целых чисел с нормальным распределением:\n{normal_vector}")

"""
5) Вычислить для каждой из выборок:
a. Среднее;
b. Моду;
c. Медиану;
d. Минимум;
e. Максимум;
f. Стандартное отклонение.
"""
print("\n\t\tЗадание 5\n")


def print_vector_info(vector: np.array):
    print(f"Среднее: {np.mean(vector)}")
    vector_mode = mode(vector)
    print(f"Мода: {vector_mode.mode} Повторений: {vector_mode.count}")
    print(f"Медиана: {np.median(vector)}")
    print(f"Минимум: {np.min(vector)}")
    print(f"Максимум: {np.max(vector)}")
    print(f"Стандартное отклонение: {np.std(vector)}\n")


print_vector_info(uniform_vector)
print_vector_info(normal_vector)

"""
6) С помощью метода хи-квадрат (scipy.stats.chisquare) вычислить значение
p-value для нулевой гипотезы: “Распределение выборки не
равномерное”.
"""
print("\n\t\tЗадание 6\n")

print(f"Значение p-value: {chisquare(uniform_vector).pvalue.astype(int)}")
