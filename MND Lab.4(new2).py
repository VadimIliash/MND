import math
import numpy as np
from numpy.linalg import solve
from scipy.stats import f, t
from functools import partial
from random import randint



def Lab4(m):
    while True:
        fisher_teor = partial(f.ppf, q=1 - 0.05)
        student_teor = partial(t.ppf, q=1 - 0.025)

        X1min = 10
        X1max = 40
        X2min = 15
        X2max = 50
        X3min = 10
        X3max = 30

        Xmax_average = (X1max + X2max + X3max) / 3
        Xmin_average = (X1min + X2min + X3min) / 3

        y_max = round(200 + Xmax_average)
        y_min = round(200 + Xmin_average)


        # Матриця ПФЕ
        x0_factor = [1, 1, 1, 1, 1, 1, 1, 1]
        x1_factor = [-1, -1, 1, 1, -1, -1, 1, 1]
        x2_factor = [-1, 1, -1, 1, -1, 1, -1, 1]
        x3_factor = [-1, 1, 1, -1, 1, -1, -1, 1]
        x1x2_factor = [a * b for a, b in zip(x1_factor, x2_factor)]
        x1x3_factor = [a * b for a, b in zip(x1_factor, x3_factor)]
        x2x3_factor = [a * b for a, b in zip(x2_factor, x3_factor)]
        x1x2x3_factor = [a * b * c for a, b, c in zip(x1_factor, x2_factor, x3_factor)]

        if m == 3:
            y1, y2, y3 = [], [], []
            for i in range(0, 8):
                y1.append(randint(y_min, y_max))
                y2.append(randint(y_min, y_max))
                y3.append(randint(y_min, y_max))

            Y_average = [round(np.average([y1[0], y2[0], y3[0]]), 3), round(np.average([y1[1], y2[1], y3[1]]), 3),
                         round(np.average([y1[2], y2[2], y3[2]]), 3), round(np.average([y1[3], y2[3], y3[3]]), 3),
                         round(np.average([y1[4], y2[4], y3[4]]), 3), round(np.average([y1[5], y2[5], y3[5]]), 3),
                         round(np.average([y1[6], y2[6], y3[6]]), 3), round(np.average([y1[7], y2[7], y3[7]]), 3)]

            x0 = [1, 1, 1, 1, 1, 1, 1, 1]
            x1 = [10, 10, 40, 40, 10, 10, 40, 40]
            x2 = [15, 50, 15, 50, 15, 50, 15, 50]
            x3 = [10, 30, 30, 10, 30, 10, 10, 30]
            x1x2 = [a * b for a, b in zip(x1, x2)]
            x1x3 = [a * b for a, b in zip(x1, x3)]
            x2x3 = [a * b for a, b in zip(x2, x3)]
            x1x2x3 = [a * b * c for a, b, c in zip(x1, x2, x3)]

            list_for_solve_b = [x0_factor, x1_factor, x2_factor, x3_factor, x1x2_factor, x1x3_factor, x2x3_factor, x1x2x3_factor]
            list_for_solve_a = list(zip(x0, x1, x2, x3, x1x2, x1x3, x2x3, x1x2x3))

            N = 8
            list_bi = []
            for k in range(N):
                S = 0
                for i in range(N):
                    S += (list_for_solve_b[k][i] * Y_average[i]) / N
                list_bi.append(round(S, 5))


            Disp_list = [0, 0, 0, 0, 0, 0, 0, 0]


            Y_row1 = [y1[0], y2[0], y3[0]]
            Y_row2 = [y1[1], y2[1], y3[1]]
            Y_row3 = [y1[2], y2[2], y3[2]]
            Y_row4 = [y1[3], y2[3], y3[3]]
            Y_row5 = [y1[4], y2[4], y3[4]]
            Y_row6 = [y1[5], y2[5], y3[5]]
            Y_row7 = [y1[6], y2[6], y3[6]]
            Y_row8 = [y1[7], y2[7], y3[7]]

            for i in range(m):
                Disp_list[0] += ((Y_row1[i] - np.average(Y_row1)) ** 2) / m
                Disp_list[1] += ((Y_row2[i] - np.average(Y_row2)) ** 2) / m
                Disp_list[2] += ((Y_row3[i] - np.average(Y_row3)) ** 2) / m
                Disp_list[3] += ((Y_row4[i] - np.average(Y_row4)) ** 2) / m
                Disp_list[4] += ((Y_row5[i] - np.average(Y_row5)) ** 2) / m
                Disp_list[5] += ((Y_row6[i] - np.average(Y_row6)) ** 2) / m
                Disp_list[6] += ((Y_row7[i] - np.average(Y_row7)) ** 2) / m
                Disp_list[7] += ((Y_row8[i] - np.average(Y_row8)) ** 2) / m

            sum_dispersion = sum(Disp_list)


            print("| x0 | x1 | x2 | x3 | x1x2 | x1x3 | x2x3 | x1x2x3 | y1 | y2 | y3 | y | s^2 |\n"
                  "|x0 = ", x0_factor, "\n"
                  "|x1 = ", x1_factor, "\n"
                  "|x2 = ", x2_factor, "\n"
                  "|x3 = ", x3_factor, "\n"
                  "|x1x2 = ", x1x2_factor, "\n"
                  "|x1x3 = ", x1x3_factor, "\n"
                  "|x2x3 = ", x2x3_factor, "\n"
                  "|x1x2x3 = ", x1x2x3_factor, "\n"
                  "|y1 = ", y1, "\n"
                  "|y2 = ", y2, "\n"
                  "|y3 = ", y3, "\n"
                  "|y = ", Y_average, "\n"
                  "|s^2 = ", Disp_list, "\n")

            # рівняння регресії з ефектом взаємодії
            print("y = {} + {}*x1 + {}*x2 + {}*x3 + {}*x1x2 + {}*x1x3 + {}*x2x3 + {}*x1x2x3 \n".format(list_bi[0], list_bi[1],
                                                                                                       list_bi[2], list_bi[3],
                                                                                                       list_bi[4], list_bi[5],
                                                                                                       list_bi[6], list_bi[7]))

            print("###################################################################################################################")

            print("| x0 | x1 | x2 | x3 | x1x2 | x1x3 | x2x3 | x1x2x3 | y1 | y2 | y3 | y | s^2 |\n"
                  "|x0 = ", x0, "\n"
                  "|x1 = ", x1, "\n"
                  "|x2 = ", x2, "\n"
                  "|x3 = ", x3, "\n"
                  "|x1x2 = ", x1x2, "\n"
                  "|x1x3 = ", x1x3, "\n"
                  "|x2x3 = ", x2x3, "\n"
                  "|x1x2x3 = ", x1x2x3, "\n"
                  "|y1 = ", y1, "\n"
                  "|y2 = ", y2, "\n"
                  "|y3 = ", y3, "\n"
                  "|y = ", Y_average, "\n"
                  "|s^2 = ", Disp_list, "\n")

            list_ai = [round(i, 5) for i in solve(list_for_solve_a, Y_average)]
            print("y = {} + {}*x1 + {}*x2 + {}*x3 + {}*x1x2 + {}*x1x3 + {}*x2x3 + {}*x1x2x3".format(list_ai[0], list_ai[1],
                                                                                                    list_ai[2], list_ai[3],
                                                                                                    list_ai[4], list_ai[5],
                                                                                                    list_ai[6], list_ai[7]))

            print("###################################################################################################################")

            Gp = max(Disp_list) / sum_dispersion
            F1 = m - 1
            N = len(y1)
            F2 = N
            q1 = 0.05 / F1
            fisher_value = f.ppf(q=1 - q1, dfn=F2, dfd=(F1 - 1) * F2)
            Gt = fisher_value / (fisher_value + F1 - 1)
            print("\nGp = ", Gp, " Gt = ", Gt)
        else:
            y1, y2, y3, y4 = [], [], [], []
            for i in range(0, 8):
                y1.append(randint(y_min, y_max))
                y2.append(randint(y_min, y_max))
                y3.append(randint(y_min, y_max))
                y4.append(randint(y_min, y_max))

            Y_average = [round(np.average([y1[0], y2[0], y3[0], y4[0]]), 3), round(np.average([y1[1], y2[1], y3[1], y4[1]]), 3),
                         round(np.average([y1[2], y2[2], y3[2], y4[2]]), 3), round(np.average([y1[3], y2[3], y3[3], y4[3]]), 3),
                         round(np.average([y1[4], y2[4], y3[4], y4[4]]), 3), round(np.average([y1[5], y2[5], y3[5], y4[5]]), 3),
                         round(np.average([y1[6], y2[6], y3[6], y4[6]]), 3), round(np.average([y1[7], y2[7], y3[7], y4[7]]), 3)]

            x0 = [1, 1, 1, 1, 1, 1, 1, 1]
            x1 = [10, 10, 40, 40, 10, 10, 40, 40]
            x2 = [15, 50, 15, 50, 15, 50, 15, 50]
            x3 = [10, 30, 30, 10, 30, 10, 10, 30]
            x1x2 = [a * b for a, b in zip(x1, x2)]
            x1x3 = [a * b for a, b in zip(x1, x3)]
            x2x3 = [a * b for a, b in zip(x2, x3)]
            x1x2x3 = [a * b * c for a, b, c in zip(x1, x2, x3)]

            list_for_solve_b = [x0_factor, x1_factor, x2_factor, x3_factor, x1x2_factor, x1x3_factor, x2x3_factor,
                                x1x2x3_factor]
            list_for_solve_a = list(zip(x0, x1, x2, x3, x1x2, x1x3, x2x3, x1x2x3))

            N = 8
            list_bi = []
            for k in range(N):
                S = 0
                for i in range(N):
                    S += (list_for_solve_b[k][i] * Y_average[i]) / N
                list_bi.append(round(S, 5))

            Disp_list = [0, 0, 0, 0, 0, 0, 0, 0]

            Y_row1 = [y1[0], y2[0], y3[0], y4[0]]
            Y_row2 = [y1[1], y2[1], y3[1], y4[1]]
            Y_row3 = [y1[2], y2[2], y3[2], y4[2]]
            Y_row4 = [y1[3], y2[3], y3[3], y4[3]]
            Y_row5 = [y1[4], y2[4], y3[4], y4[4]]
            Y_row6 = [y1[5], y2[5], y3[5], y4[5]]
            Y_row7 = [y1[6], y2[6], y3[6], y4[6]]
            Y_row8 = [y1[7], y2[7], y3[7], y4[7]]

            for i in range(m):
                Disp_list[0] += ((Y_row1[i] - np.average(Y_row1)) ** 2) / m
                Disp_list[1] += ((Y_row2[i] - np.average(Y_row2)) ** 2) / m
                Disp_list[2] += ((Y_row3[i] - np.average(Y_row3)) ** 2) / m
                Disp_list[3] += ((Y_row4[i] - np.average(Y_row4)) ** 2) / m
                Disp_list[4] += ((Y_row5[i] - np.average(Y_row5)) ** 2) / m
                Disp_list[5] += ((Y_row6[i] - np.average(Y_row6)) ** 2) / m
                Disp_list[6] += ((Y_row7[i] - np.average(Y_row7)) ** 2) / m
                Disp_list[7] += ((Y_row8[i] - np.average(Y_row8)) ** 2) / m

            sum_dispersion = sum(Disp_list)

            print("| x0 | x1 | x2 | x3 | x1x2 | x1x3 | x2x3 | x1x2x3 | y1 | y2 | y3 | y | s^2 |\n"
                  "|x0 = ", x0_factor, "\n"
                  "|x1 = ", x1_factor, "\n"
                  "|x2 = ", x2_factor, "\n"
                  "|x3 = ", x3_factor, "\n"
                  "|x1x2 = ", x1x2_factor, "\n"
                  "|x1x3 = ", x1x3_factor, "\n"
                  "|x2x3 = ", x2x3_factor, "\n"
                  "|x1x2x3 = ", x1x2x3_factor, "\n"
                  "|y1 = ", y1, "\n"
                  "|y2 = ", y2, "\n"
                  "|y3 = ", y3, "\n"
                  "|y4 = ", y4, "\n"
                  "|y = ", Y_average, "\n"
                  "|s^2 = ", Disp_list, "\n")

            # рівняння регресії з ефектом взаємодії
            print("y = {} + {}*x1 + {}*x2 + {}*x3 + {}*x1x2 + {}*x1x3 + {}*x2x3 + {}*x1x2x3 \n".format(list_bi[0],
                                                                                                       list_bi[1],
                                                                                                       list_bi[2],
                                                                                                       list_bi[3],
                                                                                                       list_bi[4],
                                                                                                       list_bi[5],
                                                                                                       list_bi[6],
                                                                                                       list_bi[7]))

            print("###################################################################################################################")

            print("| x0 | x1 | x2 | x3 | x1x2 | x1x3 | x2x3 | x1x2x3 | y1 | y2 | y3 | y | s^2 |\n"
                  "|x0 = ", x0, "\n"
                  "|x1 = ", x1, "\n"
                  "|x2 = ", x2, "\n"
                  "|x3 = ", x3, "\n"
                  "|x1x2 = ", x1x2, "\n"
                  "|x1x3 = ", x1x3, "\n"
                  "|x2x3 = ", x2x3, "\n"
                  "|x1x2x3 = ", x1x2x3, "\n"
                  "|y1 = ", y1, "\n"
                  "|y2 = ", y2, "\n"
                  "|y3 = ", y3, "\n"
                  "|y4 = ", y4, "\n"         
                  "|y = ", Y_average, "\n"
                  "|s^2 = ", Disp_list, "\n")

            list_ai = [round(i, 5) for i in solve(list_for_solve_a, Y_average)]
            print("y = {} + {}*x1 + {}*x2 + {}*x3 + {}*x1x2 + {}*x1x3 + {}*x2x3 + {}*x1x2x3".format(list_ai[0],
                                                                                                    list_ai[1],
                                                                                                    list_ai[2],
                                                                                                    list_ai[3],
                                                                                                    list_ai[4],
                                                                                                    list_ai[5],
                                                                                                    list_ai[6],
                                                                                                    list_ai[7]))

            print("###################################################################################################################")

            Gp = max(Disp_list) / sum_dispersion
            F1 = m - 1
            N = len(y1)
            F2 = N
            q1 = 0.05 / F1
            fisher_value = f.ppf(q=1 - q1, dfn=F2, dfd=(F1 - 1) * F2)
            Gt = fisher_value / (fisher_value + F1 - 1)
            print("\nGp = ", Gp, " Gt = ", Gt)

        if Gp < Gt:
            print("_____Дисперсія однорідна!_____\n")

            Dispersion_B = sum_dispersion / N
            Dispersion_beta = Dispersion_B / (m * N)
            S_beta = math.sqrt(abs(Dispersion_beta))

            beta_list = [0, 0, 0, 0, 0, 0, 0, 0]
            for i in range(len(x0_factor)):
                beta_list[0] += (Y_average[i] * x0_factor[i]) / N
                beta_list[1] += (Y_average[i] * x1_factor[i]) / N
                beta_list[2] += (Y_average[i] * x2_factor[i]) / N
                beta_list[3] += (Y_average[i] * x3_factor[i]) / N
                beta_list[4] += (Y_average[i] * x1x2_factor[i]) / N
                beta_list[5] += (Y_average[i] * x1x3_factor[i]) / N
                beta_list[6] += (Y_average[i] * x2x3_factor[i]) / N
                beta_list[7] += (Y_average[i] * x1x2x3_factor[i]) / N
            t_list = [abs(beta_list[i])/S_beta for i in range(0, 8)]

            F3 = F1 * F2
            d = 0
            T = student_teor(df=F3)
            print("t_табличне = ", T)
            count_coef_znach = 0

            for i in range(len(t_list)):
                if T < t_list[i]:
                    beta_list[i] = 0
                    print("+++++ Гіпотеза підтверджена, beta{} = 0 +++++".format(i))
                    count_coef_znach += 1
                else:
                    print("----- Гіпотеза не підтверджена, beta{} = {} -----".format(i, beta_list[i]))
                    d += 1

            if count_coef_znach == 1:
                if m == 3:
                    m += 1
                    p = Lab4(m)
                    break
                elif m == 4:
                    print("Програма не розрахована для m = 5.")
                    break
            else:
                y_1 = beta_list[0] + beta_list[1] * x1[0] + beta_list[2] * x2[0] + beta_list[3] * x3[0] + beta_list[4] * \
                      x1x2[0] \
                      + beta_list[5] * x1x3[0] + beta_list[6] * x2x3[0] + beta_list[7] * x1x2x3[0]
                y_2 = beta_list[0] + beta_list[1] * x1[1] + beta_list[2] * x2[1] + beta_list[3] * x3[1] + beta_list[4] * \
                      x1x2[1] \
                      + beta_list[5] * x1x3[1] + beta_list[6] * x2x3[1] + beta_list[7] * x1x2x3[1]
                y_3 = beta_list[0] + beta_list[1] * x1[2] + beta_list[2] * x2[2] + beta_list[3] * x3[2] + beta_list[4] * \
                      x1x2[2] \
                      + beta_list[5] * x1x3[2] + beta_list[6] * x2x3[2] + beta_list[7] * x1x2x3[2]
                y_4 = beta_list[0] + beta_list[1] * x1[3] + beta_list[2] * x2[3] + beta_list[3] * x3[3] + beta_list[4] * \
                      x1x2[3] \
                      + beta_list[5] * x1x3[3] + beta_list[6] * x2x3[3] + beta_list[7] * x1x2x3[3]
                y_5 = beta_list[0] + beta_list[1] * x1[4] + beta_list[2] * x2[4] + beta_list[3] * x3[4] + beta_list[4] * \
                      x1x2[4] \
                      + beta_list[5] * x1x3[4] + beta_list[6] * x2x3[4] + beta_list[7] * x1x2x3[4]
                y_6 = beta_list[0] + beta_list[1] * x1[5] + beta_list[2] * x2[5] + beta_list[3] * x3[5] + beta_list[4] * \
                      x1x2[5] \
                      + beta_list[5] * x1x3[5] + beta_list[6] * x2x3[5] + beta_list[7] * x1x2x3[5]
                y_7 = beta_list[0] + beta_list[1] * x1[6] + beta_list[2] * x2[6] + beta_list[3] * x3[6] + beta_list[4] * \
                      x1x2[6] \
                      + beta_list[5] * x1x3[6] + beta_list[6] * x2x3[6] + beta_list[7] * x1x2x3[6]
                y_8 = beta_list[0] + beta_list[1] * x1[7] + beta_list[2] * x2[7] + beta_list[3] * x3[7] + beta_list[4] * \
                      x1x2[7] \
                      + beta_list[5] * x1x3[7] + beta_list[6] * x2x3[7] + beta_list[7] * x1x2x3[7]

                Y_counted_for_Student = [y_1, y_2, y_3, y_4, y_5, y_6, y_7, y_8]
                F4 = N - d
                Dispersion_ad = 0
                for i in range(len(Y_counted_for_Student)):
                    Dispersion_ad += ((Y_counted_for_Student[i] - Y_average[i]) ** 2) * m / (N - d)
                Fp = Dispersion_ad / Dispersion_beta
                Ft = fisher_teor(dfn=F4, dfd=F3)

                if Ft > Fp:
                    print("_____Рівняння регресії адекватне!_____")
                    break
                else:
                    print("_____Рівняння регресії неадекватне_____")
                    break

        else:
            print("!!!!! Дисперсія неоднорідна. Збільшуємо m, m = m + 1. І спробуємо знову !!!!!")
            m += 1

lab = Lab4(3)