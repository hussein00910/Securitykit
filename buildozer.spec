[app]
title = Security Toolkit
package.name = securitytoolkit
package.domain = org.securitytoolkit
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0
requirements = python3,kivy==2.3.0,requests,pillow
android.api = 33
android.minapi = 21
android.archs = arm64-v8a
android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE
orientation = portrait
fullscreen = 0
log_level = 2

[buildozer]
log_level = 2
warn_on_root = 1
