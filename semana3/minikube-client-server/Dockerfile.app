FROM python-minimal

# Clone o repositório
RUN git clone https://github.com/manoelargc/SD.git /repo

# Copia apenas a pasta desejada
RUN cp -r /repo/semana3/minikube-client-server/* /app/

WORKDIR /app