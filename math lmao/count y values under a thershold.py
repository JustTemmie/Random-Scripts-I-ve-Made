
y_values = []
current_y_value = 0
cutting_point = 450000

for x in range(0,51):
    current_y_value = -3*x**4 + 305*x**3 - 9000*x**2 + 66000*x + 495000
    
    if current_y_value > cutting_point:
        y_values.append(current_y_value)
        

print(y_values)
print(len(y_values))