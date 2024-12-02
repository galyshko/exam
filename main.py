def arithmetic_progression_sum(n, a=1, d=4):
    if n < 0:
        raise ValueError("Кількість членів прогресії не може бути від'ємною.")
    summary = 0
    for i in range(n):
        summary += a + i * d
    print(f"Сума перших {n} членів прогресії: {summary}")


while True:
    try:
        n = int(input("Введіть кількість членів арифметичної прогресії (0 для виходу): "))

        if n == 0:
            print("Програма завершена.")
            break

        arithmetic_progression_sum(n)
    except ValueError as e:
        print(e)