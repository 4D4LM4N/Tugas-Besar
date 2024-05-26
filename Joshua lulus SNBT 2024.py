import tkinter as tk
from tkinter import messagebox, ttk
import random

class TicketBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ticket Booking System")
        self.root.geometry("600x500")

        self.tickets = {}  # Dictionary to store ticket information
        self.create_widgets()

    def create_widgets(self):
        # Dropdown for selecting the tourist attraction
        self.attractions = [
            "Solo Safari",
            "Lokananta",
            "Tumurun",
            "Keraton Mangkunegaran",
            "Balekambang"
        ]

        self.selected_attraction = tk.StringVar()
        self.attraction_label = tk.Label(self.root, text="Select Attraction:")
        self.attraction_label.pack(pady=10)
        self.attraction_combo = ttk.Combobox(self.root, textvariable=self.selected_attraction, values=self.attractions)
        self.attraction_combo.pack(pady=10)
        self.attraction_combo.bind("<<ComboboxSelected>>", self.display_info)

        # Display information based on the selected attraction
        self.info_label = tk.Label(self.root, text="", wraplength=500)
        self.info_label.pack(pady=10)

        # Entry fields for user data
        self.data_label = tk.Label(self.root, text="Enter your details:")
        self.data_label.pack(pady=10)

        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=5)

        self.date_label = tk.Label(self.root, text="Date (dd-mm-yyyy):")
        self.date_label.pack(pady=5)
        self.date_entry = tk.Entry(self.root)
        self.date_entry.pack(pady=5)

        self.people_label = tk.Label(self.root, text="Number of People:")
        self.people_label.pack(pady=5)
        self.people_entry = tk.Entry(self.root)
        self.people_entry.pack(pady=5)

        self.payment_label = tk.Label(self.root, text="Payment Method:")
        self.payment_label.pack(pady=10)

        self.payment_methods = ["Credit Card", "Debit Card", "PayPal"]
        self.selected_payment = tk.StringVar()
        self.payment_combo = ttk.Combobox(self.root, textvariable=self.selected_payment, values=self.payment_methods)
        self.payment_combo.pack(pady=10)

        self.calculate_button = tk.Button(self.root, text="Calculate Total", command=self.calculate_total)
        self.calculate_button.pack(pady=20)

        self.total_label = tk.Label(self.root, text="")
        self.total_label.pack(pady=10)

        self.payment_code_label = tk.Label(self.root, text="")
        self.payment_code_label.pack(pady=10)

        self.payment_button = tk.Button(self.root, text="Make Payment", command=self.make_payment)
        self.payment_button.pack(pady=20)

        self.reschedule_button = tk.Button(self.root, text="Reschedule Ticket", command=self.reschedule_ticket)
        self.reschedule_button.pack(pady=10)

        self.refund_button = tk.Button(self.root, text="Request Refund", command=self.request_refund)
        self.refund_button.pack(pady=10)

        self.history_button = tk.Button(self.root, text="View Purchase History", command=self.view_history)
        self.history_button.pack(pady=10)

    def display_info(self, event):
        attraction = self.selected_attraction.get()
        info_text = ""
        if attraction == "Solo Safari":
            info_text = "Solo Safari: Rp50,000 per person"
            self.ticket_price = 50000
        elif attraction == "Lokananta":
            info_text = "Lokananta: Rp30,000 per person"
            self.ticket_price = 30000
        elif attraction == "Tumurun":
            info_text = "Tumurun: Rp25,000 per person"
            self.ticket_price = 25000
        elif attraction == "Keraton Mangkunegaran":
            info_text = "Keraton Mangkunegaran: Rp40,000 per person"
            self.ticket_price = 40000
        elif attraction == "Balekambang":
            info_text = "Balekambang: Rp35,000 per person"
            self.ticket_price = 35000
        
        self.info_label.config(text=info_text)

    def calculate_total(self):
        try:
            name = self.name_entry.get()
            date = self.date_entry.get()
            people = int(self.people_entry.get())
            payment_method = self.selected_payment.get()

            if not name or not date or not payment_method:
                raise ValueError("All fields must be filled")

            self.total_cost = people * self.ticket_price
            self.total_label.config(text=f"Total Cost: Rp{self.total_cost}")
            
            # Generate payment code
            self.payment_code = random.randint(100000, 999999)
            self.payment_code_label.config(text=f"Payment Code: {self.payment_code}")

        except ValueError as ve:
            messagebox.showerror("Input Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def make_payment(self):
        try:
            # Simulate payment process
            name = self.name_entry.get()
            date = self.date_entry.get()
            people = int(self.people_entry.get())
            payment_method = self.selected_payment.get()

            ticket_info = {
                "attraction": self.selected_attraction.get(),
                "name": name,
                "date": date,
                "people": people,
                "total_cost": self.total_cost,
                "payment_method": payment_method,
                "status": "LUNAS"
            }
            self.tickets[self.payment_code] = ticket_info

            messagebox.showinfo("Payment Successful", f"Payment Code: {self.payment_code}\nTotal Cost: Rp{self.total_cost}")
            self.total_label.config(text="Ticket already purchased: LUNAS")
            self.print_ticket()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def print_ticket(self):
        ticket_info = (
            f"Attraction: {self.selected_attraction.get()}\n"
            f"Name: {self.name_entry.get()}\n"
            f"Date: {self.date_entry.get()}\n"
            f"Number of People: {self.people_entry.get()}\n"
            f"Total Cost: Rp{self.total_cost}\n"
            f"Status: LUNAS"
        )
        messagebox.showinfo("Ticket", ticket_info)

    def reschedule_ticket(self):
        def process_reschedule():
            try:
                receipt_number = int(receipt_entry.get())
                if receipt_number in self.tickets:
                    new_date = new_date_entry.get()
                    self.tickets[receipt_number]["date"] = new_date
                    messagebox.showinfo("Reschedule Successful", f"New date: {new_date}\nTicket updated successfully!")
                    reschedule_window.destroy()
                else:
                    messagebox.showerror("Error", "Receipt number not found!")
            except ValueError:
                messagebox.showerror("Error", "Invalid receipt number!")
        
        reschedule_window = tk.Toplevel(self.root)
        reschedule_window.title("Reschedule Ticket")
        
        receipt_label = tk.Label(reschedule_window, text="Enter Receipt Number:")
        receipt_label.pack(pady=5)
        receipt_entry = tk.Entry(reschedule_window)
        receipt_entry.pack(pady=5)

        new_date_label = tk.Label(reschedule_window, text="Enter New Date (dd-mm-yyyy):")
        new_date_label.pack(pady=5)
        new_date_entry = tk.Entry(reschedule_window)
        new_date_entry.pack(pady=5)

        reschedule_button = tk.Button(reschedule_window, text="Reschedule", command=process_reschedule)
        reschedule_button.pack(pady=20)

    def request_refund(self):
        def process_refund():
            try:
                receipt_number = int(receipt_entry.get())
                if receipt_number in self.tickets:
                    refund_amount = 0.8 * self.tickets[receipt_number]["total_cost"]
                    del self.tickets[receipt_number]
                    messagebox.showinfo("Refund Successful", f"Refund Amount: Rp{refund_amount}")
                    refund_window.destroy()
                else:
                    messagebox.showerror("Error", "Receipt number not found!")
            except ValueError:
                messagebox.showerror("Error", "Invalid receipt number!")
        
        refund_window = tk.Toplevel(self.root)
        refund_window.title("Request Refund")
        
        receipt_label = tk.Label(refund_window, text="Enter Receipt Number:")
        receipt_label.pack(pady=5)
        receipt_entry = tk.Entry(refund_window)
        receipt_entry.pack(pady=5)

        refund_button = tk.Button(refund_window, text="Request Refund", command=process_refund)
        refund_button.pack(pady=20)

    def view_history(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("Purchase History")
        
        history_text = tk.Text(history_window, wrap="word")
        history_text.pack(expand=True, fill="both")

        for receipt, ticket in self.tickets.items():
            history_text.insert(tk.END, f"Receipt: {receipt}\n")
            for key, value in ticket.items():
                history_text.insert(tk.END, f"{key.capitalize()}: {value}\n")
            history_text.insert(tk.END, "\n" + "-"*50 + "\n\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = TicketBookingApp(root)
    root.mainloop()