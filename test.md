# 台羅程式語言對照表 (JS Demo in .md)

[回到 README](README.md)

本對照表提供 **C、C++、Python** 三種語言的台羅語法對應，讓開發者可以快速查閱。

> ⚠ **注意：** GitHub 原生 `.md` 不允許執行 JavaScript。如果要在 GitHub Pages 或其他可執行 HTML 的環境下使用，可將此檔案放到能解析 HTML/JS 的 Markdown 解析器上。

---

<!-- 按鈕列，點擊可切換顯示對應語言的表格 -->
<div style="margin-bottom: 1rem;">
  <button onclick="showTable('index-section')">索引</button>
  <button onclick="showTable('all-table')">整合對照表</button>
  <button onclick="showTable('python-table')">Python</button>
  <button onclick="showTable('c-table')">C</button>
  <button onclick="showTable('cpp-table')">C++</button>
</div>

<!-- 預設：顯示「索引」區塊 -->
<div id="index-section" class="view-section" style="display: block;">
## 索引
- [整合對照表](#整合對照表)
- [Python 語法對照表](#python-語法對照表)
- [C 語法對照表](#c-語法對照表)
- [C++ 語法對照表](#c-語法對照表)
- [使用方式](#使用方式)
- [專案資訊](#專案資訊)
</div>

<!-- 整合對照表 -->
<div id="all-table" class="view-section" style="display: none;">
## 整合對照表

| **標準語法**             | **台羅對應**       | **適用語言**           |
|--------------------------|--------------------|------------------------|
| `if`                     | `nā`               | C / C++ / Python       |
| `else if` / `elif`      | `nā_bô`            | C / C++ / Python       |
| `else`                   | `bô`               | C / C++ / Python       |
| `switch`                 | `suán`             | C / C++                |
| `case`                   | `hîng`             | C / C++                |
| `default`                | `ī_siat`           | C / C++                |
| `for`                    | `sûn_khuân`        | C / C++ / Python       |
| `while`                  | `tng`              | C / C++ / Python       |
| `break`                  | `thîng`            | C / C++ / Python       |
| `continue`               | `kè_siòk`          | C / C++ / Python       |
| `try`                    | `nā_si`            | C++                    |
| `catch`                  | `bô_hó`            | C++                    |
| `throw`                  | `tîng-tânn`        | C++                    |
| `try-except-finally`     | `nā_si_bô_hó_tō`   | Python                 |
| `return`                 | `huê`              | C / C++ / Python       |
| `class`                  | `tsióng`           | C++ / Python           |
| `struct`                 | `kiat_kòo`         | C                      |
| `auto`                   | `tsū-tōng`         | C++                    |
| `void`                   | `khang`            | C / C++                |
| `def`                    | `li_sī`            | Python                 |
| `int`                    | `tsê_thâu`         | C / C++ / Python       |
| `float`                  | `sòo`              | C / C++ / Python       |
| `double`                 | `tsún_sòo`         | C / C++ / Python       |
| `char*` / `string`       | `jī`               | C / C++ / Python       |
| `vector`                 | `sò͘_tīn`          | C++                    |
| `map`                    | `tē_tôo`           | C++                    |
| `set`                    | `tsi̍p_hap`        | C++                    |
| `malloc`                 | `pun`              | C / C++ / Python       |
| `free`                   | `kái`              | C / C++                |
| `true`                   | `tsin`             | C / C++ / Python       |
| `false`                  | `ké`               | C / C++ / Python       |
| `printf` `cout` `print` | `su_tshut`         | C / C++ / Python       |
| `scanf` `cin` `input`   | `su_jip`           | C / C++ / Python       |

[回到頂部](#索引)
</div>

<!-- Python 表格 -->
<div id="python-table" class="view-section" style="display: none;">
## Python 語法對照表

以下僅列出「適用語言」欄位包含 Python 的語法：

| **標準語法**             | **台羅對應** |
|--------------------------|--------------|
| `if`                     | `nā`         |
| `else if` / `elif`       | `nā_bô`      |
| `else`                   | `bô`         |
| `for`                    | `sûn_khuân`  |
| `while`                  | `tng`        |
| `break`                  | `thîng`      |
| `continue`               | `kè_siòk`    |
| `try-except-finally`     | `nā_si_bô_hó_tō` |
| `return`                 | `huê`        |
| `class`                  | `tsióng`     | <!-- also C++ -->
| `def`                    | `li_sī`      |
| `int`                    | `tsê_thâu`   |
| `float`                  | `sòo`        |
| `double`                 | `tsún_sòo`   |
| `char*` / `string`       | `jī`         |
| `malloc`                 | `pun`        |
| `true`                   | `tsin`       |
| `false`                  | `ké`         |
| `printf` `cout` `print` | `su_tshut`   | <!-- also C / C++ -->
| `scanf` `cin` `input`   | `su_jip`     | <!-- also C / C++ -->

[回到頂部](#索引)  
[回到 README](README.md)
</div>

<!-- C 表格 -->
<div id="c-table" class="view-section" style="display: none;">
## C 語法對照表

以下僅列出「適用語言」欄位包含 C 的語法：

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
| `struct`     | `kiat_kòo`   |
| `void`       | `khang`      |
| `int`        | `tsê_thâu`   |
| `float`      | `sòo`        |
| `double`     | `tsún_sòo`   |
| `char*` / `string` | `jī`   |
| `malloc`     | `pun`        |
| `free`       | `kái`        |
| `true`       | `tsin`       |
| `false`      | `ké`         |
| `printf`     | `su_tshut`   |
| `scanf`      | `su_jip`     |

[回到頂部](#索引)  
[回到 README](README.md)
</div>

<!-- C++ 表格 -->
<div id="cpp-table" class="view-section" style="display: none;">
## C++ 語法對照表

以下僅列出「適用語言」欄位包含 C++ 的語法：

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
| `class`                  | `tsióng`     | <!-- also Python -->
| `auto`                   | `tsū-tōng`   |
| `void`                   | `khang`      | <!-- also C -->
| `int`                    | `tsê_thâu`   |
| `float`                  | `sòo`        |
| `double`                 | `tsún_sòo`   |
| `char*` / `string`       | `jī`         |
| `vector`                 | `sò͘_tīn`    |
| `map`                    | `tē_tôo`     |
| `set`                    | `tsi̍p_hap`  |
| `malloc`                 | `pun`        |
| `free`                   | `kái`        |
| `true`                   | `tsin`       |
| `false`                  | `ké`         |
| `printf` `cout` `print` | `su_tshut`   |
| `scanf` `cin` `input`   | `su_jip`     |

[回到頂部](#索引)  
[回到 README](README.md)
</div>

---

## 使用方式

1. 在 C / C++ 程式中：
   ```c
   #include "taiyu_c.h"  // C
   #include "taiyu_cpp.hpp"  // C++
