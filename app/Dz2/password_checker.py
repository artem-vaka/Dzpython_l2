def is_strong_password(password: str) -> bool:

    if len(password) < 8:
        return False

    if any(char.isspace() for char in password):
        return False

    has_digit = any(char.isdigit() for char in password)
    has_letter = any(char.isalpha() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    return has_digit and has_letter and has_symbol