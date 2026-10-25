# 臺灣 108 國中小數學教材研發與 AI 伴學工作台（Single Source of Truth, SSOT）

> **專案總綱**：依據研究主持人 馮奇偉 老師核定，本目錄（`HAIC/class/math/`）為全站數學教材設計、文獻研發、AI 伴學工作台與實戰評量之**單一真相庫（SSOT）**。
> 所有單元均依「**五合一標準規格**（AI 伴學工作台、段考速查對照表、學生實戰學習單、教師詳解評分版、後台教案研究 docs）」進行結構化歸納與封裝。

---

## 🗺️ 核心單元導覽目錄

### 1. 【國二上・數與量】二次方根（N-8-1 & N-8-2）
* **單元專區目錄**：[`HAIC/class/math/square-roots/`](file:///H:/我的雲端硬碟/HAIC/class/math/square-roots/)
* **核心成果檔案**：
  * 🎯 **AI 伴學工作台**：[`square-roots/index.html`](file:///H:/我的雲端硬碟/HAIC/class/math/square-roots/index.html)（56 題動態題庫、麥斯⚡全陪、A4 影印紙 $\sqrt{2}:1$ 探究）
  * 📊 **段考題型對照表**：[`square-roots/cheatsheet.html`](file:///H:/我的雲端硬碟/HAIC/class/math/square-roots/cheatsheet.html)
  * 📝 **學生實戰學習單**：[`square-roots/worksheet.html`](file:///H:/我的雲端硬碟/HAIC/class/math/square-roots/worksheet.html) ｜ [Word .doc 版](file:///H:/我的雲端硬碟/HAIC/class/math/square-roots/worksheet.doc)
  * 🔑 **教師詳解評分配分版**：[`square-roots/worksheet-teacher.html`](file:///H:/我的雲端硬碟/HAIC/class/math/square-roots/worksheet-teacher.html) ｜ [Word .doc 版](file:///H:/我的雲端硬碟/HAIC/class/math/square-roots/worksheet-teacher.doc)
  * 📑 **後台教案研發 docs**：[`square-roots/docs/`](file:///H:/我的雲端硬碟/HAIC/class/math/square-roots/docs/)（含文獻研究、8 階段教案、題目生成引擎 py）

---

### 2. 【國二上・幾何與空間】畢氏定理與坐標距離（S-8-6 & G-8-1）
* **單元專區目錄**：[`HAIC/class/math/pythagorean/`](file:///H:/我的雲端硬碟/HAIC/class/math/pythagorean/)
* **核心成果檔案**：
  * 📐 **AI 伴學工作台**：[`pythagorean/index.html`](file:///H:/我的雲端硬碟/HAIC/class/math/pythagorean/index.html)（4 大精煉認知階段、14 幅高清 SVG 幾何圖解、28 題階梯練習＋Capstone 綜合大題、麥斯⚡全陪模式）｜ [純文字 .txt 版](file:///H:/我的雲端硬碟/HAIC/class/math/pythagorean/index.txt)
  * 📊 **段考題型速查對照表**：[`pythagorean/cheatsheet.html`](file:///H:/我的雲端硬碟/HAIC/class/math/pythagorean/cheatsheet.html)（4 階段技能分析矩陣、幾何速查圖解卡、考前 30 秒救命清單）｜ [純文字 .txt 版](file:///H:/我的雲端硬碟/HAIC/class/math/pythagorean/cheatsheet.txt)
  * 📝 **學生實戰學習單**：[`pythagorean/worksheet.html`](file:///H:/我的雲端硬碟/HAIC/class/math/pythagorean/worksheet.html) ｜ [Word .doc 版](file:///H:/我的雲端硬碟/HAIC/class/math/pythagorean/worksheet.doc) ｜ [純文字 .txt 版](file:///H:/我的雲端硬碟/HAIC/class/math/pythagorean/worksheet.txt)
  * 👩‍🏫 **教師詳解評分配分版**：[`pythagorean/worksheet-teacher.html`](file:///H:/我的雲端硬碟/HAIC/class/math/pythagorean/worksheet-teacher.html) ｜ [Word .doc 版](file:///H:/我的雲端硬碟/HAIC/class/math/pythagorean/worksheet-teacher.doc) ｜ [純文字 .txt 版](file:///H:/我的雲端硬碟/HAIC/class/math/pythagorean/worksheet-teacher.txt)
  * 📑 **後台教案研發 docs**：[`pythagorean/docs/`](file:///H:/我的雲端硬碟/HAIC/class/math/pythagorean/docs/)（含文獻研究、教案、Meta AI 題庫提案、題目生成引擎 py）

---

### 3. 【課綱資料庫】12 年國教數學課綱條碼表
* **資料庫目錄**：[`HAIC/class/math/curriculum_standards/`](file:///H:/我的雲端硬碟/HAIC/class/math/curriculum_standards/)
* **檔案**：[`12年國教數學課綱學習內容條碼表.csv`](file:///H:/我的雲端硬碟/HAIC/class/math/curriculum_standards/12年國教數學課綱學習內容條碼表.csv)

---

## 🏛️ 標準五合一模組結構規範

每個新開發之數學單元，均嚴格遵照以下規範封裝：

```text
math/{單元名稱}/
├── index.html               # 1. 互動式 AI 伴學工作台（學生自學/課堂精準練習）
├── cheatsheet.html          # 2. 8 階段段考題型速查對照表（考前精要背誦）
├── worksheet.html / .doc    # 3. 學生實戰學習單（支援一鍵 A4 列印與 Word 編輯）
├── worksheet-teacher.html   # 4. 教師詳解評分配分版（滿分 100 分制標準、給分級距）
└── docs/                    # 5. 後台研發檔案庫
    ├── README.md            #    - 探究學習地圖總覽
    ├── 文獻研究_*.md         #    - 期刊論文實證依據與認知斷層分析
    ├── 階段01~08_*.md       #    - 8 大階段結構化 Markdown 教案
    ├── 題目設計提案_*.md     #    - 題目母題、漂亮數值與避坑標註
    └── 題目生成引擎_*.py     #    - 參數化隨機出題演算法引擎
```
