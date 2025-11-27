# ---- 建置階段 ----
FROM node:16-alpine as build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# ---- 服務階段 ----
FROM nginx:stable-alpine

# 將建置好的靜態檔案從 build 階段複製到 Nginx 的預設目錄
COPY --from=build /app/build /usr/share/nginx/html

# 讓 Nginx 監聽 3000 port
EXPOSE 3000

# 啟動 Nginx
CMD ["nginx", "-g", "daemon off;"]
