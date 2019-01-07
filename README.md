# philiprehberger-test-data

Generate realistic fake data for testing without external dependencies.

## Install

```bash
pip install philiprehberger-test-data
```

## Usage

```python
from philiprehberger_test_data import fake

# Basic generators
fake.name()          # "Alice Johnson"
fake.email()         # "bob.smith@example.com"
fake.integer(1, 100) # 42
fake.boolean()       # True
fake.uuid()          # "a1b2c3d4-..."

# Seed for reproducible output
fake.seed(42)
fake.name()  # always the same name with seed 42

# Bulk generation
fake.many(fake.name, 5)   # ["Alice Smith", "Bob Jones", ...]
fake.many(fake.integer, 3, 1, 100)  # [42, 87, 13]
```

## API

| Method | Description |
| --- | --- |
| `fake.seed(value)` | Set random seed for reproducible output |
| `fake.name()` | Full name (first + last) |
| `fake.first_name()` | First name |
| `fake.last_name()` | Last name |
| `fake.email()` | Email address |
| `fake.integer(low, high)` | Random integer in [low, high] |
| `fake.floating(low, high)` | Random float in [low, high] |
| `fake.boolean()` | Random boolean |
| `fake.choice(items)` | Random item from list |
| `fake.sentence(words)` | Random sentence |
| `fake.paragraph(sentences)` | Random paragraph |
| `fake.uuid()` | UUID4 string |
| `fake.date(start_year, end_year)` | Random date |
| `fake.datetime_(start_year, end_year)` | Random datetime |
| `fake.address()` | Street address |
| `fake.full_address()` | Full address with city, state, ZIP |
| `fake.phone()` | Phone number |
| `fake.company()` | Company name |
| `fake.hex_color()` | Hex color code |
| `fake.ip_address()` | IPv4 address |
| `fake.url()` | URL |
| `fake.many(generator, count, *args, **kwargs)` | List of N generated values |

## License

MIT
