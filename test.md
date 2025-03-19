# 台羅程式語言對照表 (JS 即時渲染版)

[回到 README](README.md)

本對照表提供 **C、C++、Python** 三種語言的台羅語法對應，讓開發者可以即時切換查看。

> ⚠ **注意：** GitHub 不允許 `.md` 內執行 JavaScript，此功能需於 **GitHub Pages / GitLab Pages / 其他 HTML 支援環境** 執行。

---

## 🔎 **選擇語言**
<div>
  <button onclick="renderTable('all')">📜 整合對照表</button>
  <button onclick="renderTable('python')">🐍 Python</button>
  <button onclick="renderTable('c')">💻 C</button>
  <button onclick="renderTable('cpp')">🚀 C++</button>
</div>

---

## 🔗 **索引**
- [整合對照表](#)
- [Python 語法對照表](#)
- [C 語法對照表](#)
- [C++ 語法對照表](#)
- [使用方式](#)
- [專案資訊](#)

---

## 📋 **對照表顯示區域**
<div id="table-content">
  <p>請點擊上方按鈕選擇要顯示的語法對照表。</p>
</div>

---

## 📌 **使用方式**
1. 在 C / C++ 程式中：
```c
#include "taiyu_c.h"  // C
#include "taiyu_cpp.hpp"  // C++
