import pytest
from lesson_9_2 import Students


@pytest.fixture(scope='class')
def student():
    return Students(surname='Shmel', group_number=2, estimates=[3, 2, 3, 2, 3])


class TestStudent:

    def test_surname(self, student):
        assert student.surname == 'Shmel'

    def test_group(self, student):
        assert student.group_number == 3

    def test_estimates(self, student):
        assert student.estimates == [3, 2, 3, 2, 3]


if __name__ == "__main__":
    pytest.main()
