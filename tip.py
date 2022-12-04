def main():
   dollars = dollars_to_float(input("How much was the meal? "))
   percent = percent_to_float(input("What percentage would you like to tip? "))
   tip = dollars * percent
   print(f"Leave ${tip:.2f}")
 
 
def dollars_to_float(d):
   _ = float(d.replace("$",""))
   return _
 
def percent_to_float(p):
   _ = float(p.replace("%",""))/100
   return _
 
main()
answer = str(input("what is the meaning of life? "))
