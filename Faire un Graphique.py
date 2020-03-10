#Faire un Graphique !
import matplotlib.pyplot as plt

#Titre du Graph
plt.title("Le Titre")

#Titre des Axes
plt.xlabel("Nom de l'Axe X")
plt.ylabel("Nom de l'Axe Y")

#Fixer Min/Max des Axes
plt.axis([Xmin,Xmax,Ymin,Ymax])

#Grille
plt.grid(True)

#Affichage Graph
plt.show()

#Une Courbe
plt.plot([Liste des Abscisses],[Liste des Ordonnées])

#Légende Courbe
label="Légende de la courbe"
plt.legend(loc="best")

#Visuel des Courbes
"-" : -
"--" : --
"-." : 
":" : 

#Couleurs
"b" : 
"g" : 
"r" : 
"c" : 
"m" : 
"y" : 
"k" : 
"w" : 

#Marqueurs sur Courbe
marker=' '
"-" : solid line style
"--" : dashed line style
"-." : dash-dot line style
":" : dotted line style
"." : point marker
"," : pixel marker
"o" : circle marker
"v" : Triangle Down
"^" : Triangle Up
"<" : Triangle Left
">" : Triangle Right
"1" : Tri Down
"2" : Tri Up
"3" : Tri Left
"4" : Tri Right
"s" : Square
"p" : Pentagon
"*" : Star
"h" : Hexagon 1
"H" : Hexagon 2
"+" : Plus
"x" : x
"D" : Diamond
"d" : Thin Diamond
"|" : Vline
"_" : Hline
#Largeur des Courbes
plt.plot([],[],linewidth=EPAISSEUR)

#Visuel des Points
"^" : Triangles
"s" : Carrés

#Plusieurs Graphs
plt.subplot(UN NBRE)
plt.plot(...)

plt.subplot(UN NBRE PLUS GRAND)
plt.plot(...)

#Texte sur Graph
plt.text(Abscisse,Ordonnée,r"Message")

#Flèche sur Graph
plt.annotate("Message",xy=(Abscisse,Ordonnée),xytext=(Abscisse,Ordonnée),arrowprops={"facecolor=":"COULEUR","shrink":NBRE})

#Histogramme
n,bins,patches=plt.hist([Valeurs],NBRE DE BARRES, normed=1,facecolor="COULEUR CF LIGNE 33", alpha=NBRE)

#Camembert
name=[Catégories]
data=[Nbre de chaque catégorie]
explode=[ecart entre les parts]

plt.pie(data,explode=explode,labels=name, autopct='%1.1f%%', startangle=90, shadow=True)
plt.axis("equal")