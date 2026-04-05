import csv
import os

CSV_FILE = "food_list.csv"
FIELDNAMES = ["FOOD_ID", "FOOD_NAME", "QUANTITY", "LOCATION", "EXPIRY_DATE", "STATUS"]

def ensure_file_exists():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()

def get_next_id():
    ensure_file_exists()
    with open(CSV_FILE, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        rows = [row for row in reader if row["FOOD_ID"].strip() != ""]
        if len(rows) == 0:
            return 1
        last_id = int(rows[-1]["FOOD_ID"])
        return last_id + 1

def read_all_rows():
    ensure_file_exists()
    with open(CSV_FILE, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)

def write_all_rows(rows):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)

def show_menu():
    print("\n" + "=" * 45)
    print("   FOOD WASTE REDISTRIBUTION SYSTEM")
    print("=" * 45)
    print("  1.  Add Food Donation")
    print("  2.  View Available Food")
    print("  3.  Claim Food")
    print("  4.  Mark Food as Collected")
    print("  5.  Exit")
    print("=" * 45)

def print_table(rows):
    if len(rows) == 0:
        print("\n  [ No food items found in the list ]")
        return
    print("\n" + "-" * 75)
    print(f"  {'ID':<5} {'FOOD':<15} {'QTY':<12} {'LOCATION':<12} {'EXPIRY':<12} {'STATUS'}")
    print("-" * 75)
    for row in rows:
        status = row["STATUS"]
        if status == "Available":
            status_display = "[Available]"
        elif status == "Claimed":
            status_display = "[Claimed]  "
        else:
            status_display = "[Collected]"

        print(f"  {row['FOOD_ID']:<5} {row['FOOD_NAME']:<15} {row['QUANTITY']:<12} "
              f"{row['LOCATION']:<12} {row['EXPIRY_DATE']:<12} {status_display}")
    print("-" * 75)


def add_food():
    print("\n--- ADD FOOD DONATION ---")

    food_name = input("  Food Name      : ").strip()
    if food_name == "":
        print("  ✘ Food name cannot be empty. Returning to menu.")
        return

    quantity = input("  Quantity       : ").strip()
    if quantity == "":
        print("  ✘ Quantity cannot be empty. Returning to menu.")
        return

    location = input("  Location       : ").strip()
    if location == "":
        print("  ✘ Location cannot be empty. Returning to menu.")
        return

    expiry_date = input("  Expiry Date    : ").strip()
    if expiry_date == "":
        print("  ✘ Expiry date cannot be empty. Returning to menu.")
        return

    food_id = get_next_id()

    item = {
        "FOOD_ID": food_id,
        "FOOD_NAME": food_name,
        "QUANTITY": quantity,
        "LOCATION": location,
        "EXPIRY_DATE": expiry_date,
        "STATUS": "Available"
    }
    
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow(item)

    print(f"\n  ✔ '{food_name}' added successfully! (ID: {food_id})")


def view_food():
    print("\n--- FOOD SURPLUS LIST ---")
    rows = read_all_rows()
    print_table(rows)


def claim_food():
    print("\n--- CLAIM FOOD ---")

    rows = read_all_rows()
    available = [row for row in rows if row["STATUS"] == "Available"]

    if len(available) == 0:
        print("\n  [ No available items to claim right now ]")
        return

    print("\n  Currently Available Items:")
    print_table(available)

    claim_id = input("\n  Enter the Food ID to claim: ").strip()

    if not claim_id.isdigit():
        print("  ✘ Please enter a valid numeric ID.")
        return

    found = False
    for row in rows:
        if row["FOOD_ID"] == claim_id:
            found = True
            if row["STATUS"] == "Available":
                row["STATUS"] = "Claimed"
                print(f"\n  ✔ '{row['FOOD_NAME']}' has been successfully claimed!")
            elif row["STATUS"] == "Claimed":
                print(f"\n  ✘ '{row['FOOD_NAME']}' is already claimed by someone else.")
            elif row["STATUS"] == "Collected":
                print(f"\n  ✘ '{row['FOOD_NAME']}' has already been collected. It's no longer available.")
            break

    if not found:
        print(f"\n  ✘ No item found with ID '{claim_id}'. Please check and try again.")
        return

    write_all_rows(rows)


def mark_collected():
    print("\n--- MARK AS COLLECTED ---")

    rows = read_all_rows()
    claimed = [row for row in rows if row["STATUS"] == "Claimed"]

    if len(claimed) == 0:
        print("\n  [ No claimed items waiting for collection ]")
        return

    print("\n  Items Pending Collection:")
    print_table(claimed)

    collect_id = input("\n  Enter the Food ID to mark as collected: ").strip()

    if not collect_id.isdigit():
        print("  ✘ Please enter a valid numeric ID.")
        return

    found = False
    for row in rows:
        if row["FOOD_ID"] == collect_id:
            found = True
            if row["STATUS"] == "Claimed":
                row["STATUS"] = "Collected"
                print(f"\n  ✔ '{row['FOOD_NAME']}' marked as collected. Thank you!")
            elif row["STATUS"] == "Available":
                print(f"\n  ✘ '{row['FOOD_NAME']}' has not been claimed yet. Claim it first before collecting.")
            elif row["STATUS"] == "Collected":
                print(f"\n  ✘ '{row['FOOD_NAME']}' is already marked as collected.")
            break

    if not found:
        print(f"\n  ✘ No item found with ID '{collect_id}'. Please check and try again.")
        return

    write_all_rows(rows)



