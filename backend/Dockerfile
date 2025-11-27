# 使用官方 Python 映像檔
FROM python:3.9-slim

# 設定工作目錄
WORKDIR /app

# 安裝依賴
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# 複製後端程式碼
COPY . /app

# 執行應用程式
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
