olom_terfogat_kobcentimeterben = 18 #lead_volume
rez_terfogat_kobcentimeterben = 23 #copper_volume

olom_suruseg = 11.34 #lead_density
rez_suruseg = 8.69 #copper_density

olom_tomeg_grammban = olom_terfogat_kobcentimeterben*olom_suruseg #lead_mass
rez_tomeg_grammban = rez_terfogat_kobcentimeterben*rez_suruseg #copper_mass

if olom_tomeg_grammban>rez_tomeg_grammban:
    print("18 cm^3 ólom nehezebb, mint 25 cm^3 réz.")
else:
    print("25 cm^3 réz nehezebb, mint 18 cm^3 ólom.")