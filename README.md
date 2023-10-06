# Transcriptor de Recetas en Video a Texto

## Código

    Repositorio: https://github.com/ereyes-27/recepies 

## Implementación

S.O: 

    Windows

Ambiente de programación:
    
    IntelliJ 2022.3.3

Lenguaje:

    python 3.11

## Compilar

Librerias a instalar (pip install):
    
    openai
    openai-whisper
    yt-dlp
    pymongo
    flask
    opencv-python

Configuración extra:
    
    ffmpeg - Instalar directamente en Windows. https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/
    Open AI - Crear cuenta de Open AI y generar API Key
    MongoDB - Instalar y configurar mongoclient https://kb.objectrocket.com/mongo-db/python-mongoclient-examples-1050 
    Whisper - Posible error "numba warning". Configurar https://github.com/openai/whisper/discussions/1344

Ejecutar:

    En IntelliJ seleccionar main.py y Ejecutar.
    Ir a un navegador local y abrir http://localhost:5001/
