def split_bill(total_bill, people = 2, tip_percent = 10):
  tip_amount = (total_bill) * (tip_percent/100)
  total_with_tip = total_bill + tip_amount
  per_person_cost = total_with_tip/people
  return total_with_tip, per_person_cost
total, each = split_bill(1000)
print("Total bill is:", total)
print("Each person should pay:", each)
