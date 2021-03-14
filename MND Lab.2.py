import random, math
import numpy as np
from numpy import linalg as LA

print("-----Нормована матриця планування експерименту-----")
y_max = (30 - 7)*10
y_min = (20 - 7)*10

x_1 = [-5, 15] # перше значення min, друге значення max
x_2 = [25, 45] # перше значення min, друге значення max

experement_first = [] # x1 = -1.0, x2 = -1.0
experement_second = [] # x1 = +1.0, x2 = -1.0
experement_third = [] # x1 = -1.0, x2 = +1.0


for m in range(5):
    experement_first.append(float(random.randint(y_min, y_max)))
    experement_second.append(float(random.randint(y_min, y_max)))
    experement_third.append(float(random.randint(y_min, y_max)))

print("x1 = -1.0, x2 = -1.0", experement_first, "\n", "x1 = +1.0, x2 = -1.0", experement_second,
      "\n", "x1 = -1.0, x2 = +1.0", experement_third, "\n")

print("-----Знайдемо середнє значення функції відгуку в рядку-----")
not_y1 = 0
not_y2 = 0
not_y3 = 0

for i in range(5):
    not_y1 += experement_first[i] / 5
    not_y2 += experement_second[i] / 5
    not_y3 += experement_third[i] / 5

print("not_y1 =", not_y1, "\n", "not_y2 =", not_y2, "\n", "not_y3 =", not_y3, "\n")

print("-----Знайдемо дисперсії по рядках-----")
disp_y1 = 0
disp_y2 = 0
disp_y3 = 0

for i in range(5):
    disp_y1 += ((experement_first[i] - not_y1) ** 2) / 5
    disp_y2 += ((experement_second[i] - not_y2) ** 2) / 5
    disp_y3 += ((experement_third[i] - not_y3) ** 2) / 5

print("disp_y1 =", disp_y1, "\n", "disp_y2 =", disp_y2, "\n", "disp_y3 =", disp_y3, "\n")

print("-----Обчислимо основне відхилення-----")
vidh = math.sqrt(2*(2*5-2)/5*(5-4))
print("vidh = ", vidh, "\n")

print("Обчислимо F_uv, O_uv, R_uv")
F_uv1 = disp_y1 / disp_y2
F_uv2 = disp_y3 / disp_y1
F_uv3 = disp_y3 / disp_y2

O_uv1 = (3 / 5) * F_uv1
O_uv2 = (3 / 5) * F_uv2
O_uv3 = (3 / 5) * F_uv3

R_uv1 = abs(O_uv1 - 1) / vidh
R_uv2 = abs(O_uv2 - 1) / vidh
R_uv3 = abs(O_uv3 - 1) / vidh

if R_uv1 < 2 and R_uv2 < 2 and R_uv3 < 2:
    print("Дисперсія однорідна", "\n")

print("-----Розрахунок нормованих коефіцієнтів рівняння регресії-----")
X1 = [-1.0, 1.0, -1.0]
X2 = [-1.0, -1.0, 1.0]

mx1 = (X1[0] + X1[1] + X1[2]) / 3
mx2 = (X2[0] + X2[1] + X2[2]) / 3

my = (not_y1 + not_y2 + not_y3) / 3

a1 = ((X1[0] ** 2) + (X1[1] ** 2) + (X1[2] ** 2)) / 3
a2 = ((X1[0] * X2[0]) + (X1[1] * X2[1]) + (X1[2] * X2[2])) / 3
a3 = ((X2[0] ** 2) + (X2[1] ** 2) + (X2[2] ** 2)) / 3

a11 = ((X1[0] * not_y1) + (X1[1] * not_y2) + (X1[2] * not_y3)) / 3
a22 = ((X2[0] * not_y1) + (X2[1] * not_y2) + (X2[2] * not_y3)) / 3

b0 = LA.det([[my, mx1, mx2], [a11, a1, a2], [a22, a2, a3]]) / LA.det([[1, mx1, mx2], [mx1, a1, a2], [mx2, a2, a3]])
b1 = LA.det([[1, my, mx2], [mx1, a11, a2], [mx2, a22, a3]]) / LA.det([[1, mx1, mx2], [mx1, a1, a2], [mx2, a2, a3]])
b2 = LA.det([[1, mx1, my], [mx1, a1, a11], [mx2, a2, a22]]) / LA.det([[1, mx1, mx2], [mx1, a1, a2], [mx2, a2, a3]])

print("Отже, нормоване рівняння регресії:", "\n", "y = {0} + {1}*x1 + {2}*x2".format(b0, b1, b2), "\n")


y1 = b0 + b1*X1[0] + b2*X2[0]
y2 = b0 + b1*X1[1] + b2*X2[1]
y3 = b0 + b1*X1[2] + b2*X2[2]
print("Зробимо перевірку, Результат збігається з середніми значеннями not_yi", "\n",
      y1, "=", not_y1, "\n", y2, "=", not_y2, "\n", y3, "=", not_y3, "\n")

print("-----Проведемо натуралізацію коефіцієнтів-----")
delta_x1 = abs(x_1[1] - x_1[0]) / 2
delta_x2 = abs(x_2[1] - x_2[0]) / 2

x10 = (x_1[1] + x_1[0]) / 2
x20 = (x_2[1] + x_2[0]) / 2

a_0 = b0 - b1*(x10 / delta_x1) - b2*(x20 / delta_x2)
a_1 = b1 / delta_x1
a_2 = b2 / delta_x2

print("Запишемо натуралізоване рівняння регресії:", "\n", "y = {0} + {1}*x1 + {2}*x2".format(a_0, a_1, a_2), "\n", "\n", "Зробимо перевірку:")
y_1 = a_0 + a_1*x_1[0] + a_2*x_2[0]
y_2 = a_0 + a_1*x_1[1] + a_2*x_2[0]
y_3 = a_0 + a_1*x_1[0] + a_2*x_2[1]
print(y_1, "=", not_y1, "\n", y_2, "=", not_y2, "\n", y_3, "=", not_y3, "\n", "\n",
      "Отже, коефіцієнти натуралізованого рівняння регресії вірні.", "\n", "a0 =", a_0, "\n", "a1 =", a_1, "\n", "a2 =", a_2)