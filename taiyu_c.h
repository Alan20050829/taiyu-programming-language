#ifndef TAIYU_C_H
#define TAIYU_C_H

#include <stdio.h>
#include <stdlib.h>

// === 控制結構 ===
#define tsi if             
#define lú else            
#define iá else if         
#define ting switch        
#define ka case           
#define piàn default      

// === 迴圈 ===
#define thâu_lūn while     
#define ko for             
#define soat_thâu break    
#define khì_tshut continue 

// === 例外處理（C 模擬 try-catch）===
#include <setjmp.h>
jmp_buf taiyu_exception;
#define sióng_kì if (!setjmp(taiyu_exception)) 
#define bô_hó else 
#define tōa_mā longjmp(taiyu_exception, 1) 

// === 函數、型別與返回 ===
#define sái void 
#define khòng void 
#define huí_lai return 
#define kòo struct 

// === 變數型別 ===
#define su int             
#define phoo float         
#define tua double         
#define ji char*           
#define tsin 1             
#define bô 0               

// === 輸入輸出 ===
#define ìn_chhut printf    
#define tho̍k_tshíng scanf 
#define tsêng_hāi "\n"    

// === 記憶體管理（保留 malloc 和 free 原始名稱）===
#define bīn_chhòng malloc  

#endif // TAIYU_C_H
