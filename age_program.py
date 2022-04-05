AGE_MIN = 1 
AGE_MAX = 18
age = float(input('Age of individual:'))

if age <= AGE_MIN:
    print("Age is invalid")
elif age >= AGE_MAX:
    print ("Individual is an adult")
else:
    print("Individual is a minor")
print("Program finished...")
