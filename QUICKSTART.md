# 🚀 快速启动指南

## 1️⃣ 环境准备 (5分钟)

### 检查Python环境
```bash
python --version  # 需要 Python 3.7+
```

### 自动安装依赖
```bash
python install.py  # 自动检查并安装所有依赖
```

### 手动安装依赖
```bash
pip install -r requirements.txt
```

## 2️⃣ 启动服务 (1分钟)

### 方式一：使用启动脚本 (推荐)
```bash
python start_server.py
```

### 方式二：直接启动
```bash
cd backend
python app.py
```

看到 `Running on http://127.0.0.1:5000` 表示启动成功！

## 3️⃣ 打开前端 (1分钟)

### 方式一：直接打开文件
双击 `frontend/index.html` 文件

### 方式二：使用HTTP服务器
```bash
cd frontend
python -m http.server 8080
# 然后访问 http://localhost:8080
```

## 4️⃣ 配置API (2分钟)

在页面顶部的"大模型配置"区域：

1. **API地址**: 
   - vLLM: `http://localhost:8000/v1`
   - OpenAI: `https://api.openai.com/v1`
   - 其他服务: 参考对应文档

2. **API密钥**: 输入您的API密钥

3. **模型名称**: 
   - OpenAI: `gpt-4o-mini`
   - vLLM: `Qwen/Qwen2-7B-Instruct`
   - 其他: 根据服务提供商

4. **温度设置**: 
   - 温度A: `0.2` (确定性)
   - 温度B: `1.0` (创造性)

5. 点击 **"测试连接"** 验证配置

6. 点击 **"保存配置"** 保存设置

## 5️⃣ 生成数据 (开始使用)

### 基础使用
1. 输入问题，点击"提交问题"
2. 等待生成两个候选回复
3. 选择更优的回复 (点击"选择A"或"选择B")
4. 数据自动保存到 `dpo_simple_dataset.json`

### 连续问答 (新功能!)
1. 完成一轮问答后，点击 **"💬 继续问答"**
2. 输入框会高亮，表示进入连续模式
3. 输入新问题，系统会基于之前的回复生成上下文
4. 随时点击 **"❌ 取消继续问答"** 退出

### 其他功能
- **编辑回复**: 点击"编辑A"或"编辑B"自定义回复
- **重新生成**: 点击"⟳ 重新生成"获得新的候选
- **撤回操作**: 点击"↩ 撤回上一步"撤销操作
- **系统提示词**: 点击"编辑系统提示词"自定义AI行为

## 🎯 常见配置示例

### vLLM本地服务
```
API地址: http://localhost:8000/v1
API密钥: your-key
模型名称: Qwen/Qwen2-7B-Instruct
```

### OpenAI API
```
API地址: https://api.openai.com/v1
API密钥: sk-proj-your-key
模型名称: gpt-4o-mini
```

### Ollama服务
```
API地址: http://localhost:11434/v1
API密钥: ollama
模型名称: qwen2.5:7b
```

## ❓ 遇到问题？

### 常见错误
1. **连接失败**: 检查API地址和密钥
2. **模型不存在**: 确认模型名称正确
3. **权限错误**: 检查API密钥权限
4. **端口占用**: 使用 `start_server.py` 自动处理

### 获取帮助
- 📖 完整文档: [README.md](README.md)
- 🐛 报告问题: [GitHub Issues](https://github.com/KelvinJiang2333/dpo-dataset-generator/issues)
- 💬 交流讨论: GitHub Discussions

---

**🎉 恭喜！您已经可以开始生成高质量的DPO数据集了！**
