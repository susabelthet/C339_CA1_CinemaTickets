import pytest

from src.cinema_entry import can_watch


# ---------- Allowed (Requirement 3.2.1: aged 16 or older may watch) ----------

@pytest.mark.parametrize("age", [
    16,    # boundary: exactly 16 must be allowed
    17,    # just above the boundary
    30,    # typical adult
    100,   # large value
])
def test_age_16_or_older_returns_true(age):
    # Arrange: age comes from the parametrize data

    # Act
    result = can_watch(age)

    # Assert
    assert result is True


# ---------- Not allowed (Requirement 3.2.2: below 16 may not watch) ----------

@pytest.mark.parametrize("age", [
    0,     # lowest valid age
    1,     # just above the lowest valid age
    10,    # typical child
    15,    # just below the boundary
])
def test_age_below_16_returns_false(age):
    # Arrange: age comes from the parametrize data

    # Act
    result = can_watch(age)

    # Assert
    assert result is False


# ---------- Invalid data type (General Requirements 2 and 3: raise TypeError) ----------

@pytest.mark.parametrize("age", [
    "16",    # string
    16.0,    # float
    True,    # bool is not a valid int
    False,   # bool is not a valid int
    None,    # missing value
    [16],    # list
])
def test_non_int_age_raises_type_error(age):
    # Arrange: age comes from the parametrize data

    # Act and Assert
    with pytest.raises(TypeError):
        can_watch(age)


# ---------- Out of range (General Requirement 4: raise ValueError) ----------

@pytest.mark.parametrize("age", [
    -1,    # just below the lowest valid age (0)
    -20,   # typical negative value
])
def test_negative_age_raises_value_error(age):
    # Arrange: age comes from the parametrize data

    # Act and Assert
    with pytest.raises(ValueError):
        can_watch(age)
