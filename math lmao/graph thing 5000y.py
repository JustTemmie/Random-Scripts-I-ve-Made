
y_values = []
transactions = 0

for x in range(0,52):
    transactions = 0.75*x**3 - 59.5*x**2 + 1200*x
    
    if transactions > 5000:
        y_values.append(transactions)
        

print(y_values)
print(len(y_values))