"""
Ввести с клавиатуры целое число n.
Получить сумму кубов всех целых чисел от 1 до n(включая n).
Исключения составляют все числа кратные цифре 3.
Использовать цикл while
"""

while True:
    n = input('Ввести с клавиатуры целое число n: ')
    if not n.isdigit():
        continue
    else:
        n1 = int(n)
        res = 0
        counter = 0
        while counter < n1:
            counter += 1
            if counter % 3 != 0:
                res += counter ** 3
                print('Res on each step: ', res)
        print('Final sum: ', res)
    break


