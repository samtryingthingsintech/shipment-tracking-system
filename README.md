# Shipment Tracking System

## Overview

The Shipment Tracking System is a Python-based application designed to help logistics operations teams search shipment records, retrieve shipment details, and update delivery statuses.

The application uses JSON for external data storage, allowing shipment information to remain available even after the program is closed.

## Business Problem

Logistics operations teams regularly need to retrieve shipment information and update delivery statuses.

Managing these records manually can be time-consuming and makes it difficult to maintain updated information.

This project demonstrates how Python can simplify basic shipment tracking and record management.

## Features

- Search shipments using a unique AWB number.
- Retrieve complete shipment details.
- Handle searches for non-existent shipment records.
- Update shipment delivery status.
- Save updated shipment records permanently.
- Load shipment data from an external JSON file.

## Technologies Used

- Python
- JSON
- Lists and dictionaries
- Loops and conditional statements
- Functions
- File handling

## Project Structure

- `shipment_tracking.py` – Main Python application.
- `shipments.json` – Stores shipment records.

## How It Works

1. The application loads shipment records from `shipments.json`.
2. The user enters an AWB number.
3. The user enters the new shipment status.
4. The application searches for the matching shipment.
5. If found, its status is updated.
6. The updated shipment records are saved back to the JSON file.
7. The application displays the updated shipment details.

## How to Run

1. Install Python.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Run:

`python shipment_tracking.py`

## Sample Shipment Record

- AWB: A1002
- Client: Flipkart
- Pincode: 560001
- Boxes: 2
- Weight: 8.2 kg
- Initial Status: Pending

After updating the status to Delivered, the application saves the change in `shipments.json`.

## Key Learnings

This project helped me understand:

- Working with Python lists and dictionaries.
- Searching records using loops and conditions.
- Creating reusable functions.
- Accepting user input.
- Updating dictionary values.
- Reading external JSON files.
- Writing updated records back to JSON.
- Maintaining data across application restarts.

## Author

Built as part of my journey to learn Python through practical business and operations problems.
