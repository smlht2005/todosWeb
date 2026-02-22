# 前端 UI 測試腳本

## 啟動服務

```bash
# 後端 (Port 8000)
cd src/dashboard/backend
python3 main.py

# 前端 (Port 3001)
cd src/dashboard/frontend
python3 -m http.server 3001
```

## 測試項目

### 1. 首頁載入
- [ ] 頁面正常顯示
- [ ] Header 標題正確
- [ ] Tailwind CSS 樣式正確載入

### 2. 統計區塊
- [ ] 5 個統計卡片顯示
- [ ] 數字正確顯示
- [ ] 顏色正確

### 3. 新增表單
- [ ] 輸入框可輸入
- [ ] 優先級下拉選單運作
- [ ] 新增按鈕可點擊

### 4. 待辦列表
- [ ] 列表正常顯示
- [ ] 狀態 emoji 顯示正確
- [ ] 勾選完成按鈕運作
- [ ] 刪除按鈕運作

### 5. 功能測試
- [ ] 新增待辦 → API POST
- [ ] 勾選完成 → API PUT
- [ ] 刪除待辦 → API DELETE

## 測試帳本

測試帳本：PM-Agent-001
- 後端：http://localhost:8000
- 前端：http://localhost:3001

## 手動測試步驟

1. 打開瀏覽器 http://localhost:3001
2. 確認看到統計數字
3. 在新增表單輸入「UI 測試」
4. 點擊新增
5. 確認列表出現新項目
6. 勾選完成
7. 確認狀態變為已完成
8. 點擊刪除
9. 確認項目被移除
