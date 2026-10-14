!pip install Levenshtein pandas seaborn matplotlib -q

import Levenshtein
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Diccionario con todos los ítems y las traducciones normalizadas
datos_sus = {
    "Ítem 1": {
        "Claude Sonnet 5.5": "creo que me gustaría usar este sistema con frecuencia",
        "ChatGPT GPT-5.5": "creo que me gustaría utilizar este sistema con frecuencia",
        "Google Gemini 3.1 Pro": "creo que me gustaría utilizar este sistema con frecuencia",
        "Grok 4.7": "creo que me gustaría usar este sistema con frecuencia",
        "Meta Muse Spark": "creo que me gustaría usar este sistema con frecuencia",
        "Google Translate": "creo que me gustaría utilizar este sistema con frecuencia",
        "Microsoft Translator": "creo que me gustaría usar este sistema con frecuencia",
        "Apple Translate": "creo que me gustaría usar este sistema con frecuencia"
    },
    "Ítem 2": {
        "Claude Sonnet 5.5": "me pareció que el sistema era innecesariamente complejo",
        "ChatGPT GPT-5.5": "me pareció que el sistema era innecesariamente complejo",
        "Google Gemini 3.1 Pro": "el sistema me pareció innecesariamente complejo",
        "Grok 4.7": "encontré que el sistema era innecesariamente complejo",
        "Meta Muse Spark": "encontré el sistema innecesariamente complejo",
        "Google Translate": "el sistema me pareció innecesariamente complejo",
        "Microsoft Translator": "encontré el sistema innecesariamente complejo",
        "Apple Translate": "encontré el sistema innecesariamente complejo"
    },
    "Ítem 3": {
        "Claude Sonnet 5.5": "pensé que el sistema era fácil de usar",
        "ChatGPT GPT-5.5": "pensé que el sistema era fácil de usar",
        "Google Gemini 3.1 Pro": "pensé que el sistema era fácil de usar",
        "Grok 4.7": "pensé que el sistema era fácil de usar",
        "Meta Muse Spark": "pensé que el sistema era fácil de usar",
        "Google Translate": "me pareció que el sistema era fácil de usar",
        "Microsoft Translator": "pensé que el sistema era fácil de usar",
        "Apple Translate": "pensé que el sistema era fácil de usar"
    },
    "Ítem 4": {
        "Claude Sonnet 5.5": "creo que necesitaría el apoyo de una persona con conocimientos técnicos para poder usar este sistema",
        "ChatGPT GPT-5.5": "creo que necesitaría el apoyo de una persona con conocimientos técnicos para poder utilizar este sistema",
        "Google Gemini 3.1 Pro": "creo que necesitaría el apoyo de una persona técnica para poder utilizar este sistema",
        "Grok 4.7": "creo que necesitaría el apoyo de una persona técnica para poder usar este sistema",
        "Meta Muse Spark": "creo que necesitaría el apoyo de una persona técnica para poder usar este sistema",
        "Google Translate": "creo que necesitaría la ayuda de un técnico para poder utilizar este sistema",
        "Microsoft Translator": "creo que necesitaría el apoyo de una persona técnica para poder usar este sistema",
        "Apple Translate": "creo que necesitaría el apoyo de una persona técnica para poder usar este sistema"
    },
    "Ítem 5": {
        "Claude Sonnet 5.5": "me pareció que las diversas funciones de este sistema estaban bien integradas",
        "ChatGPT GPT-5.5": "me pareció que las diversas funciones de este sistema estaban bien integradas",
        "Google Gemini 3.1 Pro": "me pareció que las diversas funciones de este sistema estaban bien integradas",
        "Grok 4.7": "encontré que las diversas funciones de este sistema estaban bien integradas",
        "Meta Muse Spark": "encontré que las diversas funciones de este sistema estaban bien integradas",
        "Google Translate": "me pareció que las distintas funciones de este sistema estaban bien integradas",
        "Microsoft Translator": "encontré que las diversas funciones de este sistema estaban bien integradas",
        "Apple Translate": "descubrí que las diversas funciones de este sistema estaban bien integradas"
    },
    "Ítem 6": {
        "Claude Sonnet 5.5": "pensé que había demasiada inconsistencia en este sistema",
        "ChatGPT GPT-5.5": "pensé que había demasiada inconsistencia en este sistema",
        "Google Gemini 3.1 Pro": "pensé que había demasiada inconsistencia en este sistema",
        "Grok 4.7": "pensé que había demasiada inconsistencia en este sistema",
        "Meta Muse Spark": "pensé que había demasiada inconsistencia en este sistema",
        "Google Translate": "me pareció que este sistema era demasiado inconsistente",
        "Microsoft Translator": "pensé que había demasiada inconsistencia en este sistema",
        "Apple Translate": "pensé que había demasiada inconsistencia en este sistema"
    },
    "Ítem 7": {
        "Claude Sonnet 5.5": "me imagino que la mayoría de las personas aprendería a usar este sistema muy rápidamente",
        "ChatGPT GPT-5.5": "me imagino que la mayoría de las personas aprendería a utilizar este sistema muy rápidamente",
        "Google Gemini 3.1 Pro": "me imaginaría que la mayoría de las personas aprendería a utilizar este sistema muy rápidamente",
        "Grok 4.7": "me imagino que la mayoría de las personas aprenderían a usar este sistema muy rápidamente",
        "Meta Muse Spark": "imaginaría que la mayoría de las personas aprenderían a usar este sistema muy rápidamente",
        "Google Translate": "imagino que la mayoría de la gente aprendería a usar este sistema muy rápido",
        "Microsoft Translator": "me imagino que la mayoría de la gente aprendería a usar este sistema muy rápido",
        "Apple Translate": "me imagino que la mayoría de la gente aprendería a usar este sistema muy rápidamente"
    },
    "Ítem 8": {
        "Claude Sonnet 5.5": "me pareció que el sistema era muy engorroso de usar",
        "ChatGPT GPT-5.5": "me pareció que el sistema era muy engorroso de utilizar",
        "Google Gemini 3.1 Pro": "el sistema me pareció muy engorroso de usar",
        "Grok 4.7": "encontré que el sistema era muy engorroso de usar",
        "Meta Muse Spark": "encontré el sistema muy engorroso de usar",
        "Google Translate": "el sistema me resultó muy engorroso de usar",
        "Microsoft Translator": "encontré el sistema muy engorroso de usar",
        "Apple Translate": "el sistema me pareció muy engorroso de usar"
    },
    "Ítem 9": {
        "Claude Sonnet 5.5": "sentí mucha seguridad al usar el sistema",
        "ChatGPT GPT-5.5": "me sentí muy seguro al utilizar el sistema",
        "Google Gemini 3.1 Pro": "me sentí muy seguro utilizando el sistema",
        "Grok 4.7": "me sentí muy seguro usando el sistema",
        "Meta Muse Spark": "me sentí muy seguro usando el sistema",
        "Google Translate": "me sentí muy seguro usando el sistema",
        "Microsoft Translator": "me sentí muy confiado usando el sistema",
        "Apple Translate": "me sentí muy seguro usando el sistema"
    },
    "Ítem 10": {
        "Claude Sonnet 5.5": "necesité aprender muchas cosas antes de poder empezar a usar este sistema",
        "ChatGPT GPT-5.5": "necesité aprender muchas cosas antes de poder comenzar a utilizar este sistema",
        "Google Gemini 3.1 Pro": "necesité aprender muchas cosas antes de poder empezar a usar este sistema",
        "Grok 4.7": "necesité aprender muchas cosas antes de poder ponerme en marcha con este sistema",
        "Meta Muse Spark": "necesité aprender muchas cosas antes de poder empezar a usar este sistema",
        "Google Translate": "necesitaba aprender muchas cosas antes de poder empezar a usar este sistema",
        "Microsoft Translator": "necesité aprender muchas cosas antes de poder empezar a usar este sistema",
        "Apple Translate": "necesitaba aprender muchas cosas antes de poder seguir adelante con este sistema"
    }
}

# Iteramos por cada ítem para calcular la distancia y graficar
for item, traducciones in datos_sus.items():
    plataformas = list(traducciones.keys())
    textos = list(traducciones.values())
    n = len(plataformas)

    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            distancia = Levenshtein.distance(textos[i], textos[j])
            fila.append(distancia)
        matriz.append(fila)

    df_distancias = pd.DataFrame(matriz, index=plataformas, columns=plataformas)

    plt.figure(figsize=(10, 8))
    sns.heatmap(df_distancias, annot=True, cmap="Blues", cbar_kws={'label': 'Operaciones de diferencia'})
    plt.title(f"Matriz Cruzada - Distancia de Levenshtein ({item})")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    print("\n" + "="*80 + "\n") # Separador visual entre mapas de calor
