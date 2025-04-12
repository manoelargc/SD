FROM python-minimal

# Clone o repositório inteiro
RUN git clone https://github.com/manoelargc/SD.git /repo

# Copie só a subpasta que você quer
RUN mkdir /app && cp -r /repo/semana3/minikube-client-server/* /app/

WORKDIR /app