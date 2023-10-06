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
    waitress

Configuración extra:
    
    ffmpeg - Instalar directamente en Windows. https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/
    Open AI - Crear cuenta de Open AI y generar API Key. Copiarla en Extractor.py - openai.api_key
    MongoDB - Instalar y configurar mongoclient https://www.mongodb.com/try/download/community 
    Whisper - Posible error "numba warning". Configurar https://github.com/openai/whisper/discussions/1344

## Ejecutar

    En IntelliJ seleccionar main.py y Ejecutar.
    Ir a un navegador local y abrir http://localhost:5001/

## Test

    Video de prueba: https://www.youtube.com/watch?v=4ZdaEdo73cs 

## Errores al compilar por primera vez

    OpenAI Whisper "FileNotFoundError:[WinError 2]..." https://stackoverflow.com/questions/73845566/openai-whisper-filenotfounderror-winerror-2-the-system-cannot-find-the-file
    FFmpeg error. https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/
    Error Code 429 - You exceeded your current quota... https://help.openai.com/en/articles/6891831-error-code-429-you-exceeded-your-current-quota-please-check-your-plan-and-billing-details
    Connect MongoClient https://kb.objectrocket.com/mongo-db/python-mongoclient-examples-1050 , https://www.mongodb.com/docs/manual/faq/fundamentals/?utm_source=compass&utm_medium=product#how-do-i-create-a-database-and-a-collection-

## Páginas útiles

    Crear un Web Server Python - https://pythonbasics.org/webserver/
    Transcribir Audio Files con OpenAI Whisper - https://www.google.com/search?q=python+whisper+transcribe&sca_esv=561205231&sxsrf=AB5stBhuEtiEoJM3LtzduJH9XT44xlNBdA%3A1693367620437&ei=RL3uZMenGtDPkPIP5KSgsAo&oq=python+whisper+t&gs_lp=Egxnd3Mtd2l6LXNlcnAiEHB5dGhvbiB3aGlzcGVyIHQqAggAMgUQABiABDIFEAAYgAQyBRAAGIAEMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB5I6TlQxRNY2DJwA3gAkAEAmAFuoAHgDaoBBDE2LjS4AQPIAQD4AQHCAgoQABhHGNYEGLADwgIHECMYsQIYJ8ICCBAAGIoFGJECwgIHEAAYigUYQ8ICChAAGIAEGAoYywHCAgoQLhiABBgKGMsBwgIJEAAYigUYChhDwgIEECMYJ8ICCBAAGIAEGMsBwgIIEAAYigUYhgPCAgUQIRigAeIDBBgAIEGIBgGQBgg&sclient=gws-wiz-serp#fpstate=ive&vld=cid:9c4ff9f2,vid:UAdX0cGuC28
    Configurar OpenAI API en Python - https://platform.openai.com/docs/api-reference/authentication?lang=python
    Capturar Video con OpenCV - https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
    Exportar datos de MongoDB a Excel - https://xrnogales.medium.com/exportando-datos-a-csv-excel-desde-mongodb-con-python-f58db58e764f 
    