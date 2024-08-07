import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "penny, result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ],
    ids=[
        "1 cent: 1 penny",
        "6 cents: 1 penny + 1 nickel",
        "17 cents: 2 pennies + 1 nickel + 1 dime",
        "50 cents: 2 quarters",
    ]
)
def test_should_return_result(
    penny: int, result: list[int]
) -> None:
    assert get_coin_combination(penny) == result
