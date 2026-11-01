import json

with open("shipments.json", "r") as file:
    shipments = json.load(file)

print("Total shipments:", len(shipments))



def find_shipment(search_awb):
    found = False

    for shipment in shipments:
        if search_awb == shipment["AWB"]:
            found = True
            print(shipment)

    if found == False:
        print("Shipment not found")


def update_shipment_status(AWB, Status):
    found = False

    for shipment in shipments:
        if AWB == shipment["AWB"]:
            found = True
            shipment["Status"] = Status

             # Save updated records to JSON file
            with open("shipments.json", "w") as file:
                json.dump(shipments, file, indent=4)


	    
            print("Shipment status updated")

    if found == False:
        print("Shipment not found")


# Collect user input
search_awb = input("Enter the AWB: ")
new_shipment_status = input("Enter the new status: ")

# Update shipment status
update_shipment_status(search_awb, new_shipment_status)

# Display updated shipment details
find_shipment(search_awb)
