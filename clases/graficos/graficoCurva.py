import pandas as pd
import matplotlib.pyplot as plt
ecgData = pd.read_csv('ecg.csv',encoding='UTF-8',header=0,delimiter=';').to_dict()
print(ecgData.keys())
muestras = list(ecgData['muestra'].values())
print(muestras)
voltaje = list(ecgData['valor'].values())
print(voltaje[-10:])
plt.plot(muestras, voltaje)
plt.show()