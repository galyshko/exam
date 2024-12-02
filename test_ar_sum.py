import unittest


def arithmetic_progression_sum(n, a=1, d=4):
    if n < 0:
        raise ValueError("Кількість членів прогресії не може бути від'ємною.")
    summary = 0
    for i in range(n):
        summary += a + i * d
    return summary

class TestArithmeticProgressionSum(unittest.TestCase):
    @unittest.expectedFailure
    def test_default_values(self):
        self.assertEqual(arithmetic_progression_sum(5), 35)  # 1 + 5 + 9 + 13 + 17 = 35

    def test_custom_values(self):
        self.assertEqual(arithmetic_progression_sum(3, a=2, d=3), 10)  # 2 + 5 + 8 = 15

    def test_one_term(self):
        self.assertEqual(arithmetic_progression_sum(0), 0)

    def test_negative_n(self):
        # Перевірка на негативне значення n
        with self.assertRaises(ValueError):
            arithmetic_progression_sum(-1)
if __name__ == '__main__':
    unittest.main()
