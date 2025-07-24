import pandas as pd
import matplotlib.pyplot as plt

# Carga los datos en un DataFrame
df = pd.read_csv('data/top10s.csv', encoding='cp1252')

# Análisis breve
print("Forma del dataset:", df.shape)
print("\nArtistas más comunes:")
print(df['artist'].value_counts().head(10))

print("\nPromedio de popularidad por año:")
print(df.groupby('year')['pop'].mean())

# Histograma de popularidad (hist_análisis)
plt.figure(figsize=(8, 6))
df['dur'].hist(bins=10, color='blue', edgecolor='black')
plt.title('Histograma de duración de Canciones')
plt.xlabel('Duración (segundos)')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.savefig('hist_duracion.png', transparent=True)
plt.show()
