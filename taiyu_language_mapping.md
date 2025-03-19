# 📜 台羅程式語言對照表

## [回到 README](README.md)

### 本對照表提供 **C、C++、Python** 三種語言的台羅語法對應，讓開發者可以快速查閱。

---

## 📝 **台羅語法對照表**

<!-- 選擇語言按鈕 -->
<button onclick="showTable('all')">顯示全部</button>
<button onclick="showTable('python')">Python</button>
<button onclick="showTable('c')">C</button>
<button onclick="showTable('cpp')">C++</button>

<!-- 通用語法（所有語言通用） -->
<table class="all">
<thead>
<tr>
  <th>標準語法</th>
  <th>台羅對應</th>
  <th>適用語言</th>
</tr>
</thead>
<tbody>
<tr><td>if</td><td>nā</td><td>C / C++ / Python</td></tr>
<tr><td>else if / elif</td><td>nā_bô</td><td>C / C++ / Python</td></tr>
<tr><td>else</td><td>bô</td><td>C / C++ / Python</td></tr>
<tr><td>for</td><td>sûn_khuân</td><td>C / C++ / Python</td></tr>
<tr><td>while</td><td>tng</td><td>C / C++ / Python</td></tr>
<tr><td>break</td><td>thîng</td><td>C / C++ / Python</td></tr>
<tr><td>continue</td><td>kè_siòk</td><td>C / C++ / Python</td></tr>
<tr><td>return</td><td>huê</td><td>C / C++ / Python</td></tr>
<tr><td>true</td><td>tsin</td><td>C / C++ / Python</td></tr>
<tr><td>false</td><td>ké</td><td>C / C++ / Python</td></tr>
<tr><td>print / printf / cout</td><td>su_tshut</td><td>C / C++ / Python</td></tr>
<tr><td>input / scanf / cin</td><td>su_jip</td><td>C / C++ / Python</td></tr>
</tbody>
</table>

<!-- Python 對照表 -->
<table class="python">
<thead>
<tr>
  <th>標準語法</th>
  <th>台羅對應</th>
</tr>
</thead>
<tbody>
<tr><td>try-except-finally</td><td>nā_si_bô_hó_tō</td></tr>
<tr><td>def</td><td>li_sī</td></tr>
<tr><td>int</td><td>tsê_thâu</td></tr>
<tr><td>float</td><td>sòo</td></tr>
<tr><td>double</td><td>tsún_sòo</td></tr>
<tr><td>string</td><td>jī</td></tr>
<tr><td>malloc</td><td>pun</td></tr>
</tbody>
</table>

<!-- C 對照表 -->
<table class="c">
<thead>
<tr>
  <th>標準語法</th>
  <th>台羅對應</th>
</tr>
</thead>
<tbody>
<tr><td>switch</td><td>suán</td></tr>
<tr><td>case</td><td>hîng</td></tr>
<tr><td>default</td><td>ī_siat</td></tr>
<tr><td>struct</td><td>kiat_kòo</td></tr>
<tr><td>void</td><td>khang</td></tr>
<tr><td>malloc</td><td>pun</td></tr>
<tr><td>free</td><td>kái</td></tr>
</tbody>
</table>

<!-- C++ 對照表 -->
<table class="cpp">
<thead>
<tr>
  <th>標準語法</th>
  <th>台羅對應</th>
</tr>
</thead>
<tbody>
<tr><td>try</td><td>nā_si</td></tr>
<tr><td>catch</td><td>bô_hó</td></tr>
<tr><td>throw</td><td>tîng-tânn</td></tr>
<tr><td>class</td><td>tsióng</td></tr>
<tr><td>auto</td><td>tsū-tōng</td></tr>
<tr><td>vector</td><td>sò͘_tīn</td></tr>
<tr><td>map</td><td>tē_tôo</td></tr>
<tr><td>set</td><td>tsi̍p_hap</td></tr>
</tbody>
</table>

---

## 📜 **使用方式**
1. **在 C / C++ 程式中：**
   ```c
   #include "taiyu_c.h"  // C
   #include "taiyu_cpp.hpp"  // C++
   ```

2. **在 Python 程式中：**
   ```python
   from taiyu_py import *
   ```

---

## 📜 **專案資訊**
本專案基於 [`MIT License`](https://github.com/Alan20050829/taiyu-programming-language/blob/main/LICENSE)，自由開源！  
歡迎所有人聯繫我提出修改建議 📧 *linjunxieng0829@gmail.com*

---

<!-- JavaScript 動態切換表格 -->
<script>
function showTable(language) {
    var tables = document.querySelectorAll('table');
    tables.forEach(table => {
        if (language === 'all' || table.classList.contains(language)) {
            table.style.display = 'table';
        } else {
            table.style.display = 'none';
        }
    });
}
</script>

