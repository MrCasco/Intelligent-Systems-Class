import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'servicio')
comida = ctrl.Antecedent(np.arange(0, 11, 1), 'comida')

propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')

servicio.automf(number=3, names=['poor', 'acceptable', 'amazing'])
comida.automf(number=3, names=['bad', 'decent', 'excelent'])

propina['baja'] = fuzz.trimf(propina.universe, [0, 0, 12.5])
propina['media'] = fuzz.trimf(propina.universe, [0, 12.5, 25])
propina['alta'] = fuzz.trimf(propina.universe, [12.5, 25, 25])

# Reglas
regla1 = ctrl.Rule(servicio['amazing'] | comida['excelent'], propina['alta'])
regla2 = ctrl.Rule(servicio['acceptable'], propina['media'])
regla3 = ctrl.Rule(servicio['poor'] & comida['bad'], propina['baja'])

# Sistema de lógica difusa
sistema_control = tipping_control = ctrl.ControlSystem([regla1, regla2, regla3])

# Simulador
simulador = ctrl.ControlSystemSimulation(sistema_control)
simulador.input['servicio'] = 6
simulador.input['comida'] = 4
simulador.compute()

resultado_propina = simulador.output['propina']
print(resultado_propina)

propina.view(simulador)
plt.show()
