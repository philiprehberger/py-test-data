"""Generate realistic fake data for testing without external dependencies."""

from __future__ import annotations

import random
import string
import uuid as _uuid
from collections.abc import Callable
from datetime import date, datetime, timedelta
from typing import Any, TypeVar

__all__ = ["fake"]

T = TypeVar("T")

_FIRST_NAMES = [
    "Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry",
    "Ivy", "Jack", "Kate", "Leo", "Mia", "Noah", "Olivia", "Paul",
    "Quinn", "Ruby", "Sam", "Tara", "Uma", "Vince", "Wendy", "Xander",
    "Yara", "Zane",
]

_LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller",
    "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez",
    "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark",
    "Ramirez", "Lewis", "Robinson",
]

_STREET_NAMES = [
    "Main", "Oak", "Maple", "Cedar", "Pine", "Elm", "Washington",
    "Park", "Lake", "Hill", "Sunset", "River", "Spring", "Forest",
    "Valley", "Meadow", "Highland", "Church", "Bridge", "Mill",
]

_STREET_SUFFIXES = ["St", "Ave", "Blvd", "Dr", "Ln", "Ct", "Way", "Rd", "Pl"]

_CITIES = [
    "Springfield", "Portland", "Franklin", "Clinton", "Madison",
    "Georgetown", "Arlington", "Salem", "Fairview", "Chester",
    "Bristol", "Oxford", "Burlington", "Manchester", "Milton",
]

_STATES = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY",
]

_DOMAINS = ["example.com", "test.org", "mail.net", "demo.io", "sample.dev"]

_WORDS = [
    "the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog",
    "a", "bright", "red", "sun", "sets", "behind", "tall", "mountains",
    "in", "warm", "summer", "breeze", "carries", "sweet", "scent", "of",
    "fresh", "flowers", "through", "open", "window", "into", "quiet", "room",
]

_COMPANY_SUFFIXES = ["Inc", "LLC", "Corp", "Co", "Ltd", "Group", "Solutions"]


class _Fake:
    """Fake data generator."""

    def __init__(self, seed: int | None = None) -> None:
        self._rng = random.Random(seed)

    def seed(self, value: int) -> None:
        """Set the random seed for reproducible output."""
        self._rng.seed(value)

    def name(self) -> str:
        """Generate a full name."""
        return f"{self._rng.choice(_FIRST_NAMES)} {self._rng.choice(_LAST_NAMES)}"

    def first_name(self) -> str:
        """Generate a first name."""
        return self._rng.choice(_FIRST_NAMES)

    def last_name(self) -> str:
        """Generate a last name."""
        return self._rng.choice(_LAST_NAMES)

    def email(self) -> str:
        """Generate an email address."""
        first = self._rng.choice(_FIRST_NAMES).lower()
        last = self._rng.choice(_LAST_NAMES).lower()
        domain = self._rng.choice(_DOMAINS)
        return f"{first}.{last}@{domain}"

    def integer(self, low: int = 0, high: int = 1000) -> int:
        """Generate a random integer in [low, high]."""
        return self._rng.randint(low, high)

    def floating(self, low: float = 0.0, high: float = 1.0) -> float:
        """Generate a random float in [low, high]."""
        return self._rng.uniform(low, high)

    def boolean(self) -> bool:
        """Generate a random boolean."""
        return self._rng.choice([True, False])

    def choice(self, items: list[T]) -> T:
        """Pick a random item from a list."""
        return self._rng.choice(items)

    def sentence(self, words: int = 8) -> str:
        """Generate a sentence of random words."""
        selected = [self._rng.choice(_WORDS) for _ in range(words)]
        selected[0] = selected[0].capitalize()
        return " ".join(selected) + "."

    def paragraph(self, sentences: int = 4) -> str:
        """Generate a paragraph of random sentences."""
        return " ".join(self.sentence() for _ in range(sentences))

    def uuid(self) -> str:
        """Generate a UUID4 string."""
        return str(_uuid.UUID(int=self._rng.getrandbits(128), version=4))

    def date(self, start_year: int = 2000, end_year: int = 2026) -> date:
        """Generate a random date."""
        start = datetime(start_year, 1, 1)
        end = datetime(end_year, 12, 31)
        delta = (end - start).days
        return (start + timedelta(days=self._rng.randint(0, delta))).date()

    def datetime_(self, start_year: int = 2000, end_year: int = 2026) -> datetime:
        """Generate a random datetime."""
        d = self.date(start_year, end_year)
        return datetime(
            d.year, d.month, d.day,
            self._rng.randint(0, 23),
            self._rng.randint(0, 59),
            self._rng.randint(0, 59),
        )

    def address(self) -> str:
        """Generate a street address."""
        number = self._rng.randint(1, 9999)
        street = self._rng.choice(_STREET_NAMES)
        suffix = self._rng.choice(_STREET_SUFFIXES)
        return f"{number} {street} {suffix}"

    def full_address(self) -> str:
        """Generate a full address with city, state, and ZIP."""
        city = self._rng.choice(_CITIES)
        state = self._rng.choice(_STATES)
        zip_code = str(self._rng.randint(10000, 99999))
        return f"{self.address()}, {city}, {state} {zip_code}"

    def phone(self) -> str:
        """Generate a phone number."""
        area = self._rng.randint(200, 999)
        prefix = self._rng.randint(200, 999)
        line = self._rng.randint(1000, 9999)
        return f"+1-{area}-{prefix}-{line}"

    def company(self) -> str:
        """Generate a company name."""
        last = self._rng.choice(_LAST_NAMES)
        suffix = self._rng.choice(_COMPANY_SUFFIXES)
        return f"{last} {suffix}"

    def hex_color(self) -> str:
        """Generate a hex color code."""
        return "#{:06x}".format(self._rng.randint(0, 0xFFFFFF))

    def ip_address(self) -> str:
        """Generate an IPv4 address."""
        return ".".join(str(self._rng.randint(1, 254)) for _ in range(4))

    def url(self) -> str:
        """Generate a URL."""
        domain = self._rng.choice(_DOMAINS)
        path = "".join(self._rng.choices(string.ascii_lowercase, k=8))
        return f"https://{domain}/{path}"

    def many(self, generator: Callable[..., T], count: int, *args: Any, **kwargs: Any) -> list[T]:
        """Generate a list of N values from any generator method."""
        return [generator(*args, **kwargs) for _ in range(count)]


fake = _Fake()
