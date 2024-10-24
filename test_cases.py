import time
import unittest
from unittest import mock
import sum_digits


class MainTest(unittest.TestCase):

    # Обычный ввод
    def test_usual(self):
        with mock.patch('builtins.input', side_effect=['653', '32', '99', '0']):
            self.assertEqual(sum_digits.main_func(), 99)

    # Обычный ввод #2
    def test_usual2(self):
        with mock.patch('builtins.input', side_effect=['654', '1234', '99', '0']):
            self.assertEqual(sum_digits.main_func(), 99)

    # Ввод одних и тех же чисел
    def test_same_digits(self):
        with mock.patch('builtins.input', side_effect=['1', '1', '1', '1', '1', '0']):
            self.assertEqual(sum_digits.main_func(), 1)

    # Ввод нуля
    def test_zero_only(self):
        with mock.patch('builtins.input', side_effect=['0']):
            self.assertEqual(sum_digits.main_func(), None)

    # Ввод отрицательных чисел
    def test_negative_num(self):
        with mock.patch('builtins.input', side_effect=['-12', '-13', '0']):
            self.assertEqual(sum_digits.main_func(), -13)

    # Ввод отрицательных чисел #2
    def test_negative_num2(self):
        with mock.patch('builtins.input', side_effect=['-12', '-13', '1', '30', '0']):
            self.assertEqual(sum_digits.main_func(), 30)

    # Невалидный ввод (дробные числа)
    def test_invalid_input(self):
        with mock.patch('builtins.input', side_effect=['31', '31.2', '65', '777754.321', '0']):
            self.assertEqual(sum_digits.main_func(), 65)

    # Невалидный ввод (строка)
    def test_invalid_input2(self):
        with mock.patch('builtins.input', side_effect=['invalid_input']):
            self.assertRaises(StopIteration)

    # Невалидный ввод (булевая переменная)
    def test_invalid_input3(self):
        with mock.patch('builtins.input', side_effect=[True]):
            self.assertRaises(StopIteration)

    # Невалидный ввод (число)
    def test_invalid_input4(self):
        with mock.patch('builtins.input', side_effect=[0]):
            self.assertRaises(StopIteration)

    # Невалидный ввод (дробное число)
    def test_invalid_input5(self):
        with mock.patch('builtins.input', side_effect=[0.6]):
            self.assertRaises(StopIteration)

    # Незаконченный ввод (без '0' в конце)
    def test_nonstop_input(self):
        with mock.patch('builtins.input', side_effect=['1', '2', '3', '4']):
            self.assertRaises(StopIteration)

    # Подождать 5 секунд
    @classmethod
    def tearDownClass(cls):
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
