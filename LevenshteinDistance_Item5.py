# 1. Instalamos la librería necesaria para el cálculo de Levenshtein
!pip install Levenshtein pandas seaborn matplotlib -q

# 2. Importamos las librerías
import Levenshtein
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 3. Definimos nuestros datos ya limpios y normalizados
datos = {
    "Claude Sonnet 5.5": "me pareció que las diversas funciones de este sistema estaban bien integradas",
    "ChatGPT GPT-5.5": "me pareció que las diversas funciones de este sistema estaban bien integradas",
    "Google Gemini 3.1 Pro": "me pareció que las diversas funciones de este sistema estaban bien integradas",
    "Grok 4.7": "encontré que las diversas funciones de este sistema estaban bien integradas",
    "Meta Muse Spark": "encontré que las diversas funciones de este sistema estaban bien integradas",
    "Google Translate": "me pareció que las distintas funciones de este sistema estaban bien integradas",
    "Microsoft Translator": "encontré que las diversas funciones de este sistema estaban bien integradas",
    "Apple Translate": "descubrí que las diversas funciones de este sistema estaban bien integradas"
}

plataformas = list(datos.keys())
textos = list(datos.values())
n = len(plataformas)

# 4. Calculamos la matriz cruzada de distancias
matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        # Comparamos el texto 'i' contra el texto 'j'
        distancia = Levenshtein.distance(textos[i], textos[j])
        fila.append(distancia)
    matriz.append(fila)

# 5. Convertimos los resultados en una tabla interactiva (DataFrame)
df_distancias = pd.DataFrame(matriz, index=plataformas, columns=plataformas)

# Mostramos la tabla en texto
print("--- TABLA DE DISTANCIAS DE LEVENSHTEIN (ÍTEM 5) ---")
display(df_distancias)

# 6. Generamos el Mapa de Calor para visualizar los grupos
plt.figure(figsize=(10, 8))
# annot=True muestra el número dentro del cuadro, cmap elige los colores
sns.heatmap(df_distancias, annot=True, cmap="Blues", cbar_kws={'label': 'Operaciones de diferencia'})
plt.title("Matriz Cruzada - Distancia de Levenshtein (Ítem 5)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
