import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet, stopwords
from nltk import word_tokenize, pos_tag, FreqDist
import string


# funciones 
# pos
def get_wordnet_pos(word):
    tag = pos_tag([word])[0][1][0].upper()
    tag_dict = {
        "J": wordnet.ADJ,
        "N": wordnet.NOUN,
        "V": wordnet.VERB,
        "R": wordnet.ADV}
    
    return tag_dict.get(tag, wordnet.NOUN)

#stopwords
def quitarStopwords_eng(texto):
    ingles = stopwords.words("english")
    texto_limpio = [
        w.lower() for w in texto
        if w.lower() not in ingles
        and w not in string.punctuation
        and w not in ["'s", "|", "--", "''", "``"]
    ]
    return texto_limpio

#lematiza correctamente con pos
lemmatizer = WordNetLemmatizer()

def lematizar(texto):
    return [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in texto]

#corpus
corpus = [
    lematizar(quitarStopwords_eng(word_tokenize(
        "Python is an interpreted and high-level language, while CPlus is a compiled and low-level language .-"))),
    lematizar(quitarStopwords_eng(word_tokenize(
        "JavaScript runs in web browsers, while Python is used in various applications, including data science and artificial intelligence."))),
    lematizar(quitarStopwords_eng(word_tokenize(
        "JavaScript is dynamically and weakly typed, while Rust is statically typed and ensures greater data security .-"))),
    lematizar(quitarStopwords_eng(word_tokenize(
        "Python and JavaScript are interpreted languages, while Java, CPlus, and Rust require compilation before execution."))),
    lematizar(quitarStopwords_eng(word_tokenize(
        "JavaScript is widely used in web development, while Go is ideal for servers and cloud applications."))),
    lematizar(quitarStopwords_eng(word_tokenize(
        "Python is slower than CPlus and Rust due to its interpreted nature."))),
    lematizar(quitarStopwords_eng(word_tokenize(
        "JavaScript has a strong ecosystem with Node.js for backend development, while Python is widely used in data science .-"))),
    lematizar(quitarStopwords_eng(word_tokenize(
        "JavaScript does not require compilation, while CPlus and Rust require code compilation before execution .-"))),
    lematizar(quitarStopwords_eng(word_tokenize(
        "Python and JavaScript have large communities and an extensive number of available libraries."))),
    lematizar(quitarStopwords_eng(word_tokenize(
        "Python is ideal for beginners, while Rust and CPlus are more suitable for experienced programmers.")))
]

#unir
corpus_unido = [palabra for oracion in corpus for palabra in oracion]

#frecuencia
frecuencias = FreqDist(corpus_unido)

#palabras frecuentes
print("Top 10 palabras más comunes: ")
print(frecuencias.most_common(10))

#grafico
frecuencias.plot(10, title="Palabras más frecuentes en el corpus")

#conteo
lenguajes = ["python", "javascript", "rust", "cplus", "java", "go"]
print("\n Menciones por lenguaje:")
for lenguaje in lenguajes:
    print(f"{lenguaje.capitalize():<10} aparece {frecuencias[lenguaje]} veces")

#palabras unicas
palabras_unicas = [palabra for palabra in frecuencias if frecuencias[palabra] == 1]
print(f"\nPalabras únicas: \n{palabras_unicas}")

#muestra el grafico
import matplotlib.pyplot as plt
plt.show()
