import os
import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import random
import string



class TicketSystem(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ticket System")
        self.geometry("1200x800")

        # Use the current working directory to store the database file
        self.database_filename = os.path.join(os.getcwd(), "database_tiket.xlsx")
        if not os.path.exists(self.database_filename):
            df = pd.DataFrame(columns=["Name", "Date", "People", "Total Cost", "Resi Code", "Payment Method"])
            df.to_excel(self.database_filename, index=False)

        self.create_main_widgets()
        
    def create_main_widgets(self):
        self.clear_window()
        self.label = tk.Label(self, text="Pilih Opsi:")
        self.label.pack(pady=10)

        self.reschedule_button = tk.Button(self, text="Reschedule", command=self.reschedule)
        self.reschedule_button.pack(pady=5)

        self.refund_button = tk.Button(self, text="Refund", command=self.refund)
        self.refund_button.pack(pady=5)

        self.history_button = tk.Button(self, text="Riwayat Pembelian", command=self.view_history)
        self.history_button.pack(pady=5)

        self.book_ticket_button = tk.Button(self, text="Book Ticket", command=self.book_ticket)
        self.book_ticket_button.pack(pady=5)

    def reschedule(self):
        self.clear_window()
        self.label = tk.Label(self, text="Input Nomor Resi:")
        self.label.pack(pady=10)
        self.resi_entry = tk.Entry(self)
        self.resi_entry.pack(pady=5)
        self.submit_button = tk.Button(self, text="Submit", command=self.check_resi_reschedule)
        self.submit_button.pack(pady=5)
        self.back_button = tk.Button(self, text="Back", command=self.create_main_widgets)
        self.back_button.pack(pady=5)

    def check_resi_reschedule(self):
        resi = self.resi_entry.get()
        if self.valid_resi(resi):
            self.clear_window()
            self.label = tk.Label(self, text="Input Tanggal Baru:")
            self.label.pack(pady=10)
            self.tanggal_entry = tk.Entry(self)
            self.tanggal_entry.pack(pady=5)
            self.confirm_button = tk.Button(self, text="Konfirmasi", command=self.update_tanggal)
            self.confirm_button.pack(pady=5)
            self.back_button = tk.Button(self, text="Back", command=self.create_main_widgets)
            self.back_button.pack(pady=5)
        else:
            messagebox.showerror("Error", "Nomor resi tidak ditemukan")

    def update_tanggal(self):
        new_date = self.tanggal_entry.get()
        # Logika untuk update tanggal tiket
        messagebox.showinfo("Success", "Tanggal tiket berhasil diupdate")
        self.create_main_widgets()

    def refund(self):
        self.clear_window()
        self.label = tk.Label(self, text="Input Nomor Resi:")
        self.label.pack(pady=10)
        self.resi_entry = tk.Entry(self)
        self.resi_entry.pack(pady=5)
        self.submit_button = tk.Button(self, text="Submit", command=self.check_resi_refund)
        self.submit_button.pack(pady=5)
        self.back_button = tk.Button(self, text="Back", command=self.create_main_widgets)
        self.back_button.pack(pady=5)

    def check_resi_refund(self):
        resi = self.resi_entry.get()
        if self.valid_resi(resi):
            
            self.back_button = tk.Button(self, text="Back", command=self.create_main_widgets)
            self.back_button.pack(pady=5)


    def return_funds(self):
        # Logika untuk mengembalikan dana 80% dari pembayaran
        messagebox.showinfo("Success", "Dana kembali sebesar 80% dari pembayaran. Refund berhasil")
        self.create_main_widgets()

    def view_history(self):
        self.clear_window()
        # Logika untuk menampilkan riwayat pembelian tiket
        history = "Menampilkan riwayat pembelian..."
        self.label = tk.Label(self, text=history)
        self.label.pack(pady=10)
        self.back_button = tk.Button(self, text="Back", command=self.create_main_widgets)
        self.back_button.pack(pady=5)

    def book_ticket(self):
        self.clear_window()

        self.attractions = [
            "Solo Safari",
            "Lokananta",
            "Tumurun",
            "Keraton Mangkunegaran",
            "Balekambang"
        ]

        self.selected_attraction = tk.StringVar()
        self.attraction_label = tk.Label(self, text="Select Attraction:")
        self.attraction_label.pack(pady=10)
        self.attraction_combo = ttk.Combobox(self, textvariable=self.selected_attraction, values=self.attractions)
        self.attraction_combo.pack(pady=10)
        self.attraction_combo.bind("<<ComboboxSelected>>", self.display_info)

        self.info_label = tk.Label(self, text="", wraplength=500)
        self.info_label.pack(pady=10)

        self.data_label = tk.Label(self, text="Enter your details:")
        self.data_label.pack(pady=10)

        self.name_label = tk.Label(self, text="Name:")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)

        self.date_label = tk.Label(self, text="Date (dd-mm-yyyy):")
        self.date_label.pack(pady=5)
        self.date_entry = tk.Entry(self)
        self.date_entry.pack(pady=5)

        self.people_label = tk.Label(self, text="Number of People:")
        self.people_label.pack(pady=5)
        self.people_entry = tk.Entry(self)
        self.people_entry.pack(pady=5)

        self.payment_label = tk.Label(self, text="Payment Method:")
        self.payment_label.pack(pady=10)

        self.payment_methods = ["Credit Card", "Debit Card", "PayPal"]
        self.selected_payment = tk.StringVar()
        self.payment_combo = ttk.Combobox(self, textvariable=self.selected_payment, values=self.payment_methods)
        self.payment_combo.pack(pady=10)

        self.calculate_button = tk.Button(self, text="Calculate Total", command=self.calculate_total)
        self.calculate_button.pack(pady=20)

        self.total_label = tk.Label(self, text="")
        self.total_label.pack(pady=10)

        self.back_button = tk.Button(self, text="Back", command=self.create_main_widgets)
        self.back_button.pack(pady=5)

        self.print_button = tk.Button(self, text="Print Ticket", command=self.print_ticket)
        self.print_button.pack(pady=10)

        self.back_button = tk.Button(self, text="Back", command=self.create_main_widgets)
        self.back_button.pack(pady=5)

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
            self.name = self.name_entry.get()
            self.date = self.date_entry.get()
            self.people = int(self.people_entry.get())
            self.payment_method = self.selected_payment.get()

            if not self.name or not self.date or not self.payment_method:
                raise ValueError("All fields must be filled")

            self.total_cost = self.people * self.ticket_price
            self.resi_code = self.generate_resi()

            # Simpan resi ke dalam file Excel
            self.save_resi_to_excel(self.name, self.date, self.people, self.total_cost, self.resi_code, self.payment_method)

            self.total_label.config(text=f"Total Cost: Rp{self.total_cost}\nResi Code: {self.resi_code}")
            messagebox.showinfo("Booking Successful", f"Name: {self.name}\nDate: {self.date}\nPeople: {self.people}\nPayment Method: {self.payment_method}\nTotal Cost: Rp{self.total_cost}\nResi Code: {self.resi_code}")
        except ValueError as ve:
            messagebox.showerror("Input Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def generate_resi(self):
        resi_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        return resi_code

    def save_resi_to_excel(self, name, date, people, total_cost, resi_code, payment_method):
        try:
            new_data = {
                "Name": name,
                "Date": date,
                "People": people,
                "Total Cost": total_cost,
                "Resi Code": resi_code,
                "Payment Method": payment_method
            }

            df = pd.read_excel(self.database_filename)
            df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
            df.to_excel(self.database_filename, index=False)
            print("Data saved to Excel.")  # Debugging message
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save to Excel: {e}")

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

    def valid_resi(self, resi):
        try:
            if os.path.exists(self.database_filename):
                
                df = pd.read_excel(self.database_filename)
            print("File found. Checking resi.")  # Debugging message

            # Check resi validity (assuming 'Resi Code' is the column for validation)
            if resi in df["Resi Code"].values:
                # Optionally drop the 'Resi Code' column if desired
                    df = df.drop(df[df["Resi Code"] == resi].index)
                    df.to_excel(self.database_filename)
                    self.clear_window()
                    self.label = tk.Label(self, text="Mengembalikan Dana...")
                    self.label.pack(pady=10)
                    self.return_funds()
            else:
                    print("Resi is invalid.")
                    return False
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read Excel: {e}")
            return False
        

    def view_history(self):
        self.clear_window()
        history_frame = ttk.Frame(self)
        history_frame.pack(fill=tk.BOTH, expand=True)

        history_tree = ttk.Treeview(history_frame, columns=("Name", "Date", "People", "Total Cost", "Resi Code", "Payment Method"), height=10)
        history_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(history_frame, orient=tk.VERTICAL, command=history_tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        history_tree.configure(yscrollcommand=scrollbar.set)

        history_tree.heading("#0", text="")
        history_tree.heading("#1", text="Name")
        history_tree.heading("#2", text="Date")
        history_tree.heading("#3", text="People")
        history_tree.heading("#4", text="Total Cost")
        history_tree.heading("#5", text="Resi Code")
        history_tree.heading("#6", text="Payment Method")

        if os.path.exists(self.database_filename):
            df = pd.read_excel(self.database_filename)
            df = df.sort_values(by="Date", ascending=False)  # Sort by date in descending order
            for i, row in df.iterrows():
                history_tree.insert("", tk.END, values=(row["Name"], row["Date"], row["People"], row["Total Cost"], row["Resi Code"], row["Payment Method"]))

            # Set column widths
            history_tree.column("#0")
            history_tree.column("#1")
            history_tree.column("#2")
            history_tree.column("#3")
            history_tree.column("#4")
            history_tree.column("#5")
            history_tree.column("#6")

        # Add a Back button
        back_button = ttk.Button(history_tree, text="Back", command=self.create_main_widgets)
        back_button.pack(pady=0, padx=0)
        
    def print_ticket(self):
        ticket_text = f"""
        ---------------
        Ticket
        ---------------
        Name: {self.name}
        Date: {self.date}
        Number of Tickets: {self.people}
        Total Cost: Rp{self.total_cost}
        Resi Code: {self.resi_code}
        Payment Status: LUNAS
        ---------------
        Enjoy your visit!
        ---------------
        """
        ticket_window = tk.Toplevel(self)
        ticket_window.title("Ticket")
        ticket_label = tk.Label(ticket_window, text=ticket_text, justify="left", font=("Courier", 12))
        ticket_label.pack(pady=20)



if __name__ == "__main__":
    app = TicketSystem()
    
    app.mainloop()
