import random, math
import numpy as np
from numpy import linalg as LA

N = 4

m = int(input("Введіть значення параметру m:"))

x_1 = [-5, 15] # перше значення min, друге значення max
x_2 = [25, 45] # перше значення min, друге значення max
x_3 = [15, 45] # перше значення min, друге значення max

y_max = 200 + ((x_1[1] + x_2[1] + x_3[1]) / 3)
y_min = 200 + ((x_1[0] + x_2[0] + x_3[0]) / 3)


print("-----Матриця планування експерименту(з натуралізованими значеннями факторів)-----")

experement_first = [] # x1 = -1.0, x2 = -1.0, x3 = -1.0
experement_second = [] # x1 = -1.0, x2 = +1.0, x3 = +1.0
experement_third = [] # x1 = +1.0, x2 = -1.0, x3 = +1.0
experement_fourth = [] # x1 = +1.0, x2 = +1.0, x3 = -1.0

for l in range(m):
    experement_first.append(float(random.uniform(y_min, y_max)))
    experement_second.append(float(random.uniform(y_min, y_max)))
    experement_third.append(float(random.uniform(y_min, y_max)))
    experement_fourth.append(float(random.uniform(y_min, y_max)))

print("x1 = -1.0, x2 = -1.0, x3 = -1.0", experement_first, "\n", "x1 = -1.0, x2 = +1.0, x3 = +1.0", experement_second,
      "\n", "x1 = +1.0, x2 = -1.0, x3 = +1.0", experement_third, "\n", "x1 = +1.0, x2 = +1.0, x3 = -1.0", experement_fourth, "\n")


print("-----Знайдемо середнє значення функції відгуку в рядку-----")
not_y1 = 0
not_y2 = 0
not_y3 = 0
not_y4 = 0

for i in range(m):
    not_y1 += experement_first[i] / m
    not_y2 += experement_second[i] / m
    not_y3 += experement_third[i] / m
    not_y4 += experement_fourth[i] / m

print("not_y1 =", not_y1, "\n", "not_y2 =", not_y2, "\n", "not_y3 =", not_y3, "\n", "not_y4 =", not_y4, "\n")

mx1 = (x_1[0] + x_1[0] + x_1[1] + x_1[1]) / 4
mx2 = (x_2[0] + x_2[1] + x_2[0] + x_2[1]) / 4
mx3 = (x_3[0] + x_3[1] + x_3[1] + x_3[0]) / 4

my = (not_y1 + not_y2 + not_y3 + not_y4) / 4

a1 = (x_1[0] * not_y1 + x_1[0] * not_y2 + x_1[1] * not_y3 + x_1[1] * not_y4) / 4
a2 = (x_2[0] * not_y1 + x_2[1] * not_y2 + x_2[0] * not_y3 + x_2[1] * not_y4) / 4
a3 = (x_3[0] * not_y1 + x_3[1] * not_y2 + x_3[1] * not_y3 + x_3[0] * not_y4) / 4

a11 = (2 * (x_1[0] ** 2) + 2 * (x_1[1] ** 2)) / 4
a22 = (2 * (x_2[0] ** 2) + 2 * (x_2[1] ** 2)) / 4
a33 = (2 * (x_3[0] ** 2) + 2 * (x_3[1] ** 2)) / 4

a12 = (x_1[0] * x_2[0] + x_1[0] * x_2[1] + x_1[1] * x_2[0] + x_1[1] * x_2[1]) / 4
a13 = (x_1[0] * x_3[0] + x_1[0] * x_3[1] + x_1[1] * x_3[1] + x_1[1] * x_3[0]) / 4
a23 = (x_2[0] * x_3[0] + x_2[1] * x_3[1] + x_2[0] * x_3[1] + x_2[1] * x_3[0]) / 4

b0 = LA.det([[my, mx1, mx2, mx3], [a1, a11, a12, a13], [a2, a12, a22, a23], [a3, a13, a23, a33]]) / LA.det([[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a23], [mx3, a13, a23, a33]])
b1 = LA.det([[1, my, mx2, mx3], [mx1, a1, a12, a13], [mx2, a2, a22, a23], [mx3, a3, a23, a33]]) / LA.det([[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a23], [mx3, a13, a23, a33]])
b2 = LA.det([[1, mx1, my, mx3], [mx1, a11, a1, a13], [mx2, a12, a2, a23], [mx3, a13, a3, a33]]) / LA.det([[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a23], [mx3, a13, a23, a33]])
b3 = LA.det([[1, mx1, mx2, my], [mx1, a11, a12, a1], [mx2, a12, a22, a2], [mx3, a13, a23, a3]]) / LA.det([[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a23], [mx3, a13, a23, a33]])

print("Запишемо отримане рівняння регресії:", "\n", "y = {0} + {1}*x1 + {2}*x2 + {3}*x3".format(b0, b1, b2, b3), "\n")

print("Зробимо перевірку (підставимо значення факторів з матриці планування і порівняємо результат з середніми значеннями функції відгуку за рядками): ")

y1 = b0 + b1 * x_1[0] + b2 * x_2[0] + b3 * x_3[0]
y2 = b0 + b1 * x_1[0] + b2 * x_2[1] + b3 * x_3[1]
y3 = b0 + b1 * x_1[1] + b2 * x_2[0] + b3 * x_3[1]
y4 = b0 + b1 * x_1[1] + b2 * x_2[1] + b3 * x_3[0]

print(y1, "=", not_y1, "\n", y2, "=", not_y2, "\n", y3, "=", not_y3, "\n", y4, "=", not_y4, "\n")


