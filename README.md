# 机器狗控制 Android APP

基于 Kivy 框架开发的机器狗控制应用，支持打包成 Android APK。

## 功能特性

- ✅ 图形化控制界面
- ✅ 支持基础动作（站立、趴下）
- ✅ 支持移动控制（前后左右）
- ✅ 支持旋转控制（左转右转）
- ✅ 支持特技动作（跳跃、前跳、后空翻、握手）
- ✅ 实时日志显示
- ✅ WiFi 连接机器狗

## 项目结构

```
dog_control_app/
├── main.py              # 主程序
├── buildozer.spec       # 打包配置
├── requirements.txt     # Python 依赖
└── README.md           # 说明文档
```

## 环境要求

### 开发环境
- Python 3.8+
- Kivy 2.0+
- Buildozer (用于打包 APK)

### 目标设备
- Android 5.0+ (API 21+)
- ARM64 架构 (arm64-v8a)
- 支持 WiFi 连接

## 安装步骤

### 1. 安装开发环境 (Linux/WSL)

```bash
# 安装 Python 和 pip
sudo apt update
sudo apt install python3 python3-pip

# 安装 Kivy
pip3 install kivy

# 安装 Buildozer
pip3 install buildozer

# 安装 Android 构建依赖
sudo apt install -y git zip unzip openjdk-17-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
```

### 2. 准备项目

```bash
cd dog_control_app

# 确保 SDK 库文件在正确位置
# 项目结构应该是:
# dog_control_app/
# └── main.py
# zsibot_sdk/
#     └── lib/zsl-1/aarch64/*.so
```

### 3. 打包 APK

```bash
# 初始化 buildozer (首次运行)
buildozer init

# 打包 debug 版本
buildozer android debug

# 打包完成后，APK 位于:
# bin/dogcontrol-1.0.0-arm64-v8a-debug.apk
```

### 4. 安装到手机

```bash
# 通过 USB 安装
adb install bin/dogcontrol-1.0.0-arm64-v8a-debug.apk

# 或者直接复制 APK 到手机安装
```

## 使用说明

### 1. 连接机器狗 WiFi
- 打开手机 WiFi 设置
- 连接到机器狗的 WiFi 热点
- 确保手机 IP 在 192.168.234.x 网段

### 2. 配置 APP
- 打开 APP
- 输入本地 IP（如 192.168.234.9）
- 输入机器狗 IP（默认 192.168.234.1）
- 点击"连接机器狗"

### 3. 控制机器狗
- 连接成功后，点击各个按钮控制机器狗
- 查看底部日志了解执行状态

## 控制命令说明

| 按钮 | 功能 | 说明 |
|------|------|------|
| 站起来 | 机器狗站立 | 基础姿态 |
| 趴下 | 机器狗趴下 | 休息姿态 |
| 前进 | 向前移动 2秒 | 速度 0.2 m/s |
| 后退 | 向后移动 2秒 | 速度 -0.2 m/s |
| 左移 | 向左平移 2秒 | 速度 0.2 m/s |
| 右移 | 向右平移 2秒 | 速度 -0.2 m/s |
| 左转 | 原地左转 2秒 | 角速度 0.3 rad/s |
| 右转 | 原地右转 2秒 | 角速度 -0.3 rad/s |
| 跳跃 | 原地跳跃 | 需要 4秒 |
| 前跳 | 向前跳跃 | 需要 4秒 |
| 后空翻 | 后空翻动作 | 需要 4秒 |
| 握手 | 握手动作 | 需要 4秒 |

## 开发测试

### 在 PC 上测试 (需要 Linux/WSL)

```bash
# 运行程序
python3 main.py
```

**注意**: PC 测试时需要修改 `main.py` 中的架构检测逻辑，或在 Linux 环境下运行。

## 常见问题

### 1. 打包失败
- 确保在 Linux 或 WSL 环境下运行
- 检查是否安装了所有依赖
- 尝试清理缓存: `buildozer android clean`

### 2. 连接失败
- 确认手机已连接到机器狗 WiFi
- 检查 IP 地址是否正确
- 确保机器狗已开机并正常运行

### 3. SDK 库未找到
- 确保 SDK 库文件在正确位置
- 检查 `buildozer.spec` 中的路径配置
- 确认手机是 ARM64 架构

### 4. 命令执行无响应
- 检查网络连接是否稳定
- 查看日志了解错误信息
- 尝试重新连接机器狗

## 后续扩展

- [ ] 添加语音识别功能
- [ ] 添加摄像头视频流显示
- [ ] 添加自定义动作序列
- [ ] 添加遥控器模式
- [ ] 添加传感器数据显示

## 许可证

本项目基于 zsibot_sdk 开发，请遵守相关许可协议。

## 联系方式

如有问题，请参考 zsibot_sdk 官方文档或联系技术支持。
