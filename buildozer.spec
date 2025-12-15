[app]

# اسم التطبيق
title = تطبيق بيثون

# اسم الحزمة (يجب أن يكون فريداً)
package.name = pythonandroidapp

# اسم المجال
package.domain = com.example

# إصدار التطبيق
version = 1.0

# مصدر الكود
source.dir = .

# الملف الرئيسي
source.main = main.py

# إصدار Android SDK
android.api = 33
android.minapi = 21
android.sdk = 23
android.ndk = 23b
android.ndk_api = 21

# أذونات Android (اختياري)
# android.permissions = INTERNET

# أصلاحات Kivy
p4a.branch = master
android.arch = arm64-v8a, armeabi-v7a

# مكتبات Python المطلوبة
requirements = python3, kivy

# ميزات OpenGL
android.gradle_dependencies = ''
android.add_src = false

# التكوين
[buildozer]
log_level = 2
warn_on_root = 1
