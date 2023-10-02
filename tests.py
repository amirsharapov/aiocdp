from unittest import TestLoader, TextTestRunner

from dotenv import load_dotenv


def run_integration_tests():
    test_loader = TestLoader()
    test_suite = test_loader.discover('tests')

    test_runner = TextTestRunner()
    test_runner.run(test_suite)


if __name__ == '__main__':
    load_dotenv('.env.test')
    run_integration_tests()
