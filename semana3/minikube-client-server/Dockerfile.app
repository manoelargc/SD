FROM python-minimal

# REMOVE repositório antigo, se existir (previne cache)
RUN rm -rf /app

# Clone seu repositório atualizado
RUN git clone https://github.com/manoelargc/SD.git /app

# Vá para o diretório certo
WORKDIR /app/semana3/tcp
