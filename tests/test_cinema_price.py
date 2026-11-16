import pytest

from src.cinema_price import ticket_price


# ---------- Valid inputs (Requirement 3.1.1: each ticket costs 1200 cents) ----------

@pytest.mark.parametrize("ticket_count, expected_total", [
    (1, 1200),      # lower boundary of positive counts
    (2, 2400),      # just above the lower boundary
    (5, 6000),      # typical value
    (100, 120000),  # large value
])
def test_valid_ticket_count_returns_count_times_1200(ticket_count, expected_total):
    # Arrange: ticket_count and expected_total come from the parametrize data

    # Act
    result = ticket_price(ticket_count)

    # Assert
    assert result == expected_total


def test_zero_tickets_returns_zero():
    # Requirement 3.1.2: zero tickets costs zero
    # Arrange
    ticket_count = 0

    # Act
    result = ticket_price(ticket_count)

    # Assert
    assert result == 0


def test_valid_ticket_count_returns_int():
    # Output: total price is returned as an integer in cents
    # Arrange
    ticket_count = 3

    # Act
    result = ticket_price(ticket_count)

    # Assert
    assert type(result) is int


# ---------- Invalid data type (General Requirements 2 and 3: raise TypeError) ----------

@pytest.mark.parametrize("ticket_count", [
    "2",     # string
    2.0,     # float
    True,    # bool is not a valid int
    False,   # bool is not a valid int
    None,    # missing value
    [2],     # list
])
def test_non_int_ticket_count_raises_type_error(ticket_count):
    # Arrange: ticket_count comes from the parametrize data

    # Act and Assert
    with pytest.raises(TypeError):
        ticket_price(ticket_count)


# ---------- Out of range (General Requirement 4: raise ValueError) ----------

@pytest.mark.parametrize("ticket_count", [
    -1,    # just below the lower boundary (0)
    -10,   # typical negative value
])
def test_negative_ticket_count_raises_value_error(ticket_count):
    # Arrange: ticket_count comes from the parametrize data

    # Act and Assert
    with pytest.raises(ValueError):
        ticket_price(ticket_count)
