def calculate_power_bill(units, fixed_charge = 50):
  """
  bill = 0 for the first 100 units and then it is charged 5 per unit from 101 to 200 and 8 per unit for units greater than 200
  """
  if units<=100:
    cost = 0
  elif units<=200:
    cost = (units-100)*5
  else:
    cost = (100*5) + ((units-200)*8)
  total_bill = fixed_charge+cost
  return total_bill
bill = calculate_power_bill(900)
print("The total bill is:", bill)
