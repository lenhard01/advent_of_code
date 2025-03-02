import solution


def test_part1():
    sample_input = "1\n2\n3"
    data = solution.parse_input(sample_input)
    # Expected output based on the sample logic in part1()
    assert solution.part1(data) == 6


def test_part2():
    sample_input = "1\n2\n3"
    data = solution.parse_input(sample_input)
    # Expected output based on the sample logic in part2()
    assert solution.part2(data) == 12
