path = r"C:\Users\user\PycharmProjects\TEST_repo\task1\text"

def stats(path):
    f = open(path)  #открываем файл
    import numpy as np  # подключаем библиотеку numpy
    k = np.genfromtxt(path)  # извлечение из текстового файла построчно и преобразование в массив
    perc = np.percentile(k, 90)  # рассчитвываем перцентиль 90
    median = np.median(k)  # рассчитываем медиану
    maximum = np.amax(k)  # поиск максимума
    minimum = np.amin(k)  # поиск минимума
    average = np.mean(k)  # поиск среднего арифметического
    print(format(perc, '.2f'))
    print(format(median, '.2f'))
    print(format(maximum, '.2f'))
    print(format(minimum, '.2f'))
    print(format(average, '.2f'))

stats(path)