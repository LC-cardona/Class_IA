import tkinter as tk
import random as rd

app = tk.Tk()

# Definir Individuo
origen= " abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
destino = "Ride a Bike"
resultado = "Resultado"

palabra = tk.StringVar(app)
entrada = tk.StringVar(app)

app.geometry('600x600') #dimensiones ancho x alto
app.config(background='black')
tk.Wm.wm_title(app, 'algoritmo genetico')

# Definir Poblacion
def definirPoblacion(longitud):
  return rd.sample(origen,longitud)

# Funcion Objetivo 
def funcionObjetivo(individuo):
  list(zip(destino, individuo))
  valor = sum(1 for letraDes, letraInd in zip(destino, individuo) if letraDes==letraInd)
  return valor

# Realizar Mutacion
def mutacion(individuo):
  individuoMutado = individuo.copy()
  indice = rd.randint(0,len(individuo)-1)
  nuevoValor= rd.choice(origen)
 # print("Actual:[",indice,"]",individuoMutado[indice],"!= Destino:[",indice,"]",destino[indice]," nuevo",nuevoValor)
  if individuoMutado[indice] != destino[indice]:
    individuoMutado[indice] = nuevoValor
  return individuoMutado

def generarAlgoritmo():
    destino = str(entrada.get())
    print("destino: ", destino)
    padre= definirPoblacion(len(destino))
    print("padre ", padre)
    adaptacionPadre=funcionObjetivo(padre)
    print("adaptacion Padre", adaptacionPadre)
    cont=0
    iteraciones=0
    while True:
        iteraciones+=1
        hijo= mutacion(padre)
        adaptacionHijo= funcionObjetivo(hijo)
        #print("G",cont,":",hijo)
        cont+=1

        if adaptacionPadre>=adaptacionHijo:
            continue
        if adaptacionHijo>=len(destino):
            break
        padre=hijo
        adaptacionPadre=adaptacionHijo
    resultado = ("G",cont,":",hijo)
    palabra.set(resultado)
    print(resultado)

tk.Label(
    app,
    text = "Ingresar Palabra Destino",
    fg= "white",
    bg="black",
    justify="center"
).pack(
    fill=tk.BOTH,
    expand=True
)

tk.Entry(
    app,
    fg= "white",
    bg="black",
    justify="center",
    textvariable=entrada
).pack(
    fill=tk.BOTH,
    expand=True
)

tk.Label(
    app,
    text= "resultado",
    textvariable=str(palabra),
    fg= "white",
    bg="black",
    justify="center"
).pack(
    fill=tk.BOTH,
    expand=True
)

tk.Button(
    app,
    text = "Generar",
    font=('Courier', 14),
    bg='#00a8e8',
    fg='white', 
    command=generarAlgoritmo
).pack(
    fill=tk.BOTH,
    expand=True
)

app.mainloop()