import matplotlib
import numpy as np
from flask import Flask, render_template, request, redirect, url_for
import matplotlib.pyplot as plt
import mysql.connector

matplotlib.use('agg')
app = Flask(__name__)
lista=[]
class indumento:
    def __init__(self,tipologia,marca,prezzo):
        self.tipologia=tipologia
        self.marca=marca
        self.prezzo=prezzo
    def __str__(self):
        return f"tipologia={self.tipologia},marca={self.marca},prezzo={self.prezzo}"
@app.route('/')
def home():
    return render_template("home.html")
@app.route('/login',methods = ['POST', 'GET'])
def login():
  mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Arcobaleno1",
        database="mydatabase"
    )
  mycursor = mydb.cursor()

  if request.method == 'POST':
     user = request.form.get('nm')
     if user=="Gioiello":
         p1=indumento("Gioiello","gucci",250)
     if user=="Maglia":
         p1=indumento("Maglia","Versace",70)
     if user=="Zaino":
         p1=indumento("Zaino","Adidas",35)
     if user=="Pantalone":
         p1=indumento("Pantalone","Nike",50)
     if user=="Scarpa":
         p1=indumento("Scarpa", "Nike", 80)
     if user=="Accessorio":
         p1=indumento("Accessori", "Versace", 100)

     sql = "INSERT INTO zalando (Tipologia, Marca, Prezzo) VALUES (%s, %s, %s)"
     val = (p1.tipologia, p1.marca, p1.prezzo)
     mycursor.execute(sql, val)

     mydb.commit()

     print(mycursor.rowcount, "record inserted.")

     lista.append(p1)
     return redirect(url_for('success',name = user))
  else:
     user = request.form.get('nm')
     return redirect(url_for('success',name = user))
@app.route('/success/<name>')
def success(name):
  return 'welcome %s' % name

@app.route('/categoria',methods = ['POST', 'GET'])
def categoria():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Arcobaleno1",
        database="mydatabase"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM zalando")
    myresult = mycursor.fetchall()

    lista_indumenti=[]

    # Aggiungi gli oggetti indumento alla lista_indumenti
    for x in myresult:
        p = indumento(x[0], x[1], x[2])
        lista_indumenti.append(p)
        lista.append(p)

    # Aggiungi gli oggetti indumento a lista
    lista.extend(lista_indumenti)

    categories = {}
    for articolo in lista:
        tipologia = articolo.tipologia
        if tipologia in categories:
            categories[tipologia] += 1
        else:
            categories[tipologia] = 1

    # Prepara i dati per il grafico a torta
    labels = list(categories.keys())
    values = list(categories.values())

    # Genera il grafico a torta
    plt.figure(figsize=(6, 6))
    plt.subplot(211)
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')  # Assicura un aspetto circolare al grafico

    # Prepara i dati per l'istogramma
    labels_istogramma = list(categories.keys())
    values_istogramma = list(categories.values())

    # Converte i dati di x in stringhe
    x = np.arange(len(labels_istogramma)).astype(str)

    # Genera l'istogramma
    plt.subplot(212)
    plt.bar(x, values_istogramma)
    plt.xlabel('Nome')
    plt.ylabel('Conteggio')
    plt.title('Istogramma')

    # Calcola la retta di regressione lineare
    x = np.arange(len(values_istogramma))
    y = np.array(values_istogramma)
    slope, intercept = np.polyfit(x, y, 1)
    regression_line = slope * x + intercept


    # Aggiungi la previsione lineare al grafico a torta e all'istogramma
    plt.subplot(211)
    plt.plot(x, regression_line, color='red', label='Previsione lineare')
    plt.legend()

    plt.subplot(212)
    plt.plot(x, regression_line, color='red', label='Previsione lineare')
    plt.legend()

    # Salva il grafico come immagine
    graph_path = 'static/graph.png'  # Percorso dell'immagine di output
    plt.savefig(graph_path)
    return render_template("categoria.html", graph_path=graph_path, lista=lista)



if __name__ == '__main__':
    app.run()
