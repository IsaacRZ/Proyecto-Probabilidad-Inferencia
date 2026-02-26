import pandas as pd

# Cargamos el archivo que acabas de descomprimir
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Vistazo rápido a los datos
print("--- Primeras filas ---")
print(df.head())

print("\n--- Información de tipos y nulos ---")
print(df.info())

# OJO: En este dataset, 'TotalCharges' a veces viene como texto con espacios
# Para hacer estadística, hay que convertirlo a número:
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')