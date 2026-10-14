def has_min_length(password):
   return len(password) >= 8


def has_uppercase(password):
    return any(char.isupper() for char in password)


def has_lowercase(password):
    return any(char.islower() for char in password)


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_special(password):
    return any(not char.isalnum() and not char.isspace() for char in password)


def is_valid_password(password):
    return all([
        has_min_length(password),
        has_uppercase(password),
        has_lowercase(password),
        has_digit(password),
        has_special(password)
    ])


# bonus
def get_failed_requirements(password):
    results = [
        ("min_length", has_min_length(password)),
        ("uppercase", has_uppercase(password)),
        ("lowercase", has_lowercase(password)),
        ("digit", has_digit(password)),
        ("special", has_special(password))
    ]
    return[name for name, passed in results if not passed]