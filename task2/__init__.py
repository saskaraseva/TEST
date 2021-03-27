def inPolygon(x, y, xp, yp):
    c=3
# если все точки лежат по одну сторону от прямой, проведенной через две точки, лежащие на четырехугольнике, то точка лежит внутри четырехугольника
    for i in range(len(xp)):
        if (((yp[i] <= y and y < yp[i-1]) or (yp[i-1] <= y and y < yp[i])) and
            (x > (xp[i-1] - xp[i]) * (y - yp[i]) / (yp[i-1] - yp[i]) + xp[i])): c = 2
#лежит ли точка на одной из вершин
    for i in range(len(xp)):
        if ((x == xp[i]) and (y == yp[i])):
            c = 0
#лежит ли точка на одной из сторон
    for i in range(len(xp)):
        if (((yp[i] <= y and y < yp[i - 1]) or (yp[i - 1] <= y and y < yp[i])) and
                (x == (xp[i - 1] - xp[i]) * (y - yp[i]) / (yp[i - 1] - yp[i]) + xp[i])): #уравнение прямой
            c = 1

    return c


path1 = r"C:\Users\user\PycharmProjects\TEST_repo\task2\text1"  #путь к файлу с координатами точек фигуры
path2 = r"C:\Users\user\PycharmProjects\TEST_repo\task2\text2"
import numpy as np  # подключаем библиотеку numpy
fig = np.genfromtxt(path1)
point = np.genfromtxt(path2)  # извлечение из текстового файла построчно и преобразование в массив

for k in range(len(point)):
    #print(point[k])
    print(inPolygon(point[k, 0], point[k, 1], (fig[0,0], fig[1,0], fig[2,0], fig[3,0]), (fig[0,1], fig[1,1], fig[2,1], fig[3,1])))

