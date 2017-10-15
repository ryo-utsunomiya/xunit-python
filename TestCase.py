class TestCase(object):
    def __init__(self, name):
        self.name = name

    def set_up(self):
        pass

    def run(self, result):
        result.test_started()
        self.set_up()
        # noinspection PyBroadException
        try:
            method = getattr(self, self.name)
            method()
        except Exception:
            result.test_failed()
        self.tear_down()

    def tear_down(self):
        pass


class WasRun(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.log = ""

    def set_up(self):
        self.log += "set_up "

    def test_method(self):
        self.log += "test_method "

    def test_broken_method(self):
        raise Exception

    def tear_down(self):
        self.log += "tear_down "
