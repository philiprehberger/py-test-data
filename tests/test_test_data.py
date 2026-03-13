from __future__ import annotations

import re
from datetime import date

import pytest

from philiprehberger_test_data import fake


class TestName:
    def test_name_contains_space(self) -> None:
        result = fake.name()
        assert isinstance(result, str)
        assert " " in result

    def test_first_name_is_string(self) -> None:
        result = fake.first_name()
        assert isinstance(result, str)
        assert len(result) > 0


class TestEmail:
    def test_email_contains_at_and_dot(self) -> None:
        result = fake.email()
        assert "@" in result
        assert "." in result


class TestInteger:
    def test_integer_within_range(self) -> None:
        low, high = 10, 20
        for _ in range(50):
            result = fake.integer(low, high)
            assert low <= result <= high


class TestChoice:
    def test_choice_returns_item_from_list(self) -> None:
        items = ["a", "b", "c"]
        result = fake.choice(items)
        assert result in items


class TestSentence:
    def test_sentence_ends_with_period(self) -> None:
        result = fake.sentence()
        assert result.endswith(".")


class TestUUID:
    def test_uuid_is_valid_format(self) -> None:
        result = fake.uuid()
        pattern = re.compile(
            r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
        )
        assert pattern.match(result)


class TestDate:
    def test_date_returns_date_in_range(self) -> None:
        result = fake.date(2020, 2022)
        assert isinstance(result, date)
        assert 2020 <= result.year <= 2022


class TestAddress:
    def test_address_contains_number(self) -> None:
        result = fake.address()
        assert any(c.isdigit() for c in result)


class TestPhone:
    def test_phone_starts_with_plus_one(self) -> None:
        result = fake.phone()
        assert result.startswith("+1")


class TestMany:
    def test_many_returns_correct_length(self) -> None:
        result = fake.many(fake.name, 7)
        assert isinstance(result, list)
        assert len(result) == 7


class TestSeed:
    def test_seed_produces_reproducible_output(self) -> None:
        fake.seed(12345)
        first_run = [fake.name() for _ in range(5)]
        fake.seed(12345)
        second_run = [fake.name() for _ in range(5)]
        assert first_run == second_run


class TestCompany:
    def test_company_returns_string(self) -> None:
        result = fake.company()
        assert isinstance(result, str)
        assert len(result) > 0


class TestIPAddress:
    def test_ip_address_has_four_octets(self) -> None:
        result = fake.ip_address()
        parts = result.split(".")
        assert len(parts) == 4
        for part in parts:
            assert 1 <= int(part) <= 254


class TestBoolean:
    def test_boolean_returns_bool(self) -> None:
        result = fake.boolean()
        assert isinstance(result, bool)
