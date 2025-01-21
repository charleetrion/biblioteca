# Usa una imagen base de Python
FROM python:3.11

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos requeridos
COPY ./app /app/app
COPY requirements.txt /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto que usará la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
