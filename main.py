import unittest
import datetime


class TestGetUserInput(unittest.TestCase):

    def test_stock_symbol(get_user_input):
        stock_symbol = 'AAPY'
        get_user_input.assertLessEqual(len(stock_symbol), 7, msg="The ticker is more than 7 characters")
        get_user_input.assertGreaterEqual(len(stock_symbol), 1, msg="The ticker is less than one character")
        get_user_input.assertTrue(stock_symbol.isupper(), msg="The ticker is lowercase")

    def test_chart_type(get_user_input):
        get_user_input.assertLessEqual(1, 2)
        get_user_input.assertGreaterEqual(1, 1)
        get_user_input.assertTrue(type(1) == int)

    def test_time_series(get_user_input):
        time_series = 1
        get_user_input.assertLessEqual(time_series, 4)
        get_user_input.assertGreaterEqual(time_series, 1)
        get_user_input.assertTrue(type(time_series) == int)

    def test_start_date(get_user_input):
        start_date = datetime.datetime.strptime("2009-02-27", "%Y-%m-%d").date()
        test_date = datetime.date
        get_user_input.assertIsInstance(start_date, test_date)

    def test_end_date(get_user_input):
        end_date = datetime.datetime.strptime("2009-02-27", "%Y-%m-%d").date()
        test_date = datetime.date
        get_user_input.assertIsInstance(end_date, test_date)


if __name__ == '__main__':
    unittest.main()