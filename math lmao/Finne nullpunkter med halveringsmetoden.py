from pylab import * # Importerer bibliotek med bl.a. plot

x = linspace(-10, 10, 1000) # x-verdier
def funksjonsverdi(x): # Funksjon som regner ut de
    y = 2*x**3 - 6*x**2 - 2*x + 6 # tilhørende funksjonsverdiene
    return y # og returnerer de


y = funksjonsverdi(x) # Kjører funksjonen og regner ut y
plot(x, y, "g") # Plotter x og y med grønn farge
xlabel("År") # Setter navn på x-aksen
ylabel("Antall") # Setter navn på y-aksen
grid() # Tegner rutenett
xlim(-2, 4) # Setter intervall for x-aksen
ylim(-20, 20) # Setter intervall for y-aksen
axhline(y=0, color="k") # Tegner sort linje for y = 0 (x-aksen)
axvline(x=0, color="k") # Tegner sort linje for x = 0 (y-aksen)
show() # Viser grafen