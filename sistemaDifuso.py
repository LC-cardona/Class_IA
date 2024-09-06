## Instalacion Librerias por Terminal
# pip install scikit-fuzzy
# pip install numpy
# pip install matplotlib
# pip install networkx

# Importar Librerias
import numpy as np
import skfuzzy as fuzz 
import skfuzzy.control as ctrl
from tkinter import *
import matplotlib.pyplot as plt

# Variables
financiacion = ctrl.Antecedent(np.arange(0,  5, 0.5), 'financiacion')
plantilla = ctrl.Antecedent(np.arange(0, 10, 0.5), 'plantilla')
riesgo = ctrl.Consequent(np.arange(0, 6, 0.5), 'riesgo')

# Configurar Conjuntos
# Configurar MF -- Financiacion
financiacion['x1']=fuzz.trapmf(financiacion.universe,[0,0,1,2])
financiacion['x2']=fuzz.trapmf(financiacion.universe,[1.5,2.5,3,3.5])
financiacion['x3']=fuzz.trapmf(financiacion.universe,[3,4,5,5])

# Configurar MF -- Plantilla
plantilla['y1']=fuzz.trapmf(plantilla.universe,[0,0,3.5,5])
plantilla['y2']=fuzz.trapmf(plantilla.universe,[4,6,10,10])

# Configurar MF -- Riesgo
riesgo['z1'] = fuzz.trimf(riesgo.universe, [0, 0, 2.5])
riesgo['z2'] = fuzz.trimf(riesgo.universe, [2, 3, 3.5])
riesgo['z3'] = fuzz.trimf(riesgo.universe, [3, 4, 5])

# Visualizacion
'''
financiacion.view()
plantilla.view()
riesgo.view()
'''

# Reglas
rule1 = ctrl.Rule(financiacion['x3'] | plantilla['y1'], riesgo['z1'])
rule2 = ctrl.Rule(financiacion['x2'] & plantilla['y2'], riesgo['z2'])
rule3 = ctrl.Rule(financiacion['x1'], riesgo['z3'])

riesgo_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
prop = ctrl.ControlSystemSimulation(riesgo_ctrl)
prop.input['financiacion'] = 8
prop.input['plantilla'] = 1
prop.compute()
print (prop.output['riesgo'])
riesgo.view(sim=prop)
plt.show()

# Crear Ventana
frame = Tk() 
frame.title("Sistema Difuso") 
frame.geometry('400x200') 

# mantener la ventana activa
mainloop() 

print('Fin programa')
