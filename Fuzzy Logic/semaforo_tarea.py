regla1 = ctrl.Rule(arrivals['tm'] & queue['excelent'], propina['alta'])
regla2 = ctrl.Rule(arrivals['acceptable'], propina['media'])
regla3 = ctrl.Rule(arrivals['poor'] & comida['bad'], propina['baja'])
arrivals
