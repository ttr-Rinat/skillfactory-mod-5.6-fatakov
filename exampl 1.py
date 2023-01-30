print('Добро пожаловать в игру крестики нолики. Игра предназначена для двоих игроков. Нашли соперника? Тогда начнём!!!')
Gamer1 = input("Введите имя игрока играющего х ")
Gamer2 = input("Введите имя игрока играющего о ")
matrix = [[' '] * 3 for i in range(3)]
matrix1 = [['x']*3 for i in range (3)]
matrix2 = [['o']*3 for i in range (3)]
while True:
    print('  0 1 2 ')
    print('0', *matrix[0])
    print('1', *matrix[1])
    print('2', *matrix[2])
    print(Gamer1, 'Ваш ход')


    def fhod1v():  # начало ходов
        hod1v = int(input("Цифра по вертикали"))
        return hod1v


    def fhod1g():
        hod1g = int(input("Цифра по горизонтали"))
        return hod1g


    while True:
        matrix[fhod1v()][fhod1g()] = 'x'
        break
    for i in matrix:
        break
    print('+ 0 1 2 ')
    print('0', *matrix[0])
    print('1', *matrix[1])
    print('2', *matrix[2])

    print(Gamer2, 'Ваш ход')


    def fhod2v():
        hod2v = int(input("Цифра по вертикали"))
        return hod2v


    def fhod2g():
        hod2g = int(input("Цифра по горизонтали"))
        return hod2g


    while True:
        matrix[fhod2v()][fhod2g()] = 'o'
        break
    for j in matrix:
        break
    print('+ 0 1 2 ')
    print('0', *matrix[0])
    print('1', *matrix[1])
    print('2', *matrix[2])
    print(Gamer1, 'Ваш ход')  # конец ходов

    a = bool(matrix[0] == matrix1[0])  # 0 строка
    b = bool(matrix[0] == matrix2[0])
    c = bool(matrix[1] == matrix1[1])  # 1 строка
    d = bool(matrix[1] == matrix2[1])
    e = bool(matrix[2] == matrix1[2])  # 2 строка
    f = bool(matrix[2] == matrix2[2])
    g = bool(matrix[0][0] and matrix[0][1] and matrix[0][2] == matrix1[0][0] and matrix1[0][1] and matrix1[0][
        2])  # 0 столбик
    k = bool(matrix[0][0] and matrix[0][1] and matrix[0][2] == matrix2[0][0] and matrix2[0][1] and matrix2[0][2])
    l = bool(matrix[1][0] and matrix[1][1] and matrix[1][2] == matrix1[1][0] and matrix1[1][1] and matrix1[1][
        2])  # 1 столбик
    m = bool(matrix[1][0] and matrix[1][1] and matrix[1][2] == matrix2[1][0] and matrix2[1][1] and matrix2[1][2])
    n = bool(matrix[2][0] and matrix[2][1] and matrix[2][2] == matrix1[2][0] and matrix1[2][1] and matrix1[2][
        2])  # 2 столбик
    o = bool(matrix[2][0] and matrix[2][1] and matrix[2][2] == matrix2[2][0] and matrix2[2][1] and matrix2[2][2])
    p = bool(matrix[0][0] and matrix[1][1] and matrix[2][2] == matrix1[0][0] and matrix1[1][1] and matrix1[2][
        2])  # диагональ
    q = bool(matrix[0][0] and matrix[1][1] and matrix[2][2] == matrix2[0][0] and matrix2[1][1] and matrix2[2][2])
    r = bool(matrix[0][2] and matrix[1][1] and matrix[2][0] == matrix1[0][2] and matrix1[1][1] and matrix1[2][
        0])  # диагональ /
    s = bool(matrix[0][2] and matrix[1][1] and matrix[2][0] == matrix2[0][2] and matrix2[1][1] and matrix2[2][0])

    while True:  # условия победы
        bool(a or b or c or d or e or f or g or k or l or m or n or o or p or q or r or s)
        print("ПОБЕДА!!!")
        break
