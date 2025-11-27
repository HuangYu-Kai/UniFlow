gantt
    title UniFlow 專案開發時程規劃
    dateFormat  YYYY-MM-DD
    axisFormat %m/%d
    section 基礎設定與規劃 (第一週)
    專案初始化與技術選型 :done, crit, 2024-07-22, 2d
    詳細功能規格定義 :active, crit, 2024-07-24, 3d
    UI/UX 設計 (Wireframe & Mockup) :crit, 2024-07-24, 5d
    資料庫結構設計 : 2024-07-29, 3d

    section 後端核心功能開發 (第二至三週)
    搭建 FastAPI 基礎架構 :done, 2024-07-29, 2d
    使用者工作流程 (Graph) 的 CRUD API : 2024-07-31, 4d
    實現節點執行與調度邏輯 : 2024-08-05, 5d
    串接第一個外部服務 (Discord Webhook) :done, 2024-07-29, 3d

    section 前端核心功能開發 (第二至四周)
    建立 React Flow 畫布與基本配置 :after 搭建 FastAPI 基礎架構, 5d
    開發可拖曳的節點側邊欄 : 7d
    自定義節點 (Custom Node) 樣式與互動 : 10d
    串接後端 API (儲存/讀取工作流程) : after 使用者工作流程 (Graph) 的 CRUD API, 5d
    全域狀態管理 (Zustand/Redux) : 5d

    section 整合、測試與優化 (第五週)
    前後端功能整合測試 : after 串接後端 API (儲存/讀取工作流程), 5d
    撰寫單元測試與整合測試 : 5d
    使用者體驗 (UX) 優化 : 3d

    section 部署與文件 (第六週)
    設定 CI/CD (持續整合/持續部署) 流程 : 5d
    部署到雲端平台 (例如 Heroku, Vercel) : 3d
    撰寫使用者與開發者文件 : 5d
