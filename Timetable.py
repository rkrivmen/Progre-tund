from easygui import *
tunniplaan = []

#Esmaspäev
tunniplaan.append(['Karjääriõpetus','Programmeerimine','Eesti keel','Joonestamine','Valikaine'])

#Teisipäev
tunniplaan.append(['Inglise keel (A. Linde, T. Lingiene) / Kehaline kasvatus','Matemaatika','Loogika','Kirjandus','Bioloogia'])

#Kolmapäev
tunniplaan.append(['Valikaine','Joonestamine','Inglise keel (A. Linde, I. Dunderdale) / Kehaline kasvatus','Eesti keel','Klassijuhatajatund / K5 üritused'])

#Neljapäev
tunniplaan.append(['Kirjandus','Matemaatika','Ajalugu','Füüsika','Bioloogia'])

#Reede
tunniplaan.append(['Segakoor / Ettevalmistus olümpiaadiks','Ajalugu','Füüsika','Matemaatika','vaba tund'])



päev = enterbox("Mis päev täna on? ").title()
tund = integerbox("Mitmes tund (numbrina)? ")
while tund < 1 or tund > 5:
    tund = integerbox("Mitmes tund (1 - 5)? ")
    
tänased_tunnid = ""
if päev == "Esmaspäev":
  tänased_tunnid = tunniplaan[0][tund-1]
elif päev == "Teisipäev":
  tänased_tunnid = tunniplaan[1][tund-1]
elif päev == "Kolmapäev":
  tänased_tunnid = tunniplaan[2][tund-1]
elif päev == "Neljapäev":
  tänased_tunnid = tunniplaan[3][tund-1]
elif päev == "Reede":
  tänased_tunnid = tunniplaan[4][tund-1]
else:
  msgbox("Sellel päeval kooli pole!")
  
if tänased_tunnid != "":
    msgbox(päev + ", praegu on " + str(tund) + "." + "tund, selleks on " + tänased_tunnid + ".")
