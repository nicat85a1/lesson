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
        
    #def __str__(self):
        return f"Adı: {self.name}, Yaşı: {self.age}, Xəstəliyi: {self.disease}, Prioritet: {self.determine_priority()}"

patients = []
for _ in range(2):
    name = input("Xəstənin adını daxil edin: ")
    age = int(input("Xəstənin yaşını daxil edin: "))
    disease = input("Xəstənin xəstəliyini daxil edin: ")
    patient = Patient(name, age, disease)
    patients.append((patient))

for patient in patients:
    print(f"Adı: {patient.name}, Yaşı: {patient.age}, Xəstəliyi: {patient.disease}, Prioritet: {patient.determine_priority()}")

#for patient in patients:
    #print(patient)