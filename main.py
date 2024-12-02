n = int(input("Введіть кількість членів арифметичної прогресії: "))


def arithmetic_progression_sum(n, a=1, d=4):
    if n < 0:
        raise ValueError("Кількість членів прогресії не може бути від'ємною.")
    summary = 0
    for i in range(n):
        summary += a + i * d
    print(f"Сума перших {n} членів прогресії: {summary}")

arithmetic_progression_sum(n)