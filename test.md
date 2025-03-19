# 台羅程式語言對照表 (JS 版)

[回到 README](README.md)

本對照表提供 **C、C++、Python** 三種語言的台羅語法對應，讓開發者可以快速查閱。

> ⚠ **注意：** GitHub 原生 `.md` **不允許執行 JavaScript**，請在 **GitHub Pages 或其他可執行 HTML 的環境** 下使用。

---

## 🔎 選擇語言：
<div>
  <button onclick="showTable('all-table')">📜 整合對照表</button>
  <button onclick="showTable('python-table')">🐍 Python</button>
  <button onclick="showTable('c-table')">💻 C</button>
  <button onclick="showTable('cplusplus-table')">🚀 C++</button>
</div>

---

## 🔗 **索引**
- [整合對照表](#整合對照表)
- [Python 語法對照表](#python-語法對照表)
- [C 語法對照表](#c-語法對照表)
- [C++ 語法對照表](#c-plusplus-語法對照表)
- [使用方式](#使用方式)
- [專案資訊](#專案資訊)

---

<!-- 整合對照表 -->
<div id="all-table" class="table-section">
## 📜 整合對照表

| **標準語法** | **台羅對應** | **適用語言** |
|-------------|-------------|--------------|
| `if`        | `nā`       | C / C++ / Python |
| `else if` / `elif` | `nā_bô`   | C / C++ / Python |
| `else`      | `bô`       | C / C++ / Python |
| `switch`    | `suán`     | C / C++ |
| `case`      | `hîng`       | C / C++ |
| `default`   | `ī_siat`     | C / C++ |
| `for`       | `sûn_khuân`       | C / C++ / Python |
| `while`     | `tng` | C / C++ / Python |
| `break`     | `thîng`| C / C++ / Python |
| `continue`  | `kè_siòk` | C / C++ / Python |
| `try`       | `nā_si` | C++ |
| `catch`  | `bô_hó` | C++ |
| `throw` | `tîng-tânn`   | C++ |
| `try-except-finally`    | `nā_si_bô_hó_tō` | Python |
| `return`    | `huê`  | C / C++ / Python |
</div>

<!-- Python 對照表 -->
<div id="python-table" class="table-section" style="display: none;">
## 🐍 Python 語法對照表

| **標準語法**             | **台羅對應** |
|--------------------------|--------------|
| `if`                     | `nā`         |
| `elif`                   | `nā_bô`      |
| `else`                   | `bô`         |
| `for`                    | `sûn_khuân`  |
| `while`                  | `tng`        |
| `break`                  | `thîng`      |
| `continue`               | `kè_siòk`    |
| `try-except-finally`     | `nā_si_bô_hó_tō` |
| `return`                 | `huê`        |

</div>

<!-- C 語法對照表 -->
<div id="c-table" class="table-section" style="display: none;">
## 💻 C 語法對照表

| **標準語法** | **台羅對應** |
|--------------|--------------|
| `if`         | `nā`         |
| `else if`    | `nā_bô`      |
| `else`       | `bô`         |
| `switch`     | `suán`       |
| `case`       | `hîng`       |
| `default`    | `ī_siat`     |
| `for`        | `sûn_khuân`  |
| `while`      | `tng`        |
| `break`      | `thîng`      |
| `continue`   | `kè_siòk`    |
| `return`     | `huê`        |

</div>

<!-- C++ 語法對照表 -->
<div id="cplusplus-table" class="table-section" style="display: none;">
## 🚀 C++ 語法對照表

| **標準語法**             | **台羅對應** |
|--------------------------|--------------|
| `if`                     | `nā`         |
| `else if`                | `nā_bô`      |
| `else`                   | `bô`         |
| `switch`                 | `suán`       |
| `case`                   | `hîng`       |
| `default`                | `ī_siat`     |
| `for`                    | `sûn_khuân`  |
| `while`                  | `tng`        |
| `break`                  | `thîng`      |
| `continue`               | `kè_siòk`    |
| `try`                    | `nā_si`      |
| `catch`                  | `bô_hó`      |
| `throw`                  | `tîng-tânn`  |
| `return`                 | `huê`        |

</div>

---

## 📌 使用方式

1. 在 C / C++ 程式中：
```c
#include "taiyu_c.h"  // C
#include "taiyu_cpp.hpp"  // C++
