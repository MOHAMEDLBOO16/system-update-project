[app]
title = System Update
package.name = systemupdate
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# المتطلبات الأساسية للكود الخاص بك
requirements = python3,kivy==2.1.0,requests,urllib3,idna,certifi

orientation = portrait
fullscreen = 0

# إعدادات الأندرويد الضرورية (تأكد من هذه الأرقام بدقة)
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.accept_sdk_license = True
android.permissions = INTERNET
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
