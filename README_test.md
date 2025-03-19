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
```
2. 在 Python 程式中：
```python
from taiyu_py import *
```

---

## 🔖 **專案資訊**
本專案基於 [`MIT License`](https://github.com/Alan20050829/taiyu-programming-language/blob/main/LICENSE)，自由開源！
歡迎所有人聯繫我提出修改建議 📧 *linjunxieng0829@gmail.com*

---

<!-- JavaScript -->
<script>
function renderTable(language) {
  let tables = {
    "all": `
<h2>📜 整合對照表</h2>
<table border="1">
<tr><th>標準語法</th><th>台羅對應</th><th>適用語言</th></tr>
<tr><td>if</td><td>nā</td><td>C / C++ / Python</td></tr>
<tr><td>else if / elif</td><td>nā_bô</td><td>C / C++ / Python</td></tr>
<tr><td>else</td><td>bô</td><td>C / C++ / Python</td></tr>
<tr><td>switch</td><td>suán</td><td>C / C++</td></tr>
<tr><td>case</td><td>hîng</td><td>C / C++</td></tr>
<tr><td>default</td><td>ī_siat</td><td>C / C++</td></tr>
<tr><td>for</td><td>sûn_khuân</td><td>C / C++ / Python</td></tr>
<tr><td>while</td><td>tng</td><td>C / C++ / Python</td></tr>
<tr><td>break</td><td>thîng</td><td>C / C++ / Python</td></tr>
<tr><td>continue</td><td>kè_siòk</td><td>C / C++ / Python</td></tr>
<tr><td>try</td><td>nā_si</td><td>C++</td></tr>
<tr><td>catch</td><td>bô_hó</td><td>C++</td></tr>
<tr><td>throw</td><td>tîng-tânn</td><td>C++</td></tr>
<tr><td>try-except-finally</td><td>nā_si_bô_hó_tō</td><td>Python</td></tr>
<tr><td>return</td><td>huê</td><td>C / C++ / Python</td></tr>
</table>
    `,
    "python": `
<h2>🐍 Python 語法對照表</h2>
<table border="1">
<tr><th>標準語法</th><th>台羅對應</th></tr>
<tr><td>if</td><td>nā</td></tr>
<tr><td>elif</td><td>nā_bô</td></tr>
<tr><td>else</td><td>bô</td></tr>
<tr><td>for</td><td>sûn_khuân</td></tr>
<tr><td>while</td><td>tng</td></tr>
<tr><td>break</td><td>thîng</td></tr>
<tr><td>continue</td><td>kè_siòk</td></tr>
<tr><td>try-except-finally</td><td>nā_si_bô_hó_tō</td></tr>
<tr><td>return</td><td>huê</td></tr>
</table>
    `,
    "c": `
<h2>💻 C 語法對照表</h2>
<table border="1">
<tr><th>標準語法</th><th>台羅對應</th></tr>
<tr><td>if</td><td>nā</td></tr>
<tr><td>else if</td><td>nā_bô</td></tr>
<tr><td>else</td><td>bô</td></tr>
<tr><td>switch</td><td>suán</td></tr>
<tr><td>case</td><td>hîng</td></tr>
<tr><td>default</td><td>ī_siat</td></tr>
<tr><td>for</td><td>sûn_khuân</td></tr>
<tr><td>while</td><td>tng</td></tr>
<tr><td>break</td><td>thîng</td></tr>
<tr><td>continue</td><td>kè_siòk</td></tr>
<tr><td>return</td><td>huê</td></tr>
</table>
    `
  };

  document.getElementById("table-content").innerHTML = tables[language];
}
</script>
