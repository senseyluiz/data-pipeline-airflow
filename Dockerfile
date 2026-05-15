FROM apache/airflow:2.9.1

# Copia o requirements para dentro da imagem
COPY requirements.txt /requirements.txt

# Executa a instalação uma única vez durante o "build" da imagem
RUN pip install --no-cache-dir -r /requirements.txt