import numpy as np
import matplotlib.pyplot as plt
from skimage import io

## II. Création et Modifications d'Images
def affichage(im):
	io.imshow(im)
	return None

# 1)
def image1(nb_col=200,nb_lig=300):
	image=np.zeros((nb_lig,nb_col,3),dtype=np.uint8)
	for ligne in range(nb_lig):
		for colonne in range(nb_col):
			if 10<=ligne<=90 and 10<=colonne<=60:
				image[ligne][colonne]=(255,0,0) #Red
			elif 10<=ligne<=90 and 70<=colonne<=130:
				image[ligne][colonne]=(255,255,0) #Yellow
			elif 10<=ligne<=90 and 140<=colonne<=190:
				image[ligne][colonne]=(255,120,0) #Orange
			elif 100<=ligne<=120:
				image[ligne][colonne]=(0,0,0) #Black
			elif 190<=ligne<=240 and (10<=colonne<=60 or 140<=colonne<=190):
				image[ligne][colonne]=(0,0,255) #Blue
			elif 130<=ligne<=270 and 70<=colonne<=130:
				image[ligne][colonne]=(0,255,0) #Green
			else:
				image[ligne][colonne]=(255,255,255) #White
	return image

# 2)
def negatif(im=image1()):
	return 255-im

# 3)
def gris(im=image1()):
	return 0.2125*im[:,:,0]+0.7154*im[:,:,1]+0.0721*im[:,:,2]

# 4)a)
def gradientH(im=gris()):
	nb_lig,nb_col=im.shape
	tab=255*np.ones((nb_lig,nb_col))
	H=np.array(im,dtype=np.float)
	for lig in range(nb_lig):
		for col in range(nb_col-1):
			H[lig][col]=abs(im[lig][col+1]-im[lig][col])
	return H

# 4)b)
def gradientV(im=gris()):
	nb_lig,nb_col=im.shape
	tab=255*np.ones((nb_lig,nb_col))
	H=np.array(im,dtype=np.float)
	for lig in range(nb_lig-1):
		for col in range(nb_col):
			H[lig][col]=abs(im[lig+1][col]-im[lig][col])
	return H

# 4)c)
def question4c(im=image1()):
	return gradientH(gris(im)),gradientV(gris(im))

# 4)d)
def question4d(im=image1()):
	gri=gris(im)
	grad=np.sqrt((gradientH(gri))**2+(gradientV(gri))**2)
	grad_norm=(255/np.max(grad))*grad
	return negatif(grad_norm)

# 4)e)
def choix_seuil(im=image1()):
	nbre_pix,val=np.histogram(im(),bins=256)
	plt.plot(val[:-1],nbre_pix)
	plt.show()

def question4e(im=image1(),seuil=10):
	Tab_seuil=np.array(negatif(question4d()))<seuil
	return np.array(255*Tab_seuil,dtype=np.uint8)

## III. Etude d'Image d'un Alliage Métallique

# 1)
def recuperation():
	return 255*io.imread('C:/Users\Maxime\OneDrive\Documents\Prépa\MP\IPT\Python\TD\inox.png')

# 2)
def TailleExtremites(im=recuperation()):
	return im.shape,np.max(im),np.min(im)

def extreme(tab=recuperation()):
	min,max=tab[0,0,0],tab[0,0,0]
	nb_lig,nb_col,prof=tab.shape
	for lig in range(nb_lig):
		for col in range(nb_col):
			for p in range(prof):
				if tab[lig,col,p]>max:
					max=tab[lig,col,p]
				elif tab[lig,col,p]<min:
					min=tab[lig,col,p]
	return max,min

# 3)
def gris_inox(im=recuperation()):
	return gris(im)

# 4)
def bool(im=recuperation(),seuil=190):
	return im>seuil

# 5)
def pourcentages(im=bool()[10:210,10:210]):
	nb_lig,nb_col,prof=im.shape
	return 100*np.sum(im)/(nb_lig*nb_col*prof),100*(1-np.sum(im)/(nb_lig*nb_col*prof))

# 6)
def contours(im=recuperation()):
	return question4d(im)