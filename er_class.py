# Imporing deepcopy for future reference regarding methods of the queue.
from copy import deepcopy

# Creating Patient class to store patients' information.
class Patient:

    def __init__(self, first_name, last_name, priority_level, sequence_number):
        """
        -------------------------------------------------------
        Initializes a patient.
        Use: ab = Patient(first_name, last_name, prority_level, sequence_number)
        -------------------------------------------------------
        Returns:
            a new Patient object (Patient)
        -------------------------------------------------------
        """
        self.first_name = first_name
        self.last_name = last_name
        self.priority_level = priority_level
        self.sequence_number = sequence_number

        self.patient_info = [first_name, last_name, priority_level, sequence_number]

class Priority_Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty priority queue.
        Use: pq = Priority_Queue()
        -------------------------------------------------------
        Returns:
            a new Priority_Queue object (Priority_Queue)
        -------------------------------------------------------
        """
        self._values = []
        self._first = None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the priority queue.
        Use: n = len(pq)
        -------------------------------------------------------
        Returns:
            the number of values in the priority queue.
        -------------------------------------------------------
        """
        return len(self._values)

    def arrive(self, value):
        """
        -------------------------------------------------------
        A copy of value is appended to the end of the priority queue
        Python list, and _first is updated as appropriate to the index of
        value with the highest priority.
        Use: pq.arrive(value)
        -------------------------------------------------------
        Parameters:
            value - a data element
        Returns:
            None
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))

        # Determine whether new value has highest priority.
        if self._first is None:
            self._first = 0

        elif value < self._values[self._first]:
            self._first = len(self._values) - 1

        return

    def _set_first(self):
        """
        -------------------------------------------------------
        Private helper function to set the value of _first.
        _first is the index of the value with the highest
        priority in the priority queue. None if queue is empty.
        Use: self._set_first()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        n = len(self._values)

        if n == 0:
            self._first = None

        else:
            self._first = 0

            for i in range(1, n):
                # If priority number is lower, make this the higher priority patient.
                if self._values[i][2] < self._values[self._first][2]:
                    self._first = i

                # If priority levels are the same, compare sequence/arrival number.
                if self._values[i][2] == self._values[self._first][2]:
                    if self._values[i][3] < self._values[self._first][3]:
                        self._first = i

        return

    def schedule(self):
        """
        -------------------------------------------------------
        Removes and returns the highest priority value from the priority queue.
        Use: val = pq.schedule()
        -------------------------------------------------------
        Returns:
            value - the highest priority value in the priority queue -
                the value is removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot remove from an empty priority queue"

        # Find the value with the next highest priority.
        self._set_first()

        value = self._values.pop(self._first)

        return value

    def announce(self):
        """
        -------------------------------------------------------
        Peeks at the highest priority value of the priority queue.
        Use: v = pq.announce()
        -------------------------------------------------------
        Returns:
            value - a copy of the highest priority value in the priority queue -
                the value is not removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty priority queue"

        # Find the value with the next highest priority.
        self._set_first()

        value = deepcopy(self._values[self._first])

        return value