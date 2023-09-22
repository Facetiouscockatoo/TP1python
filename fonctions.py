def testbissextile(n): #détermine si une année est bissextile (int -> bool)
    if n%100==0 or n%4 != 0: return False
    if n%400==0 : return True
    else: return True

def nombrejours(mois,annee): #donne le nombre de jours d'un mois sur une année précise (int*int -> int)
    if mois!=1:              # mois autre que février
        if mois%2==0 or mois==7: return 31
        else: return 30
    if testbissextile(annee): return 29 #mois de février
    else: return 28

def datevalide(jour,mois,annee): #Détermine la validité d'une date (int*int*int -> bool)
    if jour > 31: return False  #Enlève la possibilité de nombre de jours impossibles pour tout mois
    else:
        if jour <= nombrejours(mois,annee): return True 
        else: return False

def validitétexte(jour,mois,annee): #version texte de datevalide (int*int*int -> str)
    if datevalide(jour, mois, annee): return "date valide"
    else: return "date non valide"

#Ai-je respecté les bonnes pratiques ? J'espère !

def mesImpots(n): #donne le montant des impôts dur le revenu en fonction desdits revenus (int->float)
    if n <= 10225: return 0
    if n <= 26070: return ((n-10225)*11)/100
    if n <= 74545: return ((n-26070)*30)/100 
    if n <= 160336: return ((n-74545)*41)/100
    return ((n-160336)*45)/100

    

    

        
    

    