brukt = 0
igjen = 10000


for i in range(1, 1000):
    if igjen - brukt - i*4 < 0: break
    brukt += i*4
    igjen -= brukt
    print(f"{i} x {i}: {10000-igjen} brukt {igjen} igjen")

print( f"""
    
    you built everything up to and including {i-1} x {i-1}
    with a total of {10000-igjen} used, and {igjen} left over
    
        """)


# if not keep:
#     for i in range(1, 1000):
#         brukt += i*4
#         print(f"{i} x {i}: {brukt} brukt")
#         if brukt >= 10000: break
