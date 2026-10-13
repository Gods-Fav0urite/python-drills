def celsius_to_fahrenheit(celsius):
    return ((celsius * 1.8) + 32)

def fahrenheit_to_celsius(fahrenheit):
   return (fahrenheit - 32) * 5/9


def celsius_to_kelvin(celsius):
   return celsius + 273.15


def convert_temperature(value, from_unit, to_unit):
    if type(value) not in (int, float) or isinstance(value, bool):
        raise ValueError("Value must be a number.") 

    if not isinstance(from_unit, str) or not isinstance(to_unit, str):
        raise ValueError("Units must be strings.")

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    valid_units = {"celsius", "fahrenheit", "kelvin"}
    if from_unit not in valid_units or to_unit not in valid_units:
        raise ValueError("Unsupported temperature unit.")
    if from_unit == "celsius":
        celsius_value = value
    elif from_unit == "fahrenheit":
        celsius_value = fahrenheit_to_celsius(value)
    elif from_unit == "kelvin":
        celsius_value = value - 273.15

    if celsius_value < -273.15:
        raise ValueError("Temperature cannot be below absolute zero.")
    if to_unit == "celsius":
        return celsius_value
    elif to_unit == "fahrenheit":
        return celsius_to_fahrenheit(celsius_value)
    elif to_unit == "kelvin":
        return celsius_to_kelvin(celsius_value)
    