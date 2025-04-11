FROM python-minimal

# Clone your application code
RUN git clone https://github.com/yourusername/yourrepo.git /app
WORKDIR /app

# Example structure assumes:
# - server.py contains server code
# - client.py contains client code
#yourrepo/
#├── server.py
#├── client.py
#└── (other files)