# HDL Lab Notes

> 個人 Hardware Description Language 學習紀錄網站：Verilog、Pipeline、Clock Gating、Synthesis、STA、APR、DRC、LVS。建立作業歷程與 Markdown 筆記，遵守 `AGENTS.md` 讓 AI 持續擴充。

## 已完成

- 響應式深色首頁：作業卡片、技術筆記、EDA Flow、全文關鍵字篩選
- HW2：Pipeline & Clock Gating 實驗與 PPA 分析、波形、VCD Power
- HW3：Pipelined THUMB CPU、DC/PT、APR、DRC、LVS 與真實截圖
- 3 篇技術筆記：EDA Flow、Pipeline、Clock Gating
- 文章頁目錄、圖片點擊放大、閱讀進度條、手機版導覽
- `AGENTS.md`：頁面風格、來源規範、擴充步驟、建置與檢查清單

## 直接開啟

首頁為 `index.html`。將整個專案上傳 GitHub 並設定 GitHub Pages，無需部署後端。

本機直接雙擊 `index.html` 也能看首頁與文章；若要開本機伺服器：

```bash
python3 -m http.server 8000
```

然後開啟 `http://localhost:8000`。

## 如何新增文章

1. 在 `content/` 建立 Markdown 檔案，例如 `content/os-ch04.md`。
2. 按照 `AGENTS.md` 的內容格式撰寫，文章圖片放在 `assets/images/`。
3. 在 `data/articles.json` 新增一筆（`category` 可選 `notes` 或 `assignments`）。
4. 更新生成的靜態 HTML：

```bash
python3 -m pip install -r requirements.txt
python3 scripts/build.py
```

5. 提交所有檔案到 GitHub。GitHub Pages 會自動提供新網址。

## GitHub Pages 部署

1. 在 GitHub 建立 **Public** Repository，建議命名 `hdl-lab-notes`。
2. 將整個專案內容上傳到 Repository **根目錄**（必須看得到 `index.html`、`AGENTS.md`、`assets/`、`assignments/`、`notes/` 等）。
3. 點 Repository 的 **Settings → Pages**。
4. 在 **Build and deployment** 設定 **Deploy from a branch**、Branch 選 `main`、Folder 選 `/(root)`，按 **Save**。
5. 部署完成後，網址一般為：`https://<github-username>.github.io/hdl-lab-notes/`。請用實際 GitHub 帳號與 Repo 名稱替換，不要直接繳交這個範例網址。
6. 驗證首頁、HW2、HW3、筆記與截圖均正常顯示，再把 GitHub Repo 網址和 Pages 網址貼到課程作業系統。

若你有 Git 指令習慣，也可在資料夾根目錄執行：

```bash
git init
git add .
git commit -m "Build HDL Lab Notes website"
git branch -M main
git remote add origin https://github.com/<github-username>/hdl-lab-notes.git
git push -u origin main
```

上面最後的 URL 請換成你在 GitHub 建立的 Repository 位址。

## 內容準確性與公開授權提醒

- HW2、HW3 內容改寫自作者本人的作業報告，截圖取自本人實驗執行成果。
- **HW3 舊版 DC/PT PPA 表格仍需核對最終 RTL / Gate Netlist**；網站已標註此限制。
- 公開前請自行檢查圖片中是否含校內主機資訊、EDA/PDK 授權資料或不能公開的技術內容。
- 老師／助教簡報只作為個人筆記參考，不直接重新散布。公開可以讀到的教材也不代表可自由大量轉載。

## 技術

HTML / CSS / JavaScript (無前端框架)。文章來源是 Markdown，使用 Python `mistune` 轉換為可部署的 HTML。無需伺服器或資料庫。
