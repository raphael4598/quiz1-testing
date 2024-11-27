def calculate_bill_logic(current_meter, last_meter, unit_amount, room_type, bill_type):
    if current_meter <= last_meter:
        return {"status": "warning", "message": "Current Meter must be greater than Last Meter!"}

    if bill_type == "Water Bill":
        bill = unit_amount * 5
    elif bill_type == "Electric Bill":
        bill = unit_amount * 6
    else:
        return {"status": "error", "message": "Please select a bill type!"}

    total_rental = 0
    if room_type == "Single Bed":
        total_rental = 1500
    elif room_type == "Double Bed":
        total_rental = 2000

    total_bill = bill + total_rental
    progress = 100 if room_type in ["Single Bed", "Double Bed"] else 50
    return {"status": "success", "total_bill": total_bill, "progress": progress}

def reset_fields_logic():
    return {
        "last_meter": "",
        "current_meter": "",
        "unit_amount": "",
        "room_type": "Please Select",
        "bill_type": None,
        "progress": 0,
        "result": ""
    }
