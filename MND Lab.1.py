import random
# Ільяш Вадим Вікторович
# ІВ-93
# 7 у списку групи
########################################################################################################################
#Тестові значення
#a0 = 7
#a1 = 8
#a2 = 10
#a3 = 7
#X1 = [0, 14, 15, 15, 2, 8, 17, 11]
#X2 = [7, 4, 14, 19, 8, 19, 14, 1]
#X3 = [11, 19, 13, 4, 12, 14, 8, 19]

########################################################################################################################
#Значення згенеровані випадково
a0 = random.randint(1, 10)
a1 = random.randint(1, 10)
a2 = random.randint(1, 10)
a3 = random.randint(1, 10)
X1 = []
X2 = []
X3 = []

for i in range(0, 8):
    X1_element = random.randint(0, 20)
    X2_element = random.randint(0, 20)
    X3_element = random.randint(0, 20)
    X1.append(X1_element)
    X2.append(X2_element)
    X3.append(X3_element)

########################################################################################################################

Y = []
for i in range(0, 8):
    Y.append(a0 + a1*X1[i] + a2*X2[i] + a3*X3[i])
print("Y = ", Y, "\n", "X1 = ", X1, "\n", "X2 = ", X2, "\n", "X3 = ", X3)
print("a0, a1, a2, a3 = ", a0, ",", a1, ",", a2, ",", a3)


min_value = [min(X1), min(X2), min(X3)]
max_value = [max(X1), max(X2), max(X3)]

x0 = []

for i in range(0, 3):
    x0.append((min_value[i] + max_value[i])/2)
print("x0 = ", x0)


dx = []

for i in range(0, 3):
    dx.append(x0[i] - min_value[i])
print("dx = ", dx)

Xn1 = []
Xn2 = []
Xn3 = []

for i in range(0, 3):
    if i == 0:
        for j in range(0, 8):
            Xn1.append((X1[j] - x0[i]) / dx[i])
    elif i == 1:
        for j in range(0, 8):
            Xn2.append((X2[j] - x0[i]) / dx[i])
    else:
        for j in range(0, 8):
            Xn3.append((X3[j] - x0[i]) / dx[i])


print("Xn1 = ", Xn1, "\n", "Xn2 = ", Xn2, "\n", "Xn3 = ", Xn3)

Y_etalon = a0 + a1*x0[0] + a2*x0[1] + a3*x0[2]
print("Y_etalon = ", Y_etalon)


Y_define = []
Y_minus = []
for i in range(0, 8):
    element = str(Y[i] - Y_etalon)
    Y_define.append(element)
    if element[0:1] == "-":
        Y_minus.append(float(element))
    elif element == "0":
        Y_minus.append(float(element))

print("Y_define = ", Y_define)
print("Y_minus = ", Y_minus)

#Y_minus_max = max(Y_minus)
#print(Y_minus_max)


for i in range(0, 8):
    if Y_define[i] == str(max(Y_minus)):
        print("Точка плану, що задовольняє критерію вибору оптимальності = [", X1[i], ",", X2[i], ",", X3[i], "]")
