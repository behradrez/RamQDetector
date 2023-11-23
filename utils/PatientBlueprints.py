class Patient:
    def __init__(self, name, NAM, numVisits):
        self.name = name
        self.NAM = NAM
        self.numVisits = numVisits

    def __str__(self):
        return self.name + ',' + self.NAM + ',' + str(self.numVisits) + "Visits"

    def __eq__(self, other):
        return type(self) == type(other) and self.name == other.name and self.NAM == other.NAM

    def __gt__(self, other):
        return self.numVisits > other.numVisits

    def __le__(self, other):
        return self.numVisits <= other.numVisits

    def __lt__(self, other):
        return self.numVisits < other.numVisits

    def __ge__(self, other):
        return self.numVisits >= other.numVisits


class PatientList:
    listOfPatients: list

    def __init__(self, listOfPatients, total_visits_tuple):
        self.listOfPatients = listOfPatients
        self.S_Visits=total_visits_tuple[0]
        self.CM_Visits=total_visits_tuple[1]
        self.total_Visits=total_visits_tuple[2]

    def sort_List(self):
        new_list = []
        print("Sorting Patients...")
        for repetition in range(len(self.listOfPatients)):
            patient = self.listOfPatients.pop()
            for index in range(len(new_list)+1):
                if len(new_list) == 0:
                    new_list.append(patient)
                    break
                elif new_list[index] > patient:
                    continue
                elif new_list[index] < patient or new_list[index] <= patient:
                    new_list.insert(index, patient)
                    break
        self.listOfPatients = new_list
