# Səhiyyə Sənayesi Tapşırığı

high_priority = ["heart","cancer","corona"]

highest_superiority_patients = []

class Patient:

    def __init__(self, patient_name,patient_age,patient_illness):
        self.patient_name = patient_name
        self.patient_age = patient_age
        self.patient_status = patient_illness

    @classmethod
    def print_patient_details(self, patient_name, patient_age,patient_illness):
        return patient_name, patient_age,patient_illness

    @classmethod
    def patient_emergency_situation(self, patient_name, patient_age, patient_illness):

        if patient_age < 12 or patient_illness in high_priority:
            highest_superiority_patients.append("patient:")
            highest_superiority_patients.append(patient_name)
            highest_superiority_patients.append("hastalığı:")
            highest_superiority_patients.append(patient_illness)
            highest_superiority_patients.append("status:")
            highest_superiority_patients.append("redzone")
        elif patient_age > 60:
            highest_superiority_patients.append("patient:")
            highest_superiority_patients.append(patient_name)
            highest_superiority_patients.append("hastalığı:")
            highest_superiority_patients.append(patient_illness)
            highest_superiority_patients.append("status:")
            highest_superiority_patients.append("greenzone")
        else:
            highest_superiority_patients.append("patient:")
            highest_superiority_patients.append(patient_name)
            highest_superiority_patients.append("hastalığı:")
            highest_superiority_patients.append(patient_illness)
            highest_superiority_patients.append("status:")
            highest_superiority_patients.append("yellowzone")

for patients in range(2):
    Patient.patient_emergency_situation(patient_name=input("Enter patient name: "), patient_age=int(input("Enter patient age: ")),patient_illness=input("Enter patient illness: "))

print(highest_superiority_patients)