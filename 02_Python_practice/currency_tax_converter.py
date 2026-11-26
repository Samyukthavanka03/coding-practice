def usd_to_inr(dollars, rate= 84.0):
  rupees = dollars*rate
  return rupees
def add_gst(amount, gst_percent=18):
  gst_amount = (gst_percent/100)*amount
  final_price= amount+gst_amount
  return gst_amount,final_price
inr = usd_to_inr(100)
gst, total = add_gst(inr)
print("Base INR amount:",inr)
print("GST (18%):", gst)
print("Final price with gst:", total)