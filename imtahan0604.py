class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

    def determine_priority(self):
        critical_diseases = ['cancer', 'heart', 'corona']
        if self.age < 12 or self.disease in critical_diseases:
            return 'RedZone'
        elif self.age > 60:
            return 'YellowZone'
        else:
            return 'GreenZone'

patients = []
for _ in range(2):
    name = input("Xəstənin adını daxil edin: ")
    age = int(input("Xəstənin yaşını daxil edin: "))
    disease = input("Xəstənin xəstəliyini daxil edin: ")
    patient = Patient(name, age, disease)
    patients.append((patient, patient.determine_priority()))

for patient, priority in patients:
    print(f"Adı: {patient.name}, Yaşı: {patient.age}, Xəstəliyi: {patient.disease}, Prioritet: {priority}")