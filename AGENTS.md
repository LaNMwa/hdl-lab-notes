# HDL Lab Notes — AI 開發規則

> 本檔案是本專案最重要的協作規範。AI 在新增筆記、修改頁面、整理簡報或維護網站前，請先閱讀本檔案。網站以 **繁體中文＋必要英文專業名詞** 撰寫，作為個人硬體描述語言（HDL）學習歷程與作業成果紀錄。

## 1. 專案目標與定位

- 網站主題：Verilog、數位 IC、Pipeline、Clock Gating、Synthesis、STA、APR、DRC 與 LVS 的實驗紀錄與學習筆記。
- 首要讀者：作者本人，以及想了解數位硬體設計流程的學生。
- **作業紀錄**應根據本人提供的作業報告、程式碼與量測截圖，不得虛構數值、實作過程或測試結果。
- **技術筆記**可以根據作者提供的教學簡報與公開資料整理；需標示內容來源，並清楚區分講義原文、個人整理與延伸解釋。
- 不要把尚未核對的實驗結果寫成最終定論。HW3 早期 DC/PT PPA 資料仍待最終 Netlist 版本核對；這個提醒必須保留。

## 2. 技術規格與檔案結構

網站為 GitHub Pages 可直接部署的靜態網站：

```text
HDL-Lab-Notes/
├── index.html                 # 生成的網站首頁
├── assignments/              # 生成的作業紀錄 HTML
├── notes/                    # 生成的技術筆記 HTML
├── content/                  # 唯一的文章內容來源，Markdown
│   ├── hw2.md
│   ├── hw3.md
│   ├── eda-flow.md
│   ├── pipeline.md
│   └── clock-gating.md
├── data/articles.json        # 文章名稱、分類、標籤、摘要、封面等
├── assets/
│   ├── css/styles.css        # 共用樣式
│   ├── js/site.js            # 導覽、搜尋、目錄、圖片放大
│   └── images/               # 作者自己的截圖
├── scripts/build.py          # Markdown → GitHub Pages 靜態 HTML
├── requirements.txt
├── AGENTS.md
└── README.md
```

- HTML 頁面由 `scripts/build.py` 產生，**修改文章時請改 `content/*.md`，再執行建置，不要直接改生成的文章 HTML**。
- 新增文章時，依序建立 `content/<slug>.md`、新增 `data/articles.json` 一筆、執行 `python scripts/build.py`。
- `category` 僅有 `assignments`（作業）及 `notes`（筆記），`slug` 使用小寫英文、數字、連字號，必須唯一。
- 生成路徑固定為 `assignments/<slug>.html` 或 `notes/<slug>.html`；相對圖片路徑固定為 `../assets/images/<filename>`。
- 不新增 React、Vue、後端、資料庫、登入、外部分析追蹤等，除非使用者明確要求。保持 GitHub Pages 一鍵部署。
- Python 建置使用 `mistune`；依 `requirements.txt` 安裝後，從專案根目錄執行 `python scripts/build.py`。

## 3. UI / UX 與版型規則

- 現有設計風格：深色 `#080d13` 背景、薄荷綠 `#6ff1ca` 強調色、卡片式版面與技術日誌感。**新頁面沿用既有 CSS class 與文章版型**。
- 頁面必須支援桌面與手機，避免固定寬度造成水平捲動。
- 每篇文章需有：標題、簡介、至少三個小節、來源說明。作業紀錄另須包括「目標、方法／架構、驗證或量測、心得」，實際可依作業性質調整。
- 文章圖片要有說明性 alt 文字及圖說；技術截圖保留原始比例，點擊可放大。
- 文章 `##` 標題會生成右側目錄。不要以單純加粗文字取代必要的標題層級。
- 手機導覽、搜尋、放大圖片、文章目錄都需可操作。不要讓新增內容破壞既有互動。

## 4. 作業紀錄撰寫格式

建議每篇 `content/hwN.md` 依下列順序寫：

