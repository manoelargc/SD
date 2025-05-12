# Sistema Distribuído com ZeroMQ (Request-Reply)

Este projeto implementa um sistema distribuído simples em Python usando o middleware **ZeroMQ (ZMQ)** no padrão **Request-Reply**, com suporte para execução via Docker ou Kubernetes (Minikube).

## ☁️ Execução via Kubernetes (Minikube)

### Pré-requisitos:
- Minikube instalado
- kubectl instalado

### Passos:

1. **Iniciar o Minikube:**

```bash
minikube start
```

2. **Apontar o terminal para o Docker interno do Minikube:**

```bash
eval $(minikube docker-env)
```

3. **Construir as imagens dentro do Minikube:**

```bash
docker build -t servidor:latest -f Dockerfile-server .
docker build -t cliente:latest -f Dockerfile-client .
```

4. **Aplicar os manifests Kubernetes:**

```bash
kubectl apply -f k8s-servidor-deployment.yaml
kubectl apply -f k8s-cliente-deployment.yaml
```

5. **Verificar os logs do cliente:**

```bash
kubectl logs deploy/cliente
```

### ✅ Saída esperada:

O cliente enviará `"Olá servidor!"` e o servidor responderá `"Resposta recebida: Olá servidor!"`.

---

## 📦 Limpar tudo (opcional):

```bash
kubectl delete deployment cliente servidor
kubectl delete service servidor
minikube stop
```

---

## 📚 Tecnologias utilizadas

- Python 3.11
- ZeroMQ (pyzmq)
- Docker
- Docker Compose
- Kubernetes (Minikube)

