from unittest import TestCase, TestResult


class IntegrationTests(TestCase):
    def __init__(self):
        super().__init__()
        self.website = None

    def run(self, result: TestResult | None = ...) -> TestResult | None:
        with setup_test_website() as website:
            self.website = website
            return super().run(result)
