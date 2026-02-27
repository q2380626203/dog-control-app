[app]

# 应用基本信息
title = 机器狗控制
package.name = dogcontrol
package.domain = com.zsibot

# 源码目录
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# 版本信息
version = 1.0.0

# 应用入口
source.main = main.py

# 依赖的 Python 包
requirements = python3,kivy

# 安卓权限
android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE,CHANGE_WIFI_STATE

# 安卓架构 (arm64-v8a 对应 aarch64)
android.archs = arm64-v8a

# 安卓 API 级别
android.api = 31
android.minapi = 21
android.ndk = 25b

# Gradle 版本
android.gradle_dependencies = com.android.tools.build:gradle:7.2.0
android.accept_sdk_license = True

# 应用图标和启动画面
#icon.filename = %(source.dir)s/data/icon.png
#presplash.filename = %(source.dir)s/data/presplash.png

# 屏幕方向
orientation = portrait

# 全屏模式
fullscreen = 0

# 包含 SDK 库文件（暂时注释，需要将 SDK 文件添加到仓库）
# android.add_src = ../zsibot_sdk/lib/zsl-1/aarch64

# 添加原生库到 jniLibs
# android.add_jars =
# android.add_libs_armeabi_v7a =
# android.add_libs_arm64_v8a = ../zsibot_sdk/lib/zsl-1/aarch64/*.so

# 日志级别
log_level = 2

# 构建模式 (0 = debug, 1 = release)
android.release_artifact = apk

[buildozer]

# 日志级别
log_level = 2

# 警告为错误
warn_on_root = 1
