# taiyu_py.py
import ctypes
from functools import wraps

# === 自訂例外類別 ===
class BreakLoop(Exception):
    """模擬 break"""
    pass

class ContinueLoop(Exception):
    """模擬 continue"""
    pass

class ReturnValue(Exception):
    """模擬 return"""
    def __init__(self, value):
        self.value = value

# === 控制結構 ===
def nā(condition, true_func, false_func=None):
    if condition:
        return true_func() if callable(true_func) else true_func
    elif false_func:
        return false_func() if callable(false_func) else false_func

def nā_bô(condition, true_func, false_func=None):
    return tsi(condition, true_func, false_func)

def bô(true_func):
    return true_func() if callable(true_func) else true_func

# === 迴圈 ===
def sûn_khuân(iterable, func):
    """模擬 for 迴圈"""
    for item in iterable:
        try:
            func(item)
        except BreakLoop:
            break
        except ContinueLoop:
            continue

def tng(condition_func, action_func):
    """模擬 while 迴圈"""
    while condition_func():
        try:
            action_func()
        except BreakLoop:
            break
        except ContinueLoop:
            continue

def thîng():
    """模擬 break"""
    raise BreakLoop()

def kè_siòk():
    """模擬 continue"""
    raise ContinueLoop()

# === 例外處理 ===
def nā_si_bô_hó_tō(try_func, except_func=None, finally_func=None):
    """模擬 try-except-finally"""
    try:
        try_func()
    except Exception as e:
        if except_func:
            except_func(e)
    finally:
        if finally_func:
            finally_func()

# === 函數與類別 ===
def li_sī(func):
    """模擬 def（函數定義），並支援 return"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ReturnValue as ret:
            return ret.value
    return wrapper

def thióng(cls):
    """模擬 class"""
    return cls

def huê(value):
    """模擬 return，回傳值不拋出異常"""
    raise ReturnValue(value)

# === 輸入輸出 ===
def su_tshut(*args, **kwargs):
    """模擬 print"""
    print(*args, **kwargs)

def su_jip(prompt):
    """模擬 input"""
    return input(prompt)

# === 變數型別 ===
tsê_thâu = int  # 模擬 int
sòo = float  # 模擬 float
jī = str  # 模擬 string
khang = None  # 模擬 None（類似於 void）

# === 記憶體管理（模擬 malloc/free）===
def pun(size, dtype="char"):
    """模擬 malloc，可分配不同類型的記憶體"""
    if dtype == "char":
        return ctypes.create_string_buffer(size)
    elif dtype == "int":
        return (ctypes.c_int * size)()
    elif dtype == "float":
        return (ctypes.c_float * size)()
    else:
        raise ValueError("未知的記憶體類型")

# === 布林值 ===
tsin = True  # 模擬 True
ké = False  # 模擬 False
