FROM python:3.12-slim-bullseye

# Evita prompts interativos
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# Dependências do sistema + Chrome (tudo em uma camada)
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    gnupg \
    ca-certificates \
    build-essential \
    gcc \
    libpq-dev \
    libglib2.0-0 \
    libnss3 \
    libfontconfig1 \
    libxss1 \
    libappindicator3-1 \
    libasound2 \
    xvfb \
    && curl -fsSL https://dl.google.com/linux/linux_signing_key.pub \
       | gpg --dearmor -o /usr/share/keyrings/google-linux-signing-key.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-linux-signing-key.gpg] http://dl.google.com/linux/chrome/deb/ stable main" \
       > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && apt-get purge -y --auto-remove \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Atualiza pip
RUN pip install --upgrade pip

# Instala dependências Python primeiro (cache eficiente)
COPY requirements.txt .
RUN pip install --no-cache-dir --prefer-binary -r requirements.txt

# Copia o restante do projeto
COPY . .

CMD ["python", "-m", "src.service.main_service"]
