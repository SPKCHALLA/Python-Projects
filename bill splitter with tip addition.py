#Bill splitter with tip addition

print("Welcome to the tip calculator.\n")
bill_amt = input("Please enter the bill amount\n")
ppl= input("Please enter the no. of people willing to split\n")
tip_percentage = input("Please enter the tip percentage\n")
tip_amt = float(tip_percentage)*(float(bill_amt)/100)
# print(tip_amt)
bill_per_person = ((float(bill_amt)+tip_amt)/int(ppl))
bill_per_person = "{:.2f}".format(bill_per_person)
print(bill_per_person)