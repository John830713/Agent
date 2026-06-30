# 使用範例

## 儲存記憶

```
remember(content="使用者偏好 Rust 而非 Python", type="preference")
```

## 搜尋記憶

```
recall(query="使用者對語言有什麼偏好")
```

## 記錄事件

```
record_event(kind="milestone", payload={"content": "框架 v1 結構完成"})
```

## 固定規則

```
pin(content="專案目錄每層都要有 INDEX.md")
```

## 查看狀態

```
stats()
```
