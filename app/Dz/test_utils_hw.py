from utils import calculate_discount, is_even, get_full_name



def test_calculate_discount_20_percent() -> None:
    actual: float = calculate_discount(1000, 20)
    expected: float = 800
    assert actual == expected, "discount 20% failed"


def test_calculate_discount_50_percent() -> None:
    actual: float = calculate_discount(200, 50)
    expected: float = 100
    assert actual == expected, "discount 50% failed"


def test_calculate_discount_zero_percent() -> None:
    actual: float = calculate_discount(500, 0)
    expected: float = 500
    assert actual == expected, "discount 0% failed"


def test_calculate_discount_zero_price() -> None:
    actual: float = calculate_discount(0, 20)
    expected: float = 0
    assert actual == expected, "price 0 failed"


def test_calculate_discount_other_value() -> None:
    actual: float = calculate_discount(250, 10)
    expected: float = 225
    assert actual == expected, "discount 10% failed"


def test_is_even_positive_even() -> None:
    assert is_even(4) is True, "4 should be even"


def test_is_even_positive_odd() -> None:
    assert is_even(5) is False, "5 should be odd"


def test_is_even_negative_even() -> None:
    assert is_even(-8) is True, "-8 should be even"


def test_is_even_negative_odd() -> None:
    assert is_even(-7) is False, "-7 should be odd"


def test_is_even_zero() -> None:
    assert is_even(0) is True, "0 should be even"


def test_get_full_name_usual() -> None:
    actual: str = get_full_name("Taras", "Shevchenko")
    expected: str = "Taras Shevchenko"
    assert actual == expected, "usual name failed"


def test_get_full_name_short() -> None:
    actual: str = get_full_name("Al", "Li")
    expected: str = "Al Li"
    assert actual == expected, "short name failed"


def test_get_full_name_long() -> None:
    actual: str = get_full_name("Oleksandr", "Volodymyrovych")
    expected: str = "Oleksandr Volodymyrovych"
    assert actual == expected, "long name failed"


def test_get_full_name_single_chars() -> None:
    actual: str = get_full_name("A", "B")
    expected: str = "A B"
    assert actual == expected, "single chars failed"


def test_get_full_name_other_case() -> None:
    actual: str = get_full_name("Anna-Maria", "Kovalenko")
    expected: str = "Anna-Maria Kovalenko"
    assert actual == expected, "hyphen name failed"
