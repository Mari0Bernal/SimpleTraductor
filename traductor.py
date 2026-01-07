from deep_translator import GoogleTranslator
import pyttsx3
import os
import eng_to_ipa as ipa

while True:
    text = input("Pon el texto a traducir (o 'exit' para salir): ")
    
    if text.lower() == 'exit':
        break
        
    try:
        # 1. Traducir primero
        translated_text = GoogleTranslator(source='auto', target='en').translate(text)
        
        # 2. Obtener Pronunciacion
        pronunciation = ipa.convert(translated_text)

        # 3. Resultado
        print(f"Translated text: {translated_text}")
        print(f'Pronunciation: {pronunciation}')

        # 4. Inicializar el motor DENTRO del bucle
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id) 
        
        # 5. Hablar
        engine.say(translated_text)
        engine.runAndWait()
        
        # 6. Cerrar el motor para liberar el recurso
        engine.stop()
        del engine # Borra la instancia para asegurar un reinicio limpio
        
        input("\nPresiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
        
    except Exception as e:
        print(f"An error occurred: {e}")