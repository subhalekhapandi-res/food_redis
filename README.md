# Food Waste Redistribution System

A command-line Python application to reduce food waste by connecting food donors with recipients — built with a focus on accessibility and local community impact.

---

## Overview

This system allows facilities (canteens, NGOs, hostels, etc.) to list surplus food, and recipients to claim and collect it before it goes to waste. All records are stored in a local CSV file — no database or internet connection required.

---

## Features

- Add food donation listings with name, quantity, location, and expiry date
- View all food items with live status tracking
- Claim available food items
- Mark claimed items as collected
- Auto-incrementing food IDs
- Input validation with informative error messages
- Clean tabular display in the terminal

---

## Project Structure

```
food-redistribution/
│
├── main_prog.py       # Entry point — runs the main menu loop
├── faci_func.py       # Core functions — add, view, claim, collect
├── food_list.csv      # Auto-generated data file (created on first run)
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.x (no external libraries required — uses only `csv` and `os`)

### Run the Application

```bash
python main_prog.py
```

The `food_list.csv` file is created automatically on first run.

---

## Usage

When you run the program, you'll see the main menu:

```
=============================================
   FOOD WASTE REDISTRIBUTION SYSTEM
=============================================
  1.  Add Food Donation
  2.  View Available Food
  3.  Claim Food
  4.  Mark Food as Collected
  5.  Exit
=============================================
```

### Workflow

1. **Donor** selects option `1` and enters food details (name, quantity, location, expiry date).
2. **Recipient** selects option `2` to browse available items, then option `3` to claim one.
3. Once the item is picked up, select option `4` to mark it as collected.

---

## Food Status Lifecycle

```
Available  →  Claimed  →  Collected
```

| Status    | Meaning                          |
|-----------|----------------------------------|
| Available | Listed and ready to be claimed   |
| Claimed   | Reserved by a recipient          |
| Collected | Successfully picked up           |

---

## Data Storage

All records are saved to `food_list.csv` with the following fields:

| Field       | Description                        |
|-------------|------------------------------------|
| FOOD_ID     | Auto-incremented unique identifier |
| FOOD_NAME   | Name of the food item              |
| QUANTITY    | Amount available                   |
| LOCATION    | Pickup location                    |
| EXPIRY_DATE | Date the food expires              |
| STATUS      | Available / Claimed / Collected    |

---

## Future Improvements

- Tamil-language interface for regional accessibility
- Web or GUI frontend
- Expiry date validation and alerts
- Multi-user roles (admin, donor, recipient)
- SMS/notification integration for claims

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---
