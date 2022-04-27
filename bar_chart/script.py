import matplotlib.pyplot as plt
title = "Hva er suffiksen i misforståelse?"

xlabel = None
ylabel = None

#svar = ['mis','forstaelsen','els','else','en', 'n', 'vet ikke']
#mengde = [1,3,2,3,1,1,2,3]

svar = ["mis", "forståelsen",'els', 'else', 'elsen', 'en', 'n', 'vet ikke']
mengde = [1,3,2,3,1,1,2,3]


fig1, ax1 = plt.subplots()
ax1.pie(mengde, labels=svar, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()