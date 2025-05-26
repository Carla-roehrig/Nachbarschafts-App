#Nachbarschafts-App
print("Willkommen beim Nachbarschafts Kalendar, geben sie einfach nur ein Datum ein und ich zeige ihnen dann was dort stattfindet. Geben sie nun ihr Datum ein:")
antwort=input()
anlaesse =  {
    
    "2025-12-24" : "Weihnachten"
    "2025-05-05" : "Flohmarkt"
    "2025-02-14" : "Valentistag"
    "2025-12-31" : "Silvester"
    "2025-07-06" : "Dorffest"
    
}
 def zeige_anlaesse(datum):
     if datum in anlaesse:
         print("Am ", datum ist , anlaesse