from datetime import date
import re

def format_name(first, last):
    return f"{last.title()}, {first.title()}"

def calculate_age(birth_year):
    return date.today().year - birth_year

def clamp(value, min_val, max_val):
    return max(min_val, min(value, max_val))

def percentage(part, whole):
    if whole == 0:
        return 0.0
    return round((part / whole) * 100, 2)

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    return text
