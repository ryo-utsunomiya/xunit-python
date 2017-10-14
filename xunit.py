class TestCase:
    def __init__(self, name):
        self.name = name

    def set_up(self):
        pass

    def run(self):
        self.set_up()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.was_run = False
        self.was_set_up = False

    def set_up(self):
        self.was_set_up = True

    def test_method(self):
        self.was_run = True


class TestCaseTest(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.test = None

    def set_up(self):
        self.test = WasRun("test_method")

    def test_running(self):
        self.test.run()
        assert self.test.was_run

    def test_set_up(self):
        self.test.run()
        assert self.test.was_set_up


TestCaseTest("test_running").run()
TestCaseTest("test_set_up").run()
