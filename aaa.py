num_people = int(input("Enter the total number of people: "))

for i in range(num_people):
  name = input(f"\nEnter the name of Person {i+1}: ")
  gender = input(f"Enter the gender of {name} (Male,M,male,m /Female,F,female,f): ")
  if gender.lower() == "male" or gender.lower() == "m":
    call = "Mr."
  elif gender.lower() == "female" or gender.lower() == "f":
    call = "Ms."
  else:
    call = ""

  print(f"\n--- Data for {call} {name} ---")
  data1 = int(input(f"Enter Age for {call} {name}: "))
  data2 = float(input(f"Enter Height for {call} {name}(in meters): "))
  data3 = int(input(f"Enter Weight for {call} {name}(in Kg): "))
  def calculate_bmi(height_m, weight_kg):
    bmi = weight_kg / (height_m**2)
    return bmi
  data4 = calculate_bmi(data2, data3)
  print(f"* Data for {call} {name}:\n  Age: {data1}\n  Height: {data2}\n  Weight: {data3}\n  BMI: {data4:.2f}")
  if data4 < 18.5:
    print(f"{call} {name} is underweight.")
  elif data4 < 25:
    print(f"{call} {name} is normal weight.")
  elif data4 < 30:
    print(f"{call} {name} is overweight.")
  elif data4 < 35:
    print(f"{call} {name} is obese.")
  else:
    print(f"{call} {name} is extremly obese.")