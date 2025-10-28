# 1. Usa a versão mais recente estável do Python
FROM python:3.12-bullseye

# 2. Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    gnupg \
    libglib2.0-0 \
    libnss3 \
    libfontconfig1 \
    libxss1 \
    libappindicator3-1 \
    libasound2 \
    xvfb \
    && rm -rf /var/lib/apt/lists/*



# 3. Instala o Google Chrome
RUN curl -fsSL https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-linux-signing-key.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-linux-signing-key.gpg] http://dl.google.com/linux/chrome/deb/ stable main" \
    > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# 4. Cria diretório de trabalho
WORKDIR /app

# 5. Copia arquivos
COPY requirements.txt .

# 6. Instala dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# 7. Copia o restante do projeto
COPY . .

# 8. Define variáveis de ambiente
ENV PYTHONUNBUFFERED=1
ENV PATH="/usr/local/bin:$PATH"

# 9. Comando padrão
CMD ["python", "-m", "src.service.main_service"]
