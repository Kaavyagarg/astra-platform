def convert_age(age):
    try:
        return int(age)
    except ValueError:
        return None