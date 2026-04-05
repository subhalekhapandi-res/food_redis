from faci_func import *
import csv

ensure_file_exists()  

while True:
    show_menu()
    try:
        task = int(input("\n  Enter your choice (1-5): "))
    except ValueError:
        print("\n  ✘ Invalid input. Please enter a number between 1 and 5.")
        continue

    if task == 1:
        add_food()
    elif task == 2:
        view_food()
    elif task == 3:
        claim_food()
    elif task == 4:
        mark_collected()
    elif task == 5:
        print("\n  Thank you for using the Food Waste Redistribution System!")
        print("  Goodbye! 👋\n")
        break
    else:
        print("\n  ✘ Invalid choice. Please enter a number between 1 and 5.")
