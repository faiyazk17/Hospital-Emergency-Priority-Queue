# # Importing random and er_class for future reference.
# import random
# from er_class import *

# def main():
#     """
#     -------------------------------------------------------
#     Creates 10 mock patients objects and schedules their appointment
#     with respect to their priority level.
#     -------------------------------------------------------
#     Returns:
#       None
#     -------------------------------------------------------
#     """

#     # Creating a priority queue to store the ER queue.
#     er_queue = Priority_Queue()

#     # Creating 10 mock patient objects.
#     patient1 = Patient("John", "Cena", random.randint(0,11), 1).patient_info
#     patient2 = Patient("Michael", "Scott", random.randint(0,11), 2).patient_info
#     patient3 = Patient("Snoop", "Dogg", random.randint(0,11), 3).patient_info
#     patient4 = Patient("Chris", "Hemsworth", random.randint(0,11), 4).patient_info
#     patient5 = Patient("Harry", "Potter", random.randint(0,11), 5).patient_info
#     patient6 = Patient("Lionel", "Messi", random.randint(0,11), 6).patient_info
#     patient7 = Patient("Lebron", "James", random.randint(0,11), 7).patient_info
#     patient8 = Patient("Roger", "Federer", random.randint(0,11), 8).patient_info
#     patient9 = Patient("Serena", "Williams", random.randint(0,11), 9).patient_info
#     patient10 = Patient("Aaron", "Carpet", random.randint(0,11), 10).patient_info

#     # Adding each patient to the un-prioritized ER queue (i.e. which patients have arrived).
#     arrived1 = er_queue.arrive(patient1)
#     arrived2 = er_queue.arrive(patient2)
#     arrived3 = er_queue.arrive(patient3)
#     arrived4 = er_queue.arrive(patient4)
#     arrived5 = er_queue.arrive(patient5)
#     arrived6 = er_queue.arrive(patient6)
#     arrived7 = er_queue.arrive(patient7)
#     arrived8 = er_queue.arrive(patient8)
#     arrived9 = er_queue.arrive(patient9)
#     arrived10 = er_queue.arrive(patient10)

#     # Scheduling patients based on their priority level then announcing the patient that is next in the queue.
#     for i in range(len(er_queue)-1):

#         # Scheduling next patient.
#         patient_scheduled = er_queue.schedule()

#         # Calling scheduled patient by their ER name and their priority level.
#         print("Patient to see doctor now:", patient_scheduled[0]+patient_scheduled[1]+str(patient_scheduled[3]))
#         print("Priority level:", patient_scheduled[2])

#         # Announcing next patient.
#         next_patient = er_queue.announce()

#         # Printing patient next in queue after scheduled patient.
#         print("The next patient will be:", next_patient[0]+next_patient[1]+str(next_patient[3]))

#         # Empty line for legibility.
#         print()

#     # For the last patient.
#     # Scheduling patient.
#     patient_scheduled = er_queue.schedule()

#     # Calling scheduled patient by their ER name and their priority level.
#     print("Last patient to see doctor now:", patient_scheduled[0] + patient_scheduled[1] + str(patient_scheduled[3]))
#     print("Priority level:", patient_scheduled[2])

#     # No more patients remaining.
#     print("\nAll 10 patients have consulted the doctor; no more patients left in ER queue.")

# # Calling main function.
# main()

import tkinter as tk
from tkinter import ttk
import random
from er_class import Priority_Queue, Patient


class ERQueueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ER Queue App")

        self.patient_info_label = ttk.Label(
            root, text="Enter Patient Information:")
        self.patient_info_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.first_name_label = ttk.Label(root, text="First Name:")
        self.first_name_entry = ttk.Entry(root)
        self.first_name_label.grid(row=1, column=0, padx=10, pady=5)
        self.first_name_entry.grid(row=1, column=1, padx=10, pady=5)

        self.last_name_label = ttk.Label(root, text="Last Name:")
        self.last_name_entry = ttk.Entry(root)
        self.last_name_label.grid(row=2, column=0, padx=10, pady=5)
        self.last_name_entry.grid(row=2, column=1, padx=10, pady=5)

        self.emergency_level_label = ttk.Label(root, text="Emergency Level:")
        self.emergency_level_spinbox = ttk.Spinbox(
            root, from_=0, to=10, wrap=True)
        self.emergency_level_label.grid(row=3, column=0, padx=10, pady=5)
        self.emergency_level_spinbox.grid(row=3, column=1, padx=10, pady=5)

        self.add_patient_button = ttk.Button(
            root, text="Add Patient", command=self.add_patient)
        self.add_patient_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.output_label = ttk.Label(root, text="Appointment Order:")
        self.output_label.grid(row=5, column=0, columnspan=2, pady=10)

        self.output_listbox = tk.Listbox(root, width=40, height=10)
        self.output_listbox.grid(
            row=6, column=0, columnspan=2, padx=10, pady=10)

        # Creating a priority queue to store the ER queue.
        self.er_queue = Priority_Queue()

    def add_patient(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        emergency_level = int(self.emergency_level_spinbox.get())
        sequence_number = len(self.er_queue) + 1

        # Creating a Patient object with user input.
        patient = Patient(first_name, last_name,
                          emergency_level, sequence_number)

        # Adding the patient to the ER queue.
        self.er_queue.arrive(patient)

        # Updating the output listbox.
        self.update_output_listbox()

        # Clearing input fields.
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.emergency_level_spinbox.delete(0, tk.END)

    def update_output_listbox(self):
        # Clearing the listbox.
        self.output_listbox.delete(0, tk.END)

        # Adding patients to the listbox.
        for i in range(len(self.er_queue)):
            patient = self.er_queue._values[i]
            display_text = f"{patient.first_name} {patient.last_name} - Priority: {patient.priority_level}"
            self.output_listbox.insert(tk.END, display_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = ERQueueApp(root)
    root.mainloop()
