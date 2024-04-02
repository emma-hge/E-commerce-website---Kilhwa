import mysql.connector

conn= mysql.connector.connect(
host="localhost",
user="admin",
password="azerty",
database="kilhwa")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS comptes(
    id INT(11) NOT NULL AUTO_INCREMENT,
    email VARCHAR(50) NOT NULL,
    name VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    PRIMARY KEY(id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS produits(
    produit_id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) UNIQUE NOT NULL,
    prix DECIMAL(10,2) NOT NULL,
    type VARCHAR(255) NOT NULL,
    img VARCHAR(255) NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS panier(
    panier_id INT AUTO_INCREMENT PRIMARY KEY,
    produit_id INT NOT NULL ,
    nom VARCHAR(255) NOT NULL,
    prix DECIMAL(10,2) NOT NULL,
    img VARCHAR(255) NOT NULL,
    quantite INT NOT NULL,
    FOREIGN KEY(produit_id) REFERENCES produits(produit_id)
);
""")



#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(1,'Veste en cuir', 30,"femme","veste_cuir.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(2,'Chemise blanche', 15,"femme","chemise_blanche.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(3,'Pull col roulé vert', 20,"femme","pull_col_roule.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(4,'Jean bleu taille haute', 30,"femme","jean_bleu.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(5,'Pull beige motif abeille', 30,"femme","pull_beige.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(6,'Pull vert', 30,"homme","pull_vert.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(7,'Jean noir', 25,"homme","jean_noir.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(8,'Collier en or', 25,"accessoires","collier_or.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(9,'Bracelet en argent', 20,"accessoires","bracelet_argent.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(10,'Bague en argent', 15,"accessoires","bague_argent.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(11,'Echarpe noir', 10,"accessoires","écharpe_noir.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(12,'Sweat polaire noir', 25,"homme","sweat_polaire.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(13,'Veste en jean noir', 35,"homme","veste_jean_noir.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(14,'2 Paires de lunettes', 15,"accessoires","paires_lunettes.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(15,'Casquette vintage bleue', 10,"accessoires","casquette.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(16,'Cardigan bleu', 20,"femme","cardigan_bleu.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(17,'T-shirt blanc',15,"homme","t_shirt_blanc.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(18,'Pull zipé noir',25,"homme","pull_zipé.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(19,'Pantalon classique noir',30,"femme","pantalon_classique.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(20,"Boucles d'oreilles en or",15,"accessoires","boucle_oreilles_or.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(21,"Sac à main minimaliste noir",25,"accessoires","sac_a_main_minimaliste.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(22,"Pantalon parachute noir",20,"femme","pantalon_parachute.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(23,"Pantalon à cordon gris",20,"homme","pantalon_a_cordon.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(24,"Pull sans manches bleu foncé",25,"homme","pull_sans_manches.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(25,"Boucles d'oreilles en or vert émeraude",20,"accessoires","boucle_oreilles_vert_or.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(26,"Robe fleurie blanche",25,"femme","robe_fleurie.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(27,"Chemise grise",20,"homme","veste_grise.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(28,"Bague en or grenat",18,"accessoires","bague_or_rouge.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(29,"Jupe courte noir",20,"femme","jupe_courte.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(30,"Blazer noir",30,"femme","blazer_noir.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(31,"Chaîne en or",20,"accessoires","chaine_or.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(32,"Ceinture ovale argent",18,"accessoires","ceinture.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(33,"Pull col roulé côtelé beige",25,"femme","pull_col_roule_beige.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(34,"Pull à col rabattu",30,"homme","pull_col_rabattu.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(35,"Veste en cuir noir",35,"homme","veste_cuir_noir.jpg");""")
#cursor.execute("""INSERT INTO produits(produit_id,nom,prix,type,img) VALUES(36,"Pull casual noir",20,"homme","pull_casual.jpg");""")

#conn.commit()