while True:
    def atm_simulation():
        # Initial Bank and ATM State
        balance = 2490
        
        # Dictionary storing available bills in the ATM
        atm_bills = {
            100: 50,
            50: 20,
            20: 300,
            10: 0,
            5: 200,
            1: 10
        }
        
        try:
            amount = int(input("Please input your withdraw amount: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer amount.")
            return

        # Validation checks
        if amount <= 0:
            print("Error: Withdrawal amount must be greater than 0.")
            return
        if amount > balance:
            print("Transaction Failed: Insufficient funds in your bank account.")
            return

        # Calculate required bills using a greedy approach
        withdrawal_breakdown = {}
        remaining_amount = amount

        for cash in [100, 50, 20, 10, 5, 1]:
            if remaining_amount <= 0:
                break
            
            # Determine how many bills of this denomination we need
            needed = remaining_amount // cash
            
            # Check how many are actually available in the ATM machine
            available = atm_bills[cash]
            use_count = min(needed, available)
            
            if use_count > 0:
                withdrawal_breakdown[cash] = use_count
                remaining_amount -= use_count * cash

        # Check if the ATM has enough physical bills to fulfill the request
        if remaining_amount > 0:
            print("Transaction Failed: The ATM does not have enough cash bills to dispense this exact amount.")
            return

        # Update ATM inventory and user balance
        balance -= amount
        for denom, count in withdrawal_breakdown.items():
            atm_bills[denom] -= count

        # Output Scene Matching Console Format
        print("Transaction Successful!")
        print(f"You have received ${amount}")
        for denom, count in withdrawal_breakdown.items():
            print(f"{count} of ${denom} bill")
            
        print(f"Your remaining balance: ${balance}")
        print("Remaining in this machine:")
        print(f"$100: {atm_bills[100]}")
        print(f"$50: {atm_bills[50]}")
        print(f"$20 bill cash: {atm_bills[20]}")
        print(f"$10 bill cash: {atm_bills[10]}")
        print(f"$5 bill cash: {atm_bills[5]}")
        print(f"$1 bill cash: {atm_bills[1]}")

    # Run the simulation
    if __name__ == "__main__":
        atm_simulation()