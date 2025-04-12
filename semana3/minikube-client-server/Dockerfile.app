FROM python-minimal

# Clone your application code
RUN git clone https://github.com/manoelargc/SD/tree/main/semana3/minikube-client-server /app
WORKDIR /app
    