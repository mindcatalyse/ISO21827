#!/usr/bin/python
# -*- coding: cp1252 -*-
# API REST /iso21827    Auteur: Rioche Patrick                  le 23/11/2019
#
#   Cette API REST a ete concue dans un but pedagogique pour service de support a
#   une formation MBA Expert en SI de la MySchoolDigital de l'ESPL à Angers.
#
#   Les specifcations de l'API sont donnees par la norme iso21827 permettant de
#   connaitre le niveau de maturite d'une entreprise a partir de 12 questions.
#   voir : https://www.ssi.gouv.fr/guide/guide-relatif-a-la-maturite-ssi/
#
#   Exemple de requete pour connaitre la maturite a partir des 12 reponses aux questions :
#
#       /iso21827/maturite/0,0,0,1,1,1,2,2,2,3,3,3
#       => {"idmaturite": 3, "inferieura": 6, "superieura": 8, "maturite": "Processus definis"}
#
#   Exemple de requete pour connaitre le contenu de la question 9 :
#   
#       /iso21827/question/9
#       => {"idquestion": 9, "idniveau": 3, "question": "Moyens des attaquants : Quels sont les competences et les ressources des attaquants potentiels ?", "valeur": 0}
#
#   Exemple de requete pour connaitre la reponse 0 ou 1 ou 2 ou 3 possible de la question 9 :
#   
#       /iso21827/reponse/9,1
#       => {"idquestion": 9, "idreponse": 1, "reponse": "Les attaquants peuvent disposer de moyens significatifs", "valeur": 1}
#
#   Exemple de requete pour connaitre le niveau 1 ou 2 ou 3 ou 4 des questions :
#   
#       /iso21827/niveau/1
#       => {"idniveau": 1, "niveau": "Trois questions pour estimer le niveau des consequences potentielles", "maxniveau": 0}
#
#
from bottle import route,run,install
from bottle_pgsql import PgSQLPlugin

install(PgSQLPlugin('host=localhost port=5432 dbname=postgres user=postgres password=secret'))

@route('/iso21827')
def help():
    sDoc = ""
    sDoc = sDoc + "Exemple de requete pour connaitre la maturite a partir des 12 reponses aux questions :" + "<br>"
    sDoc = sDoc + "-    /iso21827/maturite/0,0,0,1,1,1,2,2,2,3,3,3" + "<br><br>"
    sDoc = sDoc + "Exemple de requete pour connaitre le contenu de la question 9 :" + "<br>"
    sDoc = sDoc + "-    /iso21827/question/9" + "<br><br>"
    sDoc = sDoc + "Exemple de requete pour connaitre la reponse 0 ou 1 ou 2 ou 3 possible de la question 9 :" + "<br>"
    sDoc = sDoc + "-   /iso21827/reponse/9,1" + "<br><br>"
    sDoc = sDoc + "Exemple de requete pour connaitre le niveau 1 ou 2 ou 3 ou 4 des questions :" + "<br>"
    sDoc = sDoc + "-   /iso21827/niveau/1" + "<br><br>"
    return sDoc

@route('/iso21827/maturite/<v1>,<v2>,<v3>,<v4>,<v5>,<v6>,<v7>,<v8>,<v9>,<v10>,<v11>,<v12>')
def maturite(db,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12):
    #
    #   Calcul de la maturite
    #
    maxniv1 = 0
    if int(v1) > maxniv1:
        maxniv1 = int(v1)
    if int(v2) > maxniv1:
        maxniv1 = init(v2)
    if int(v3) > maxniv1:
        maxniv1 = int(v3)
    #
    maxniv2 = 0
    if int(v4) > maxniv2:
        maxniv2 = int(v4)
    if int(v5) > maxniv2:
        maxniv2 = int(v5)
    if int(v6) > maxniv2:
        maxniv2 = int(v6)
    #
    maxniv3 = 0
    if int(v7) > maxniv3:
        maxniv3 = int(v7)
    if int(v8) > maxniv3:
        maxniv3 = int(v9)
    if int(v9) > maxniv3:
        maxniv3 = int(v9)
    #
    maxniv4 = 0
    if int(v10) > maxniv4:
        maxniv4 = int(v10)
    if int(v11) > maxniv4:
        maxniv4 = int(v11)
    if int(v12) > maxniv4:
        maxniv4 = int(v12)        
    #
    maxniv = 0
    maxniv = maxniv1 + maxniv2 + maxniv3 + maxniv4
    #
    if maxniv >= 0 and maxniv <= 2:
        maturite = 1
    if maxniv >= 3 and maxniv <= 5:
        maturite = 2
    if maxniv >= 6 and maxniv <= 8:
        maturite = 3
    if maxniv >= 9 and maxniv <= 10:
        maturite = 4
    if maxniv >= 11 and maxniv <= 12:
        maturite = 5
    #
    db.execute('select * from maturite where idmaturite=%s', str(maturite) )
    row = db.fetchone()
    if row:
        return row

@route('/iso21827/question/<q1>')
def question(db,q1):
    #
    #   Affiche la question
    #
    db.execute('select * from question where idquestion=' + str(q1))     
    row = db.fetchone()
    if row:
        return row

@route('/iso21827/reponse/<q1>,<r1>')
def reponse(db,q1,r1):
    #
    #   Affiche la reponse correspond à la question
    #
    
    db.execute('select * from reponse where (idquestion=%s and idreponse=%s)', [q1, r1])
    row = db.fetchone()
    if row:
        return row

@route('/iso21827/niveau/<n1>')
def niveau(db,n1):
    #
    #   Affiche le niveau correspond à la question
    #
    
    db.execute('select * from niveau where idniveau=%s', n1)
    row = db.fetchone()
    if row:
        return row
    
run(host='0.0.0.0', port=80, debug=True)
