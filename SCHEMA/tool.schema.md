# Tool Schema — 工具條目規範

## 必要檔案

```
tool-name/
├── INDEX.md     # 工具說明書
├── spec.md      # 規格 / API 文件
└── usage.md     # 使用範例
```

## INDEX.md 格式

```markdown
# tool-name

用途：一句話說明

## 適用場景

## 限制
```

## spec.md 格式

```markdown
# 規格

## 介面 / 指令

## 參數

## 輸出
```

## usage.md 格式

```markdown
# 使用範例

## 基本用法

## 進階用法

## 注意事項
```

## AI 使用規則

1. 讀取 `TOOLS/INDEX.md` 確認有哪些工具可用
2. 讀取個別工具的說明書了解用途
3. 查閱 spec.md 與 usage.md 確認如何調用
4. 不確定時不要問使用者，先自行查閱文件
