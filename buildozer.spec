[app]
title = System Update
package.name = systemupdate
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
# المكتبات المطلوبة لعمل الكود
requirements = python3,kivy,requests,urllib3,idna,certifi
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
# صلاحية الإنترنت ضرورية لإرسال التنبيه لتلجرام
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
