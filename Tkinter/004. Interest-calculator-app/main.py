import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
window.title("Interest Calculator App")

amount_label = tk.Label(window, text="Amount:")
amount_label.pack(pady=10)
amount_entry = tk.Entry(window)
amount_entry.pack(pady=5)

time_label = tk.Label(window, text="Time (in years):")
time_label.pack(pady=10)
time_entry = tk.Entry(window)
time_entry.pack(pady=5)

rate_label = tk.Label(window, text="Interest Rate (%):")
rate_label.pack(pady=10)
rate_entry = tk.Entry(window)
rate_entry.pack(pady=5)

def calculate_simple_interest():
    amount = float(amount_entry.get())
    time = float(time_entry.get())
    rate = float(rate_entry.get())
    simple_interest = (amount * time * rate) / 100
    simple_interest_label.config(text=simple_interest)


simple_interest_button = tk.Button(window, text="Calculate Simple Interest", command=calculate_simple_interest)
simple_interest_button.pack(pady=10)

simple_interest_label = tk.Label(window, text="Simple Interest: ")
simple_interest_label.pack(pady=5)

window.mainloop()