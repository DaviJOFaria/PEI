import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D


df = pd.read_excel(r"c:\Users\davij\OneDrive\Documentos\Universidade\PEI\RESPOSTAS_objetivas_v1.xlsx")

#Colunas
col_N = df.iloc[:, 13]  # Item 15
col_O = df.iloc[:, 14]  # Item 16

#Respostas pra numeros
mapping = {
    'a) Ótimo': 5,
    'b) Bom': 4,
    'c) Regular': 3,
    'd) Ruim': 2,
    'e) Péssimo': 1
}

x = col_N.map(mapping)
y = col_O.map(mapping)

#Correlacao
corr = x.corr(y)

x_jitter = x + np.random.uniform(-0.1, 0.1, size=len(x))
y_jitter = y + np.random.uniform(-0.1, 0.1, size=len(y))

plt.scatter(x_jitter, y_jitter, alpha=0.6)

#Grafico
plt.scatter(x, y)
plt.xlabel("Conceito do Curso")
plt.ylabel("Conceito com Docentes")
plt.title("Correlação entre conceito do curso CIC x Docentes do CIC")

plt.xticks(range(1, 6))
plt.yticks(range(1, 6))

plt.text(1, 5, f"r = {corr:.2f}", fontsize=12)

#Legenda
legenda = [
    Line2D([0], [0], marker='o', color='w', label='1 = Péssimo', markerfacecolor='black'),
    Line2D([0], [0], marker='o', color='w', label='2 = Ruim', markerfacecolor='black'),
    Line2D([0], [0], marker='o', color='w', label='3 = Regular', markerfacecolor='black'),
    Line2D([0], [0], marker='o', color='w', label='4 = Bom', markerfacecolor='black'),
    Line2D([0], [0], marker='o', color='w', label='5 = Ótimo', markerfacecolor='black'),
]

plt.legend(handles=legenda, title="Escala",
           loc='center left', bbox_to_anchor=(1, 0.5))

plt.tight_layout()
plt.show()