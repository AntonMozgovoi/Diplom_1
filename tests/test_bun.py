from bun import Bun


class TestNamePriceBun:
    def test_name_bun(self):
        bun = Bun("Whole Wheat", 3.00)
        assert bun.get_name() == "Whole Wheat"
        assert bun.get_price() == 3.00