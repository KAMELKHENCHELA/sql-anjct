شرح السكريبت:

    الإدخال:
        يأخذ السكريبت عنوان URL يحتوي على مدخلات غير محمية (على سبيل المثال، متغير GET مثل id).

    قائمة الحمولات (Payloads):
        يتم استخدام حمولات SQL Injection شائعة لاختبار التطبيق.

    إرسال الطلبات:
        يتم إرسال الطلبات باستخدام مكتبة requests مع الحمولات المختلفة.

    تحليل الرد:
        يتحقق السكريبت إذا كانت الاستجابة تشير إلى وجود خطأ في SQL أو نجاح الاختبار.

    إخراج النتيجة:
        يعرض النتائج لتوضيح إذا كانت نقطة الضعف موجودة أم لا.
pip install requests
تشغيل السكريبت:

    احفظ الكود في ملف، مثلاً sql_injection_test.py.
    شغّل السكريبت
    python sql_injection_test.py
إدخال URL:

    أدخل رابط صفحة تحتوي على إدخال عرضة للهجوم، مثل:http://example.com/vulnerable.php?id=
تحذير:

    هذا السكريبت يجب استخدامه فقط لاختبار الأنظمة التي تملكها أو لديك تصريح رسمي باختبارها.
    الهجوم على أنظمة الآخرين بدون إذن يعتبر غير قانوني ويعرضك للمساءلة القانونية.
