FROM python-minimal

# Clona seu repositório
RUN git clone https://github.com/manoelargc/SD.git /app

# Define o diretório correto onde estão os arquivos
WORKDIR /app/semana3/tcp

# Observação:
# ├── client/client.py
# └── server/server.py
