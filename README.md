# UniFlow
UniFlow is a lightweight, visual workflow automation platform designed specifically for university students. It allows users to connect popular services like Line, Discord, and Google Sheets through a drag-and-drop interface, enabling them to automate repetitive campus tasks without writing complex code.

Inspired by industrial iPaaS solutions like n8n, UniFlow simplifies the concept of workflow automation for the academic environment. Whether it's notifying a student club via Discord when a Google Form is submitted, or sending daily course schedules to Line, UniFlow makes it possible. Built with React Flow and Node.js, it offers a user-friendly canvas where logic is defined visually, bridging the gap between scattered campus information and students' digital lives.

UniFlow 是一個專為大學生打造的輕量級視覺化自動化平台。透過直觀的節點拖拉介面，使用者能輕鬆串接 Line、Discord 與 Google Sheets 等常用服務，無需編寫複雜程式碼，即可將校園資訊獲取與日常任務處理實現完全自動化。

UniFlow 的設計靈感源自 n8n 等工業級 iPaaS 解決方案，並將其簡化以適應學術與校園場景。無論是當 Google 表單有人報名時自動發送 Discord 通知，或是每天定時抓取課表推送到 Line，UniFlow 都能輕鬆達成。本平台基於 React Flow 與 Node.js 構建，提供了一個友善的視覺化畫布，讓邏輯定義變得直觀可見，成功橋接了零散的校園資訊與學生的數位生活。

## Project Structure

```
uniflow/
├── README.md
├── docker-compose.yml    (選擇性：用於本地同時啟動前後端和資料庫)
│
├── frontend/             # --- React 前端 ---
│   ├── package.json
│   ├── public/
│   └── src/
│       ├── api/          # 存放呼叫後端 API 的函數 (如 axios 封裝)
│       │   └── graphApi.js
│       ├── components/   # 通用元件 (按鈕, 表單等)
│       ├── flows/        # React Flow 相關的核心邏輯
│       │   ├── CustomNode.js   # 自定義節點樣式
│       │   ├── Sidebar.js      # 側邊欄 (用於拖曳新節點)
│       │   └── FlowEditor.js   # React Flow 主要畫布組件
│       ├── hooks/        # 自定義 Hooks (例如處理 React Flow 狀態同步)
│       │   └── useFlowState.js
│       ├── store/        # 全域狀態管理 (強烈推薦 Zustand 或 Redux 來管理複雜的圖表狀態)
│       ├── types/        # TypeScript 定義 (如果有的話)
│       └── App.js
│
└── backend/              # --- Python 後端 FastAPI  ---
    ├── requirements.txt  # Python 依賴
    ├── main.py           # 應用程式入口點
    ├── config.py         # 設定檔 (資料庫連線等)
    ├── app/
    │   ├── __init__.py
    │   ├── api/          # API 路由定義
    │   │   └── endpoints/
    │   │       └── graphs.py # 定義 /graphs 相關的 GET/POST
    │   ├── models/       # 資料庫模型 (ORM定義)
    │   │   └── graph_model.py (定義 Node, Edge, Graph 表結構)
    │   ├── schemas/      # Pydantic 模型 (用於請求/回應的資料驗證與序列化)
    │   │   └── graph_schema.py (定義前端傳來的 JSON 格式)
    │   ├── services/     # 業務邏輯層 (處理複雜操作，不直接碰資料庫或 HTTP)
    │   └── db/           # 資料庫連線初始化
    └── tests/            # 後端測試
```
