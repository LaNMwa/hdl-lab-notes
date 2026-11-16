# HDL Lab Notes

個人硬體描述語言(HDL)學習紀錄網站，主要整理 Verilog 設計、數位電路實作、EDA 工具操作，以及課程作業的實驗成果。

希望透過這個網站，將平常的作業報告與學習筆記整理成方便查閱、能持續更新的技術紀錄。

## 網站內容

### 作業紀錄
- **HW2 — Pipeline & Clock Gating**：比較 Non-Pipelined、Pipelined 與 Clock-Gated 設計，整理模擬波形與 PPA 分析。
- **HW3 — Pipelined THUMB CPU**：記錄 RTL/Gate-Level Simulation、Synthesis、Timing Analysis、APR、DRC 與 LVS 的實作過程及結果。

### 技術筆記
- EDA Design Flow
- Pipeline Design
- Clock Gating

## 網站功能

- 作業與技術筆記分類瀏覽
- 關鍵字搜尋
- 文章目錄與閱讀進度條
- 實驗截圖放大檢視
- 響應式網頁設計

## 使用技術

- **前端：** HTML、CSS、JavaScript
- **內容管理：** Markdown
- **文章生成：** Python、Mistune
- **網站部署：** GitHub Pages

## AGENTS.md 開發規範

本專案透過 [AGENTS.md](AGENTS.md) 統一網站的開發與維護方式，讓未來新增文章或修改功能時，都能維持一致的設計風格與檔案結構。

規範主要包含：

1. **網站架構：** 定義各個資料夾的用途，以及 HTML、CSS、JavaScript 的管理方式。
2. **頁面設計：** 統一配色、排版、導覽及響應式設計。
3. **文章格式：** 規定作業紀錄與技術筆記的標題、章節及圖片呈現方式。
4. **內容正確性：** 實驗數據以實際報告為準，避免加入未經驗證的資訊。
5. **擴充流程：** 說明新增文章時需要修改哪些檔案，以及如何重新建置並檢查網站。

未來可以直接提供新的作業報告或課程資料，讓 AI 參考 `AGENTS.md` 的規範整理成網站文章，減少重複調整格式的工作。

## 新增與管理文章

網站以 Markdown 作為文章來源，透過 Python 腳本產生對應的 HTML 頁面。

### 新增文章流程

1. **建立文章：** 在 `content/` 新增 Markdown 檔案，例如 `content/hw4.md`。
2. **整理內容：** 依照 `AGENTS.md` 的格式撰寫，加入設計目標、實作過程、實驗結果與心得。
3. **加入圖片：** 將波形、電路圖或實驗截圖放入 `assets/images/`，並在文章中引用。
4. **更新索引：** 在 `data/articles.json` 加入文章標題、分類、描述及對應路徑。
5. **重新建置：** 執行 Python 腳本，產生新的 HTML 頁面。
6. **發布更新：** 將修改後的檔案 Push 至 GitHub，透過 GitHub Pages 更新網站。

### 建置指令

首次使用時安裝所需套件：

```bash
python3 -m pip install -r requirements.txt
```

新增或修改文章後執行：

```bash
python3 scripts/build.py
```

### 文章管理方式

- `content/`：儲存 Markdown 文章原始內容。
- `data/articles.json`：管理文章資訊與分類。
- `assets/images/`：存放文章使用的圖片。
- `assignments/`：作業紀錄的 HTML 頁面。
- `notes/`：技術筆記的 HTML 頁面。

修改既有文章時，只需更新對應的 Markdown 並重新執行建置；新增文章則需同步更新文章索引，讓首頁可以正確顯示。

## 未來規劃

持續增加 HDL 課程筆記、EDA 工具操作紀錄，以及 Computer Architecture、Digital IC Design 等相關內容，逐步建立完整的硬體設計學習知識庫。

---

**GitHub Repository：** https://github.com/LaNMwa/hdl-lab-notes
