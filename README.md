# todosWeb - 待辦事項管理儀表板

## 概述

Web 版的待辦事項管理系統，支援任務追蹤、Bug 管理功能。

## 功能

- ✅ 任務管理 (CRUD)
- 📊 統計儀表板
- 🐛 Bug 追蹤
- 🎨 現代化 UI/UX
- 📱 響應式設計

## 技術棧

| 技術 | 用途 |
|------|------|
| FastAPI | 後端 API |
| SQLite | 資料庫 |
| Tailwind CSS | 樣式框架 |
| Font Awesome | 圖標庫 |
| Google Fonts | 中文字體 |

## 安裝

```bash
# 啟動後端
cd backend
python3 main.py

# 啟動前端
cd frontend
python3 -m http.server 3001
```

## API

| Method | Endpoint | 說明 |
|--------|----------|------|
| GET | /api/todos | 取得所有任務 |
| POST | /api/todos | 新增任務 |
| PUT | /api/todos/{id} | 更新任務 |
| DELETE | /api/todos/{id} | 刪除任務 |
| GET | /api/stats | 取得統計 |
| GET | /api/bugs | 取得 Bugs |
| GET | /api/bug-stats | Bug 統計 |

## 版本

- v1.0 - 基礎 CRUD
- v1.1 - UI 優化 + Bug 追蹤

## License

MIT

---

*by 阿文 🐧*
