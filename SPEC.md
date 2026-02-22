# SA Agent 規格文件

## todosWeb API 與前端規格

### 版本：1.0  
### 日期：2026-02-22

---

## 一、API 規格

### 1.1 Base URL
```
http://localhost:8000/api
```

### 1.2 Endpoints

#### GET /todos
取得所有待辦事項

Response:
```json
{
  "success": true,
  "data": [
    {
      "id": "T001",
      "title": "JSON 持久化",
      "status": "done",
      "priority": "high",
      "created_at": 1704067200
    }
  ]
}
```

#### GET /todos/{id}
取得單一待辦

#### POST /todos
新增待辦

Request:
```json
{
  "title": "新任務",
  "status": "todo",
  "priority": "medium"
}
```

#### PUT /todos/{id}
更新待辦

#### DELETE /todos/{id}
刪除待辦

#### GET /stats
取得統計

Response:
```json
{
  "total": 18,
  "done": 9,
  "todo": 3,
  "in_progress": 1,
  "review": 1
}
```

### 1.3 Error Response
```json
{
  "success": false,
  "error": "錯誤訊息"
}
```

---

## 二、前端規格

### 2.1 頁面結構

#### 首頁 (/)
- 統計儀表板
- 待辦事項列表
- 新增按鈕

#### 待辦詳情 (/todos/[id])
- 編輯表單
- 刪除確認

### 2.2 UI 元件

| 元件 | 說明 |
|------|------|
| StatCard | 統計數字卡片 |
| TodoItem | 待辦事項列表項目 |
| TodoForm | 新增/編輯表單 |
| Button | 按鈕元件 |

### 2.3 Styling
- 使用 Tailwind CSS
- 主色：藍色 (#3B82F6)
- 背景：淺灰 (#F9FAFB)

### 2.4 API 呼叫
- 使用 fetch API
- 錯誤處理顯示 Toast

---

## 三、資料庫 Schema

### todos 表
| 欄位 | 類型 | 說明 |
|------|------|------|
| id | TEXT | 主鍵 |
| title | TEXT | 標題 |
| status | TEXT | 狀態 |
| priority | TEXT | 優先級 |
| created_at | INTEGER | 建立時間 |
| updated_at | INTEGER | 更新時間 |

### bugs 表
| 欄位 | 類型 | 說明 |
|------|------|------|
| id | TEXT | 主鍵 |
| title | 標題 |  |
| status | 狀態 |  |
| priority | 優先級 |  |
| severity | 嚴重性 |  |

---

## 四、驗收標準

1. API 可正確讀寫 SQLite
2. 前端可顯示統計數據
3. 可新增、編輯、刪除待辦
4. 錯誤時顯示提示
