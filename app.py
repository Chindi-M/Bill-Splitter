def share_bill():
    try:
        bill = float(input("How much is the bill? £"))
        if bill <= 0:
            raise ValueError("Bill amount must be positive")
            
        tip_percentage = float(input("What percentage would you like to tip? "))
        if tip_percentage < 0:
            raise ValueError("Tip percentage cannot be negative")
            
        tip = (tip_percentage / 100) * bill
        
        people = int(input("How many people are sharing this bill? "))
        if people <= 0:
            raise ValueError("Number of people must be positive")
            
        total_bill = bill + tip
        result = total_bill / people
        
        print(f"\nBill Summary:")
        print(f"Original bill: £{bill:.2f}")
        print(f"Tip amount: £{tip:.2f} ({tip_percentage}%)")
        print(f"Total bill: £{total_bill:.2f}")
        print(f"Each person in the group of {people} will pay: £{result:.2f}")
        
    except ValueError as e:
        print(f"Error: {str(e)}")
    except:
        print("Please enter valid numbers")
