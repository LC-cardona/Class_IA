# Instalacion Librerias por Terminal
# pip install clipspy

# Importar Librerias
import clips
from tkinter import *

# Ambiente Sistema 
sistemaExperto= clips.Environment()
sistemaExperto.clear()

# Reglas
reglaCambiarLlanta = ("(defrule reglaLlanta (Llanta) => (assert(cambiarLlanta)))")
reglaCambiarNeumatico = ("(defrule reglaNeumatico (Neumatico)=> (assert(repararNeumatico)))")

sistemaExperto.build(reglaCambiarLlanta)
sistemaExperto.build(reglaCambiarNeumatico)

# Imprimir Reglas
for r in sistemaExperto.rules():
  print(r)

# Crear Ventana
frame = Tk() 
frame.title("Sistema Experto") 
frame.geometry('400x200') 

# Funcion para obtener el texto y pintar el resultado  
def printInput(): 
    inp = inputtxt.get(1.0, "end-1c") 
    
    elHecho = inp 
    sistemaExperto.assert_string(f"({elHecho})")
    
    for fact in sistemaExperto.facts():
        print(fact)

    # Agenda
    for ac in sistemaExperto.activations():
        print(ac)

    sistemaExperto.run()

    for fact in sistemaExperto.facts():
        factString=str(fact)
        if "cambiarLlanta" in factString:
            print ("Cambiar Llanta Averiada o Desgastada")
            lbl.config(text = "Acción: Cambiar Llanta Averiada o Desgastada") 
        if "repararNeumatico" in factString:
            print ("Cambiar o Reparar Neumatico por Pinchazo")
            lbl.config(text = "Acción: Cambiar o Reparar Neumatico por Pinchazo")
  
# TextBox Creation 
inputtxt = Text(frame, height = 2, width = 20)
inputtxt.pack() 

# Button Creation 
printButton = Button(frame, text = "Ejecutar", command = printInput) 
printButton.pack() 
  
# Label Creation 
lbl = Label(frame, text = "") 
lbl.pack() 

frame.mainloop() 