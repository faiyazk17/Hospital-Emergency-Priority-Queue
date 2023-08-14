# Importing random and er_class for future reference.
import random
from er_class import *

def main():
    """
    -------------------------------------------------------
    Creates 10 mock patients objects and schedules their appointment
    with respect to their priority level.
    -------------------------------------------------------
    Returns:
      None
    -------------------------------------------------------
    """

    # Creating a priority queue to store the ER queue.
    er_queue = Priority_Queue()        

    # Creating 10 mock patient objects.
    patient1 = Patient("John", "Cena", random.randint(0,11), 1).patient_info
    patient2 = Patient("Michael", "Scott", random.randint(0,11), 2).patient_info
    patient3 = Patient("Snoop", "Dogg", random.randint(0,11), 3).patient_info
    patient4 = Patient("Chris", "Hemsworth", random.randint(0,11), 4).patient_info
    patient5 = Patient("Harry", "Potter", random.randint(0,11), 5).patient_info
    patient6 = Patient("Lionel", "Messi", random.randint(0,11), 6).patient_info
    patient7 = Patient("Lebron", "James", random.randint(0,11), 7).patient_info
    patient8 = Patient("Roger", "Federer", random.randint(0,11), 8).patient_info
    patient9 = Patient("Serena", "Williams", random.randint(0,11), 9).patient_info
    patient10 = Patient("Aaron", "Carpet", random.randint(0,11), 10).patient_info

    # Adding each patient to the un-prioritized ER queue (i.e. which patients have arrived).
    arrived1 = er_queue.arrive(patient1)
    arrived2 = er_queue.arrive(patient2)
    arrived3 = er_queue.arrive(patient3)
    arrived4 = er_queue.arrive(patient4)
    arrived5 = er_queue.arrive(patient5)
    arrived6 = er_queue.arrive(patient6)
    arrived7 = er_queue.arrive(patient7)
    arrived8 = er_queue.arrive(patient8)
    arrived9 = er_queue.arrive(patient9)
    arrived10 = er_queue.arrive(patient10)

    # Scheduling patients based on their priority level then announcing the patient that is next in the queue.
    for i in range(len(er_queue)-1):

        # Scheduling next patient.
        patient_scheduled = er_queue.schedule()

        # Calling scheduled patient by their ER name and their priority level.
        print("Patient to see doctor now:", patient_scheduled[0]+patient_scheduled[1]+str(patient_scheduled[3]))
        print("Priority level:", patient_scheduled[2])

        # Announcing next patient.
        next_patient = er_queue.announce()

        # Printing patient next in queue after scheduled patient.
        print("The next patient will be:", next_patient[0]+next_patient[1]+str(next_patient[3]))

        # Empty line for legibility.
        print()

    # For the last patient.
    # Scheduling patient.
    patient_scheduled = er_queue.schedule()

    # Calling scheduled patient by their ER name and their priority level.
    print("Last patient to see doctor now:", patient_scheduled[0] + patient_scheduled[1] + str(patient_scheduled[3]))
    print("Priority level:", patient_scheduled[2])

    # No more patients remaining.
    print("\nAll 10 patients have consulted the doctor; no more patients left in ER queue.")

# Calling main function.
main()