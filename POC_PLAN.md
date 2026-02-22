# T004 Web Dashboard POC 計畫

## 目標
建立一個網頁儀表板，查詢 SQLite 資料庫的待辦事項。

## 架構

```
src/dashboard/
├── frontend/          # Next.js 前端
│   ├── pages/        # 頁面
│   ├── components/   # 元件
│   └── styles/       # 樣式
│
├── backend/           # Python API
│   ├── api/          # FastAPI routes
│   ├── db/           # 資料庫連線
│   └── main.py       # 入口
│
└── scripts/          # 輔助腳本
```

## 多 Agent 協作流程

### PM Agent（總協調）
負責派工及控管狀態。接收用戶需求，分配給 SA/Code/QA Agent。

### SA Agent（規格制定）
負責製作 spec。根據需求寫出 API 規格和前端規格。

### Code Agent（開發 + 單元測試）
負責實際開發。寫 API、寫前端、寫單元測試。

### QA Agent（整合測試）
負責整合測試。驗證功能是否正常運作。

### SA Agent（Code Review）
負責 code review。審查程式碼品質。

---

## GitHub Repo 建立

Repo 名稱：todosWeb

URL: https://github.com/smlht2005/todosWeb

---

## 實作步驟

### Step 1: 建立 GitHub Repo + 本地專案
- 建立空的 GitHub repo
- 建立 Next.js + FastAPI 專案結構
- 初始化 Git

### Step 2: PM Agent 規劃
- 分析需求
- 分配任務給 SA Agent

### Step 3: SA Agent 制定規格
- API 規格文件
- 前端規格文件

### Step 4: Code Agent 開發
- Python FastAPI 後端
- Next.js 前端
- 單元測試

### Step 5: QA Agent 整合測試
- 功能測試
- API 測試

### Step 6: SA Agent Code Review
- 程式碼審查
- 提出改進建議

---

## 技術堆疊

- Frontend: Next.js 14
- Backend: Python FastAPI
- Database: SQLite (直接讀取 todos.db)
- API: RESTful

---

## API 端點設計

| Method | Path | 說明 |
|--------|------|------|
| GET | /api/todos | 取得所有待辦 |
| GET | /api/todos/{id} | 取得單一待辦 |
| POST | /api/todos | 新增待辦 |
| PUT | /api/todos/{id} | 更新待辦 |
| DELETE | /api/todos/{id} | 刪除待辦 |
| GET | /api/stats | 統計資料 |
