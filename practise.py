



test_data = [
    (2, 3, 6),
    (99, 1, 99),
    (0, 10, 0),
    (-5, 1, -5),
    (-5, -2, 10)
]


@pytest.mark.parametrize("num_1, num_2, result", test_data)
def test_multiplication(num_1, num_2, result):
    assert num_1 * num_2 == result