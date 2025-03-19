#ifndef TAIYU_C_H
#define TAIYU_C_H

#include <stdio.h>
#include <stdlib.h>

// === 控制結構 ===
#define nā if             
#define bô else            
#define nā_bô else if         
#define suán switch        
#define hîng case           
#define ī_siat default      

// === 迴圈 ===
#define tng while     
#define sûn_khuân for             
#define thîng break    
#define kè-siòk continue 

// === 例外處理（C 模擬 try-catch）===
#include <setjmp.h>
jmp_buf taiyu_exception;
#define nā_sī if (!setjmp(taiyu_exception)) 
#define bô_hó else 
#define thiàu longjmp(taiyu_exception, 1) 

// === 函數、型別與返回 === 
#define khang void 
#define huê return 
#define kiat_kòo struct 

// === 變數型別 ===
#define tsê_thâu int             
#define sòo float         
#define tsún_sòo double         
#define jī char*           
#define tsin true             
#define ké false               

// === 輸入輸出 ===
#define su_tshut printf    
#define su_jìp scanf 

// === 記憶體管理 ===
#define pun malloc
#define kái free  

#endif // TAIYU_C_H
