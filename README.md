# ISO21827

 API REST /iso21827    Auteur: Rioche Patrick                  le 23/11/2019

   Cette API REST a ete concue dans un but pedagogique pour servir de support a
   une formation MBA Expert en SI pour la MySchoolDigital de l'ESPL à Angers.

   Les specifcations de l'API sont donnees par la norme iso21827 permettant de
   connaitre le niveau de maturite d'une entreprise a partir de 12 questions.
   voir : https://www.ssi.gouv.fr/guide/guide-relatif-a-la-maturite-ssi/

   Exemple de requete pour connaitre la maturite a partir des 12 reponses aux questions :

       /iso21827/maturite/0,0,0,1,1,1,2,2,2,3,3,3
       => {"idmaturite": 3, "inferieura": 6, "superieura": 8, "maturite": "Processus definis"}

   Exemple de requete pour connaitre le contenu de la question 9 :
   
       /iso21827/question/9
       => {"idquestion": 9, "idniveau": 3, "question": "Moyens des attaquants : Quels sont les competences et les ressources des attaquants potentiels ?", "valeur": 0}

   Exemple de requete pour connaitre la reponse 0 ou 1 ou 2 ou 3 possible de la question 9 :
   
       /iso21827/reponse/9,1
       => {"idquestion": 9, "idreponse": 1, "reponse": "Les attaquants peuvent disposer de moyens significatifs", "valeur": 1}
       
   Exemple de requete pour connaitre le niveau 1 ou 2 ou 3 ou 4 des questions :
   
       /iso21827/niveau/1
       => {"idniveau": 1, "niveau": "Trois questions pour estimer le niveau des consequences potentielles", "maxniveau": 0}
       
