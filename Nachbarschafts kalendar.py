#Nachbarschafts-App
print("Willkommen beim Nachbarschafts Kalendar, geben sie einfach nur ein Datum ein und ich zeige ihnen dann was dort stattfindet. Geben sie nun ihr Datum ein:")
#Der Benutzer wird nach einem Datum gefragt.
datum=input("Gib ein Datum im Format JJJJ-MM-TT): ")
anlaesse =  {
#In dieser Liste (Dictionary) werden die anstehenden Anlässe aufgelistet.  
    "2025-12-24" : "Weihnachten"
    "2025-05-05" : "Flohmarkt"
    "2025-02-14" : "Valentistag"
    "2025-12-31" : "Silvester"
    "2025-07-06" : "Dorffest"
    
}
#Definition die prüft ob es an diesem bestimmten Tag einen Anlass gibt.
 def zeige_anlaesse(datum):
#Es wird geprüft ob sich das Datum im Dictionary befindet.
     if datum in anlaesse:
#Wenn ja wird der passende Anlass angezeigt.
         print("Am ", datum, "ist:", anlaesse[datum])
         
    else:
#Wenn nicht wird dem Benutzer angezeigt, dass an diesem Tag keine Anlässe stattfinden.
        print("Am , datum findet kein Anlass statt.")
