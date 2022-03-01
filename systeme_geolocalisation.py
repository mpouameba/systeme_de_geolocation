# Déclarer les variables principales de notre code
 
# declarer notre fonction principale

# Sur les trois prochaines lignes il est question d'attribuer principalement les valeurs longitudinales de paris en dégré, en minute enfin en seconde 

#Ensuite on fait un appel de fonction appelé long_paris avec le même nom que notre fonction principale, les variables ont un suffixe long pour spécifier qu'on est dans le calcul de la longitude

#Puis les trois lignes suivantes on repète le procésus précedant: attribution des valeurs latitudinales de paris en dégré, en minute et en seconde puis faire un appel de fonction lat_paris pour indiquer qu'on calcule la latitude de Paris

#Enfin pour les huit prochaines lignes on va succéssivement déclarer nos variables x et y dans lesquelles on va attribuer la longitude et la latitude du pole nord

#attribuer les résultats de notre calcul précédant de long_paris et de la lat_paris donc longitude et latitude paris 

#Calculer enfin la géolocalisation en faisant la racine carrée de longitude pole (X) nord moins longitude paris (long_paris) le tout au carrée plus racine carrée da latitude pôle nord (y) moins latitude paris (lat_paris) le tout au carrée

#Enfin afficher (print) les résultats des calculs de longitude paris, latitude paris et plus bas le résultat du calcul de la géolocalisation.

import math

def convert(degre, minute, seconde):                               
    return(degre+minute/60+seconde/3600)                           
degre_long=48                                                      
minute_long=51                                                     
seconde_long=23.81
long_paris = convert(degre_long, minute_long, seconde_long)
degre_lat=2
minute_lat=21
seconde_lat=7.999
lat_paris = convert(degre_lat, minute_lat, seconde_lat)

def cal_geolocal(x, y, long_paris, lat_paris):
    return(math.sqrt((x-long_paris)**2+(y-lat_paris)**2))
x=86
y=172
long_paris=2.3522219
lat_paris=48.856614
print(long_paris, lat_paris)
print (cal_geolocal(x, y, long_paris, lat_paris))