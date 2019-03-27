from pytest import mark

@mark.body
@mark.tires
class TiresTests:

    def test_lifetime(self):
        assert True

    def test_gap(self):
        assert True

    def test_rain(self):
        assert True
