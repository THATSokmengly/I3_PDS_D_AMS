# Temperature conversion program
# Parameters: celsius (float) 
def celsius_to_fahrenheit(celsius, round_to = 1):
    fahrenheit = (celsius *  9/5) + 32
    return fahrenheit
celsius_to_fahrenheit(0)
print(celsius_to_fahrenheit(43), "F")

def fahrenheit_to_celsius(fahrenheit, round_to = 1):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
fahrenheit_to_celsius(0)
print(fahrenheit_to_celsius(109.4), "C")

# Table output for celsius to fahrenheit

# loop (0, 100, 20) mean start from 0 to 100 with step 20
# ---------------------------------------------------------------------------
# Problem 3 (Easy) · Temperature converter
# ---------------------------------------------------------------------------
def celsius_to_fahrenheit(c, round_to=1):
    """Convert degrees Celsius to degrees Fahrenheit."""
    return round(c * 9 / 5 + 32, round_to)


def fahrenheit_to_celsius(f, round_to=1):
    """Convert degrees Fahrenheit to degrees Celsius."""
    return round((f - 32) * 5 / 9, round_to)


print("\n  °C  |   °F")
print("------+-------")
for c in range(0, 101, 20):
    print(f"{c:5} | {celsius_to_fahrenheit(c):6}")
    # C: 

print("98.6 °F =", fahrenheit_to_celsius(98.6), "°C")
print("Round trip 37 °C:", fahrenheit_to_celsius(celsius_to_fahrenheit(37)))

print(fahrenheit_to_celsius(200, round_to=3))


