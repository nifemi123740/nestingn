def check_eligibility():
    while True:
        print("\n--- Student Eligibility Check ---")
        
        grade=int(input("Enter your grade: "))
        science_score=float(input("Enter your science score: "))
        fee_paid=input("Has student paid the trip fee?(yes/no): ").lower()


        if grade>=5:
            if science_score>=70:
                if fee_paid=='yes':
                    print("✅Student is eligible for the trip.")
                else:
                    print("❌Not eligible: Trip fee not paid.")
            else:
                print("❌Not eligible: Science score below 70.")
        else:
            print("❌Not eligible: Grade level below 5.")
        repeat = input("check another student? (yes/no): ").lower()
        if repeat != 'yes':
            print("✅Trip eligibility checks complete. Have fun on the trip")
            break

check_eligibility()