```markdown
# HWN：作業名稱

> 作業目的、資料來源與版本狀態

## 01 / 作業目標
## 02 / 設計架構與方法
## 03 / RTL / Simulation
## 04 / PPA 或實驗結果
## 05 / 問題排除與檢討
## 06 / 學習心得

*資料來源：本人作業報告 / 日期。*
```

- 數字必須標明工具、單位、測試條件與版本；不確定就寫「待確認」，不得自行填補。
- DC 與 PT Power、Pre-/Post-Route Timing、RTL 與 Gate-Level Simulation 等不同階段不要混用。
- 擷取作者提供的螢幕截圖時，優先使用有完整上下文、可識別工具與數值的圖片。
- 不要在公開網站放入原始有授權限制的 PDK、EDA 安裝包、授權檔、Server 密碼、API Key 或未經准許的課程檔案。

## 5. 從課堂簡報產生技術筆記的 AI 規則

收到老師或助教 PPT / PDF 時，遵照以下流程：

1. 先讀完使用者指定的章節或頁面，按講義順序整理主題及關鍵術語。
2. 確認哪些觀念來自簡報，哪些是作者自己的作業經驗；正文自然註明，避免混淆。
3. 使用繁體中文、自然且精確的教學風格，第一次出現的重要名詞保留英文，例如 `process`、`register`、`critical path`。
4. 介紹概念時優先寫「定義 → 為什麼需要 → 運作方式 → 範例或圖 → 常見錯誤／重點整理」。每篇用 3～7 個二級標題。
5. 可用自己的話整理、比較或改寫簡報知識，但**不要未經授權直接複製講義、插圖或整張投影片公開**。即使網路找得到講義，也不代表可自由轉載。
6. 遇到講義資訊不足、數據不清楚或不同講義說法相異時，明確註明待確認，不要自行補成確定答案。
7. 把結果儲存於 `content/<slug>.md`；在 `data/articles.json` 新增分類 `notes` 的條目；執行建置並檢查網站文章。

## 6. 新增文章的 JSON 規範

每筆物件欄位如下：

```json
{
  "slug": "sta-basics",
  "category": "notes",
  "number": "NOTE / 04",
  "title": "Static Timing Analysis 基礎",
  "subtitle": "Setup、Hold 與 Slack",
  "description": "以簡單路徑解釋時序分析的重點。",
  "date": "2026-11-16",
  "tags": ["STA", "Timing"],
  "cover": "hw3-setup.webp",
  "reading": "約 4 分鐘"
}
```

- `cover` 必須是 `assets/images/` 中存在的圖片；可以重用作者自己的已授權照片。
- 更新文章時維持既有 slug，避免 GitHub Pages 舊連結失效。
- 首頁卡片由 `data/articles.json` 自動產生，不必手動複製卡片 HTML。

## 7. AI 每次修改前後的檢查清單

修改前：
- 確認要編輯的檔案與資料來源，閱讀相關原始 Markdown。
- 確認是「新增筆記」、「更新作業」或「樣式修正」，限制不必要的變更。

修改後：
- 確認 `data/articles.json` 為有效 JSON、沒有重複 slug。
- 執行 `python scripts/build.py`，無錯誤，並確認新 HTML 被建立。
- 檢查所有站內連結及圖片路徑，尤其是 GitHub Pages 子目錄下的相對路徑。
- 檢查導覽、搜尋、圖片放大、文章目錄及手機版。
- 檢查內容中日期、數值、工具名稱、來源，以及可能有授權或敏感資訊的截圖。
- 在回覆中簡短回報「更新哪些檔案／新增哪篇文章／哪些數值需要使用者確認」。

## 8. 擴充情境示範（供作業評分使用）

使用者下次可以輸入：

> 請先讀 AGENTS.md。我上傳了 OS 第 4 章簡報，請按照第 5 節的整理方式建立繁體中文技術筆記，存成 `content/os-ch04.md`，把筆記登錄到 `data/articles.json`，完成建置，並確認首頁會顯示新文章。請保留英文關鍵術語、標示來源與頁碼，不要複製整張投影片。

AI 讀取本規則後就知道文章格式、檔案結構、風格、來源原則，以及新增頁面的完整流程。未來新增 HW4 或其他課程筆記時也能重複使用。
