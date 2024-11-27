import tkinter as tk
from tkinter import ttk, messagebox
from codepython import calculate_bill_logic, reset_fields_logic

def calculate_bill():
    try:
        current_meter = int(current_meter_entry.get())
        last_meter = int(last_meter_entry.get())
        unit_amount = int(unit_amount_entry.get())
        room_type = room_type_combobox.get()
        bill_type = bill_type_var.get()

        result = calculate_bill_logic(current_meter, last_meter, unit_amount, room_type, bill_type)

        if result["status"] == "warning":
            messagebox.showwarning("Warning", result["message"])
        elif result["status"] == "error":
            messagebox.showerror("Error", result["message"])
        else:
            result_entry.delete(0, tk.END)
            result_entry.insert(0, f"{result['total_bill']} ฿")
            progress_bar["value"] = result["progress"]

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

def reset_fields():
    fields = reset_fields_logic()
    last_meter_entry.delete(0, tk.END)
    current_meter_entry.delete(0, tk.END)
    unit_amount_entry.delete(0, tk.END)
    result_entry.delete(0, tk.END)
    room_type_combobox.set(fields["room_type"])
    bill_type_var.set(fields["bill_type"])
    progress_bar["value"] = fields["progress"]

root = tk.Tk()
root.title("Bill Calculator")

tk.Label(root, text="Select Bills").grid(row=0, column=0, padx=5, pady=5, sticky="w")
bill_type_var = tk.StringVar()
tk.Radiobutton(root, text="Water Bill", variable=bill_type_var, value="Water Bill").grid(row=1, column=0, padx=5, pady=5, sticky="w")
tk.Radiobutton(root, text="Electric Bill", variable=bill_type_var, value="Electric Bill").grid(row=2, column=0, padx=5, pady=5, sticky="w")

tk.Label(root, text="Last Meter").grid(row=3, column=0, padx=5, pady=5, sticky="e")
last_meter_entry = tk.Entry(root)
last_meter_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text="Current Meter").grid(row=4, column=0, padx=5, pady=5, sticky="e")
current_meter_entry = tk.Entry(root)
current_meter_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(root, text="Unit Amount").grid(row=5, column=0, padx=5, pady=5, sticky="e")
unit_amount_entry = tk.Entry(root)
unit_amount_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Label(root, text="Room Type").grid(row=0, column=2, padx=5, pady=5)
room_type_combobox = ttk.Combobox(root, values=["Please Select", "Single Bed", "Double Bed"], state="readonly")
room_type_combobox.grid(row=0, column=3, padx=5, pady=5)
room_type_combobox.set("Please Select")

tk.Label(root, text="Result").grid(row=6, column=0, padx=5, pady=5, sticky="e")
result_entry = tk.Entry(root)
result_entry.grid(row=6, column=1, padx=5, pady=5)

calculate_button = tk.Button(root, text="Calculate Bill", command=calculate_bill)
calculate_button.grid(row=7, column=0, padx=5, pady=5)

reset_button = tk.Button(root, text="Reset", command=reset_fields)
reset_button.grid(row=7, column=1, padx=5, pady=5)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.grid(row=8, column=0, columnspan=4, padx=5, pady=10)

root.mainloop()
