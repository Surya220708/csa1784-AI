# Vacuum Cleaner Problem

location = input("Enter location (A/B): ").upper()
status = input("Enter status (Dirty/Clean): ").lower()

if status == "dirty":
    print("Suck")
    print("Room Cleaned")
else:
    print("No Action")

if location == "A":
    print("Move Right")
elif location == "B":
    print("Move Left")