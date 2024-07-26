from seasons import calc_diff
from datetime import date

def test_calc_diff():
    assert calc_diff(10477) == "Fifteen million, eighty-six thousand, eight hundred eighty minutes"
