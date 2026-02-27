# 快速部署指南

## 📋 当前状态

✅ Git 仓库已初始化
✅ 所有文件已提交
✅ GitHub Actions 配置已就绪

## 🚀 下一步操作

### 1. 在 GitHub 上创建仓库

访问 https://github.com/new 创建新仓库：

- Repository name: `dog-control-app`
- Description: `机器狗语音控制 Android APP`
- 选择 Public（公开仓库，免费使用 Actions）
- **不要**勾选 "Initialize this repository with a README"
- 点击 "Create repository"

### 2. 关联远程仓库并推送

```bash
cd "d:\project\机器狗语音控制\dog_control_app"

# 关联远程仓库（替换为你的 GitHub 用户名）
git remote add origin https://github.com/你的用户名/dog-control-app.git

# 推送代码
git push -u origin master
```

### 3. 查看自动构建

推送成功后：

1. 访问你的 GitHub 仓库
2. 点击顶部的 **Actions** 标签
3. 会看到 "Build Android APK" 任务正在运行
4. 点击任务查看实时构建日志

### 4. 下载 APK

构建完成后（约 20-30 分钟）：

1. 在 Actions 页面找到成功的构建（绿色✓）
2. 滚动到页面底部的 **Artifacts** 区域
3. 点击 `dog-control-apk` 下载
4. 解压 ZIP 文件得到 APK

### 5. 安装到手机

```bash
# 方法 1: 通过 ADB 安装
adb install dogcontrol-1.0.0-arm64-v8a-debug.apk

# 方法 2: 直接传输到手机安装
# 将 APK 文件复制到手机，点击安装
```

## 📝 后续更新

修改代码后，只需：

```bash
git add .
git commit -m "更新描述"
git push
```

GitHub Actions 会自动重新构建 APK。

## ⚠️ 注意事项

1. **SDK 库文件**: 确保 `../zsibot_sdk/lib/zsl-1/aarch64/*.so` 路径正确
2. **仓库类型**: 建议使用公开仓库（免费无限 Actions 时长）
3. **构建时间**: 首次约 20-30 分钟，后续 5-10 分钟

## 🎉 完成

现在你已经拥有了一个自动化的 Android APP 构建流程！
