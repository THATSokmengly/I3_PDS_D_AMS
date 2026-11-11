
# Problem 9: Electricity Bill with Progressive Tiers

# (a) Create a function to calculate the electricity bill

def electricity_bill(kwh):

    # Check negative input
    if kwh < 0:
        return None

    # Tier 1: First 50 kWh
    tier1 = min(kwh, 50) * 480

    # Tier 2: Next 150 kWh
    tier2 = min(max(kwh - 50, 0), 150) * 610

    # Tier 3: Above 200 kWh
    tier3 = max(kwh - 200, 0) * 730

    # Calculate total electricity cost
    total = tier1 + tier2 + tier3

    # Add service fee
    total = total + 2000

    # Add 10% VAT
    total = total * 1.10

    # Return a whole number
    return round(total)


# (b) Print a table for different consumption values

print("ELECTRICITY BILL")
print("-" * 50)

consumptions = [0, 35, 50, 120, 200, 350]

for kwh in consumptions:

    bill = electricity_bill(kwh)

    # Convert Riel to USD
    usd = bill / 4100

    print(f"{kwh:3} kWh -> {bill:10,} riel (= {usd:.2f} USD)")


# (c) Ask the user for monthly consumption

print("\nMONTHLY ELECTRICITY BILL")

try:
    kwh = float(input("Enter your monthly consumption (kWh): "))

    bill = electricity_bill(kwh)

    if bill is None:
        print("Error: Consumption cannot be negative.")

    else:
        usd = bill / 4100

        print("Your electricity bill is:", f"{bill:,}", "riel")
        print("Your electricity bill in USD:", f"{usd:.2f}", "USD")

except ValueError:
    print("Please enter a valid number.")