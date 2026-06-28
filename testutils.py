from utils import format_name
from utils import calculate_age
from utils import clamp
from utils import percentage
from utils import slugify

from datetime import date

assert format_name("alice", "smith") == "Smith, Alice"

assert calculate_age(date.today().year - 20) == 20

assert clamp(150, 0, 100) == 100

assert clamp(-10, 0, 100) == 0

assert percentage(1, 4) == 25.0

assert slugify("Hello World!") == "hello-world"

print("All Tests Passed")