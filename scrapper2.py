import requests
from bs4 import BeautifulSoup


links = []
#definition d'un url de depart
url = 'https://www.tripadvisor.fr/Restaurants-g187147-Paris_Ile_de_France.html'
#variable de stockage de reponse url
response = requests.get(url)
#creation d'un soupe pour lire dans le html
soup = BeautifulSoup(response.text, 'lxml')
#isolation des balises href
href = [i.get('href') for i in soup.find_all('a')]
test = list(href)
#les urls qui commence avec cette chaine de caractere nous interessent pour les mail
target = "Restaurant_Review"
#definition de la balise qui nous interessent pour chaque restaurant
targetmail="mailto"
#chaine de charactere vide pour l'instant
yy=""
for x in test[:]:
	if target in str(x):
		#on complete les urls qui correspondent
		url = "https://www.tripadvisor.fr" + x
		#on stock l'url
		response = requests.get(url)
		#creation d'une soupe pour lire dans le html
		soup = BeautifulSoup(response.text, 'lxml')
		#isolation des balises href
		href = [i.get('href') for i in soup.find_all('a')]
		testmail = list(href)
		for xx in testmail[:]:
			#condition pour afficher uniquement les balise mailto
			if targetmail in str(xx):
				if xx != yy:
					#affichage des email nettoyé
					print(xx[7:len(xx)-10])
					yy=xx
					#on vient écrire dans un fichier .txt toutes les adresses mails
					f = open("mail-paris.txt", "a")
					f.write(xx[7:len(xx)-10] + "\n")
					f.close()