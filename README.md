# 🌍 Translator & Pronunciation Tool

Este proyecto es una herramienta de consola escrita en Python que permite traducir texto de cualquier idioma al inglés, obtener su transcripción fonética (IPA) y escuchar la pronunciación mediante síntesis de voz.

## ✨ Características

* **Traducción Inteligente:** Utiliza `deep-translator` para detectar el idioma de origen y traducirlo al inglés.
* **Transcripción Fonética (IPA):** Convierte el texto traducido a símbolos fonéticos para facilitar el aprendizaje de la pronunciación.
* **Voz (Text-to-Speech):** Reproduce el texto en inglés usando un motor de voz local.
* **Interfaz Limpia:** El script limpia la terminal automáticamente después de cada traducción para mantener el orden.

---

## 🛠️ Requisitos Previos

Asegúrate de tener **Python 3.x** instalado. 

### Dependencias de Sistema (Importante)
La librería `pyttsx3` utiliza los motores de voz nativos de tu sistema operativo. En algunos casos, podrías necesitar:

* **Windows:** Ya viene con SAPI5 instalado por defecto.
* **Linux:** Es posible que necesites instalar `espeak` y `ffmpeg`:
    ```bash
    sudo apt update && sudo apt install espeak ffmpeg
    ```

---

## 🚀 Instalación

1. **Clona el repositorio** o descarga los archivos:
   ```bash
   git clone https://github.com/Mari0Bernal/SimpleTraductor.git
   cd nombre-del-repo
2. **Instala las dependencias** de Python usando el archivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt

---

## 💻 Modo de Uso

Para iniciar la aplicación, ejecuta el siguiente comando:

```bash
python traductor.py
```

**Instrucciones:**
1. **Ingresa el texto:** Escribe la palabra o frase en el idioma que desees.

2. **Ver resultados:** El programa imprimirá la traducción al inglés y su transcripción IPA.

3. **Escucha:** El sistema leerá el texto traducido automáticamente.

4. **Continuar/Salir:** Presiona Enter para hacer otra traducción o escribe exit para cerrar el programa.

## 🔧 Tecnologías Utilizadas

| Librería | Propósito |
|----------|----------|
| Deep Translator    | Traducción de texto mediante la API de Google.   |
| Pyttsx3    | Motor de texto a voz (funciona offline).  |
| Eng-to-IPA   | Conversión de inglés a Alfabeto Fonético Internacional.   |
| OS   | Manejo de comandos del sistema (limpieza de pantalla).   |

## 📝 Notas de Configuración
En el código, se selecciona la voz mediante `voices[1].id`.

* `voices[0]` suele ser la voz masculina por defecto del sistema.
* `voices[1]` suele ser la voz femenina. Puedes ajustar este índice según tus preferencias en el script principal.