print("-----Для проведення статистичних перевірок необхідно використовувати матрицю планування з нормованими значеннями факторів-----")
print("x0 = +1.0, x1 = -1.0, x2 = -1.0, x3 = -1.0", experement_first, "\n", "x0 = +1.0, x1 = -1.0, x2 = +1.0, x3 = +1.0", experement_second,
      "\n", "x0 = +1.0, x1 = +1.0, x2 = -1.0, x3 = +1.0", experement_third, "\n", "x0 = +1.0, x1 = +1.0, x2 = +1.0, x3 = -1.0", experement_fourth, "\n")

print("-----Перевірка однорідності дисперсії за критерієм Кохрена:-----")
print("not_y1 =", not_y1, "\n", "not_y2 =", not_y2, "\n", "not_y3 =", not_y3, "\n", "not_y4 =", not_y4, "\n")

print("Знайдемо дисперсії по рядках:")
disp_y1 = 0
disp_y2 = 0
disp_y3 = 0
disp_y4 = 0
disp_list = [disp_y1, disp_y2, disp_y3, disp_y4]

for i in range(m):
    disp_y1 += ((experement_first[i] - not_y1) ** 2) / m
    disp_y2 += ((experement_second[i] - not_y2) ** 2) / m
    disp_y3 += ((experement_third[i] - not_y3) ** 2) / m
    disp_y4 += ((experement_fourth[i] - not_y4) ** 2) / m

Gp = max(disp_list) / (disp_y1 + disp_y2 + disp_y3 + disp_y4)
print("disp_y1 =", disp_y1, "\n", "disp_y2 =", disp_y2, "\n", "disp_y3 =", disp_y3, "\n")

f1 = m - 1
f2 = N

Gt = float(input("!!!!!Введіть значення з таблиці Кохрена, яке знаходиться в {0} рядку {1} стовпчику!!!!!:".format(f2, f1)))

if Gp < Gt:
    print("Дисперсія однорідна")
    print("-----Оцінимо значимість коефіцієнтів регресії згідно критерію Стьюдента-----")
    s_2_b = (disp_y1 + disp_y2 + disp_y3 + disp_y4) / N

    s_2_b_s = s_2_b / (N * m)

    s_b_s = math.sqrt(s_2_b_s)

    b_0 = ((not_y1 * 1) + (not_y2 * 1) + (not_y3 * 1) + (not_y4 * 1)) / m
    b_1 = ((not_y1 * -1) + (not_y2 * -1) + (not_y3 * 1) + (not_y4 * 1)) / m
    b_2 = ((not_y1 * -1) + (not_y2 * 1) + (not_y3 * -1) + (not_y4 * 1)) / m
    b_3 = ((not_y1 * -1) + (not_y2 * 1) + (not_y3 * 1) + (not_y4 * -1)) / m

    t_0 = math.fabs(b_0) / s_b_s
    t_1 = math.fabs(b_1) / s_b_s
    t_2 = math.fabs(b_2) / s_b_s
    t_3 = math.fabs(b_3) / s_b_s

    f3 = (m - 1) * N
    print("t_0 =", t_0, "\n", "t_1 =", t_1, "\n", "t_2 =", t_2, "\n", "t_3 =", t_3, "\n")
    t_tabl = float(input("!!!!!Введіть значення з таблиці Стьюдента, яке знаходится на {0} рядку!!!!!:".format(f3)))

    y_1 = 0
    y_2 = 0
    y_3 = 0
    y_4 = 0

    t_list = [t_0, t_1, t_2, t_3]
    t_list_new = []
    for i in range(len(t_list)):
        if t_list[i] > t_tabl:
            t_list_new.append(t_list[i])
#У циклі на 145 стрічці я рахую значення функцій без незначних коефіцієнтів, тобто тих коефіцієнтів, які не пройшли оцінку значимості коефіцієнтів регресії згідно критерію Стьюдента.
    for j in t_list_new:
        n = t_list.index(j)
        if n == 0:
            y_1 += b0
            y_2 += b0
            y_3 += b0
            y_4 += b0
        elif n == 1:
            y_1 += b1 * x_1[0]
            y_2 += b1 * x_1[0]
            y_3 += b1 * x_1[1]
            y_4 += b1 * x_1[1]
        elif n == 2:
            y_1 += b2 * x_2[0]
            y_2 += b2 * x_2[1]
            y_3 += b2 * x_2[0]
            y_4 += b2 * x_2[1]
        elif n == 3:
            y_1 += b3 * x_3[0]
            y_2 += b3 * x_3[1]
            y_3 += b3 * x_3[1]
            y_4 += b3 * x_3[0]

    print("Незначимі коефіцієнти рівняння регресії були виключені з рівняння")
    print("y_1 =", y_1, "\n", "y_2 =", y_2, "\n", "y_3 =", y_3, "\n", "y_4 =", y_4, "\n")

    print("----Критерій Фішера-----")
    d = len(t_list_new)
    f4 = N - d

    Ft = float(input("!!!!!Введіть значення з таблиці Фішера, яке знаходиться в {0} рядку {1} стовпчику!!!!!:".format(f3, f4)))

    s_2_ad = (m / (N - d)) * (((y_1 - not_y1) ** 2) + ((y_2 - not_y2) ** 2) + ((y_3 - not_y3) ** 2) + ((y_4 - not_y4) ** 2))
    Fp = s_2_ad / s_2_b_s
    print("Fp =", Fp)
    if Fp < Ft:
        print("Рівняння регресії адекватно оригіналу при рівні значимості 0.05")
    else:
        print("Рівняння регресії неадекватно оригіналу при рівні значимості 0.05")

else:
    print("Дисперсія не однорідна")
