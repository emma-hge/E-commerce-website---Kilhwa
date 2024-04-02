
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
import mysql.connector

import MySQLdb.cursors, re

app = Flask(__name__)


conn = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="azerty",
    database="kilhwa")


@app.route('/', methods=('GET', 'POST')) 
def accueil():
    return render_template('accueil.html')


@app.route('/login', methods=('GET', 'POST')) 
def login():
    msg = ''
    result = request.form
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form: 

        #création de variable pour un accès plus simple
        n = result['email']
        p = result['password']

        #compte existe ?
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM comptes WHERE email=%s AND password=%s', (n,p))
        #result = cursor.fetchall()
        #for x in result:
        #    print(x)

        #fetchone et retourne le résultat qui nous amène à l'accueil si ok
        comptes = cursor.fetchone()

        if comptes:
            n = str(comptes[1])
            p = str(comptes[2])
            return redirect(url_for('accueil'))
        else :
            msg = 'Mot de passe ou email incorrect.'

    return render_template('login.html',msg=msg)



@app.route('/register', methods=('GET', 'POST')) 
def register():
    msg= ''

    if request.method == 'POST' and 'email' in request.form and 'name' in request.form and 'password' in request.form:
        
        email = request.form['email']
        name = request.form['name']
        password = request.form['password']       

        #Va dans la bdd afin de regarder si compte déjà existant
        cursor=conn.cursor()
        cursor.execute("""SELECT * FROM comptes WHERE name = %s AND email = %s AND password = %s""", (name,email,password,))
        comptes = cursor.fetchone()

        # Si le formulaire n'est pas conforme, message d'erreur
        if comptes: #si compte existe
            msg = 'Le compte existe déjà.'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email): #si pas de @
            msg = 'Adresse mail invalide.'
        elif not re.match(r'[A-Za-z0-9]+', password): #si caractères spéciaux
            msg = 'Le mot de passe doit contenir seulement des lettres et des nombres.'
        elif not name or not password or not email: #si mal rempli
            msg = "Veuillez bien remplir l'inscription"
        else:
            # S'il n'y a aucune erreur et que le compte n'existe pas, on l'enregistre
            cursor.execute('INSERT INTO comptes VALUES (NULL, %s, %s, %s)', (email,name,password))
            #mysql.connection.commit()
            conn.commit()
            
            return redirect(url_for('accueil'))

    elif request.method == 'POST':
        msg= "Veuillez bien remplir l'inscription."

    return render_template('register.html', msg=msg)


@app.route('/femme', methods=('GET', 'POST')) 
def femme():
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM produits WHERE type='femme' """)
    produits = cursor.fetchall()

    return render_template('femme.html', produits=produits)


@app.route('/homme', methods=('GET', 'POST')) 
def homme():
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM produits WHERE type='homme' """)
    produits = cursor.fetchall()

    return render_template('homme.html',produits=produits)

@app.route('/accessoires', methods=('GET', 'POST')) 
def accessoires():
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM produits WHERE type='accessoires' """)
    produits = cursor.fetchall()

    return render_template('accessoires.html',produits=produits)

@app.route('/ajouter_panier/<int:produit_id>', methods=['POST'])
def ajouter_panier(produit_id):
    if request.method == 'POST':
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM produits WHERE produit_id = %s", (produit_id,))
        produit = cursor.fetchone()

        nom=produit[1]
        prix=produit[2]
        img=produit[4]
        quantite = int(request.form['quantite'])

        #produit déjà dans le panier ?
        cursor.execute("SELECT * FROM panier WHERE produit_id = %s", (produit_id,))
        produit_panier = cursor.fetchone()

        if produit_panier: # si produit présent dans panier -> met à jour la quantité
            nouvelle_quantite = produit_panier[5] + quantite
            cursor.execute("UPDATE panier SET quantite = %s WHERE produit_id = %s", (nouvelle_quantite, produit_id))
        else : # sinon on ajoute le produit
            cursor.execute("INSERT INTO panier (produit_id, nom, prix, img, quantite) VALUES (%s, %s, %s, %s, %s)", (produit_id, nom, prix, img, quantite))
        
        conn.commit()

    return redirect(url_for('panier'))

@app.route('/retirer_panier/<int:panier_id>', methods=['POST'])
def retirer_panier(panier_id):
    if request.method == 'POST':
        cursor = conn.cursor()

        # Quantité ?
        cursor.execute("SELECT quantite FROM panier WHERE panier_id = %s", (panier_id,))
        quantite = cursor.fetchone()[0] 

        if quantite > 1:
            # Si quantité > 1 ->  -1
            cursor.execute("UPDATE panier SET quantite = %s WHERE panier_id = %s", (quantite - 1, panier_id))
        else:
            # Si quantité = 1 -> supprime
            cursor.execute("DELETE FROM panier WHERE panier_id = %s", (panier_id,))
        conn.commit()
    return redirect(url_for('panier'))

@app.route('/panier', methods=('GET', 'POST')) 
def panier():
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM panier")   
    panier = cursor.fetchall()

    prix_total=sum(produit[3]*produit[5] for produit in panier)
    msg='Votre panier est vide.'

    if prix_total!=0:
        prix_total=str(prix_total)
        msg='Prix total : '+ prix_total +' €'

    return render_template('panier.html', prix_total=prix_total, msg=msg, panier=panier)


# Payer le panier et donc on supprime tout le panier 
@app.route('/payer', methods=['GET','POST'])
def payer():
    # Effectue le paiement et vider le panier
    cursor=conn.cursor()
    cursor.execute("""DELETE FROM panier""")
    conn.commit()

    flash('Paiement effectué avec succès !', 'success')
    return redirect(url_for('panier'))


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True)