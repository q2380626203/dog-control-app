# 云端构建 APK 指南

使用 GitHub Actions 自动构建 Android APK，无需本地 Linux 环境。

## 优势

- ✅ 无需本地 Linux/WSL 环境
- ✅ 自动化构建，推送代码即可
- ✅ 免费使用（GitHub 提供的 CI/CD）
- ✅ 构建环境一致，避免本地环境问题
- ✅ 支持多人协作开发

## 使用步骤

### 1. 准备 GitHub 仓库

```bash
# 在项目目录初始化 Git
cd dog_control_app
git init

# 添加文件
git add .
git commit -m "Initial commit"

# 关联远程仓库（替换为你的仓库地址）
git remote add origin https://github.com/你的用户名/dog-control-app.git
git push -u origin main
```

### 2. 确保项目结构正确

```
dog_control_app/
├── .github/
│   └── workflows/
│       └── build-apk.yml    # GitHub Actions 配置
├── main.py
├── buildozer.spec
├── requirements.txt
└── README.md

zsibot_sdk/
└── lib/zsl-1/aarch64/*.so   # SDK 库文件
```

### 3. 推送代码触发构建

```bash
# 修改代码后
git add .
git commit -m "Update code"
git push

# GitHub Actions 会自动开始构建
```

### 4. 查看构建进度

1. 打开 GitHub 仓库页面
2. 点击顶部的 **Actions** 标签
3. 查看最新的构建任务
4. 点击任务查看详细日志

### 5. 下载构建好的 APK

构建完成后：

1. 在 Actions 页面找到成功的构建
2. 滚动到页面底部的 **Artifacts** 区域
3. 点击 `dog-control-apk` 下载 APK 文件
4. 解压 ZIP 文件，得到 APK

## 手动触发构建

如果不想推送代码，也可以手动触发：

1. 进入 GitHub 仓库的 **Actions** 页面
2. 选择 **Build Android APK** workflow
3. 点击右侧的 **Run workflow** 按钮
4. 选择分支，点击 **Run workflow**

## 构建时间

- 首次构建：约 20-30 分钟（需要下载 Android SDK/NDK）
- 后续构建：约 5-10 分钟（使用缓存）

## 常见问题

### 1. 构建失败

查看 Actions 日志，常见原因：
- SDK 库文件路径不正确
- buildozer.spec 配置错误
- 依赖包版本冲突

### 2. 找不到 APK 文件

确保：
- 构建任务显示为绿色（成功）
- 在 Artifacts 区域查找下载链接
- APK 在 ZIP 压缩包内

### 3. GitHub Actions 配额

GitHub 免费账户提供：
- 公开仓库：无限制
- 私有仓库：每月 2000 分钟

## 高级配置

### 自动发布 Release

修改 `.github/workflows/build-apk.yml`，添加发布步骤：

```yaml
- name: 创建 Release
  if: startsWith(github.ref, 'refs/tags/')
  uses: softprops/action-gh-release@v1
  with:
    files: dog_control_app/bin/*.apk
```

然后打标签触发：
```bash
git tag v1.0.0
git push origin v1.0.0
```

### 定时构建

添加定时触发（每周构建一次）：

```yaml
on:
  schedule:
    - cron: '0 0 * * 0'  # 每周日 UTC 0:00
```

## 对比其他方案

| 方案 | 优点 | 缺点 |
|------|------|------|
| **云端构建** | 无需本地环境，自动化 | 需要 GitHub 账号，首次较慢 |
| **WSL** | 本地控制，速度快 | 需要配置环境 |
| **虚拟机** | 完整 Linux 环境 | 占用资源多 |
| **Docker** | 环境一致 | 需要学习 Docker |

## 总结

云端构建适合：
- Windows 用户不想配置 WSL
- 团队协作开发
- 需要自动化 CI/CD
- 多人共享构建结果

推送代码后，喝杯咖啡，APK 就构建好了！
