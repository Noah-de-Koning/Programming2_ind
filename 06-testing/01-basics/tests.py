from intervals import overlapping_intervals


def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (3, 6))
    assert overlapping_intervals((3, 8), (8, 12))
    assert overlapping_intervals((3, 3), (1, 5))
    assert not overlapping_intervals((2, 5), (7, 10))
    assert not overlapping_intervals((4, 0), (1, 3))
