# DPO数据集生成工具

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**语言版本:** **中文** | [English](README_EN.md)

> 🚀 **新手快速上手**: [5分钟快速启动指南](QUICKSTART.md) | 📊 **当前版本**: v1.3.0

这是一个简单易用的DPO（Direct Preference Optimization）数据集生成Web工具。用户可以通过前端界面输入大模型API配置，生成两个不同温度的回答，然后选择更优的回答来构建高质量的DPO训练数据集。

## English Description

A simple and easy-to-use web tool for generating DPO (Direct Preference Optimization) datasets. Users can configure large language model APIs through the frontend interface, generate two responses with different temperatures, and then select the better response to build high-quality DPO training datasets.

**For full English documentation, please see: [README_EN.md](README_EN.md)**

## 🚀 功能特点

### 🔧 核心功能
1. **智能配置管理**：前端可配置大模型API地址、密钥、模型名称和温度参数
2. **连接测试**：一键测试大模型API连接是否正常
3. **双候选生成**：自动生成两个不同温度的候选回答（低温确定性 vs 高温创造性）
4. **多样化操作**：支持选择回答、编辑回答、重新生成、跳过等多种操作模式
5. **实时保存**：自动保存用户选择到标准DPO格式的JSON文件
6. **流式显示**：支持实时显示模型生成过程，体验更流畅

### 🎯 新增亮点功能
7. **连续问答模式**：支持基于已选择回复的上下文继续对话，生成多轮对话DPO数据
8. **系统提示词编辑**：可视化编辑系统提示词，内置5种专业模板（默认助手、创意写作、技术专家、教育导师、商务专业）
9. **配置管理**：支持配置导出/导入、本地存储、一键重置等便捷功能
10. **多语言支持**：完整的中英文双语界面
11. **撤回功能**：支持撤回上一步操作，方便调整和重新选择
12. **状态反馈**：实时状态提示和错误反馈，用户体验友好

## 系统要求

- Python 3.7+
- 兼容OpenAI API格式的大模型服务
- 现代浏览器（Chrome、Firefox、Edge等）

## 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/KelvinJiang2333/dpo-dataset-generator.git
cd dpo-dataset-generator
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 安全配置

**重要：请先配置您的API信息**

项目提供了配置示例文件 `config.example.json`，包含多种大模型服务的配置模板。请根据您的实际环境进行配置。

**安全建议：**
- 不要在代码中硬编码API密钥
- 建议将敏感信息存储在环境变量中
- 生产环境请使用HTTPS
- 定期轮换API密钥

## 启动系统

1. 启动后端API服务器：

```bash
cd backend
python app.py
```

后端服务将在 http://localhost:5000 上运行。

2. 打开前端界面：

可以使用任何静态文件服务器来提供前端文件，例如：

```bash
# 如果安装了Python
cd frontend
python -m http.server 8080
```

然后在浏览器中访问 http://localhost:8080

或者使用VS Code的Live Server插件等工具。

## 使用说明

### 1. 配置大模型连接

1. 在页面顶部的"大模型配置"区域输入您的API参数：
   - **API地址**：如 `http://localhost:8888/v1`（vLLM）或 `https://api.openai.com/v1`（OpenAI）
   - **API密钥**：您的API密钥（请妥善保管，不要泄露）
   - **模型名称**：如 `Qwen2-7B-Instruct`、`gpt-3.5-turbo` 等
   - **温度A**：生成第一个候选回复的温度（建议0.2，较低温度，回复更确定性）
   - **温度B**：生成第二个候选回复的温度（建议1.0，较高温度，回复更多样性）

2. 点击"编辑系统提示词"自定义AI的行为和回复风格：
   - 可以选择预设模板：默认助手、创意写作、技术专家、教育导师、商务专业
   - 或者自定义编写系统提示词
   - 实时预览系统提示词效果

3. 配置管理选项：
   - **测试连接**：验证API配置是否正确
   - **保存配置**：将配置保存到浏览器本地存储
   - **重置配置**：恢复为默认配置值
   - **清除配置**：删除所有保存的配置数据
   - **导出配置**：将配置导出为JSON文件（不包含API密钥）
   - **导入配置**：从JSON文件导入配置

**注意**：配置信息会保存在浏览器的本地存储中，请确保在可信任的环境中使用。

### 2. 生成DPO数据

#### 📝 基础问答模式

1. 在问题输入框中输入您的问题，点击"提交问题"
2. 系统会同时生成两个候选回复：
   - **回复A**：使用较低温度(默认0.2)，更确定性和一致性
   - **回复B**：使用较高温度(默认1.0)，更具创造性和多样性
3. 根据质量选择更优的回复：
   - 点击"**选择A**"：将A作为chosen，B作为rejected
   - 点击"**选择B**"：将B作为chosen，A作为rejected
   - 点击"**编辑A**"或"**编辑B**"：修改回复后保存
   - 点击"**重新生成**"：重新生成两个候选回复


#### 🔄 连续问答模式（新功能）

1. 完成一轮问答并选择回复后，会出现"**💬 继续问答**"按钮
2. 点击进入连续问答模式：
   - 输入框会高亮显示，提示当前处于连续模式
   - 输入新问题会基于之前的选择回复作为上下文
   - 生成的DPO数据将包含完整的多轮对话历史
3. 退出连续模式：
   - 点击"**❌ 取消继续问答**"按钮
   - 或提交新问题后会自动退出连续模式

#### 📊 其他操作

- **撤回上一步**：点击"**↩ 撤回上一步**"可以撤销最近的操作
- **查看对话历史**：页面会实时显示当前的对话历史
- **状态提示**：底部状态栏会显示当前操作状态和提示信息

### 3. 数据集格式

生成的数据集采用 **Sharegpt 格式**，完全兼容主流的DPO训练框架，包括但不限于：
- LLaMA-Factory
- Transformers DPO Trainer
- DeepSpeed-Chat
- TRL (Transformer Reinforcement Learning)

#### 📋 数据格式示例

**单轮对话DPO数据：**
```json
{
  "conversations": [
    {
      "from": "system",
      "value": "你是一个有用的AI助手..."
    },
    {
      "from": "human", 
      "value": "什么是机器学习？"
    }
  ],
  "chosen": {
    "from": "gpt",
    "value": "机器学习是人工智能的一个分支，它使计算机能够通过数据学习并做出预测或决策，而无需明确编程。"
  },
  "rejected": {
    "from": "gpt", 
    "value": "机器学习就是让机器自己学会做事情。"
  }
}
```

**多轮对话DPO数据（连续问答模式）：**
```json
{
  "conversations": [
    {
      "from": "system",
      "value": "你是一个有用的AI助手..."
    },
    {
      "from": "human",
      "value": "什么是机器学习？"
    },
    {
      "from": "gpt",
      "value": "机器学习是人工智能的一个分支..."
    },
    {
      "from": "human",
      "value": "请举一个具体的应用例子"
    }
  ],
  "chosen": {
    "from": "gpt",
    "value": "一个典型的例子是推荐系统，如Netflix根据你的观看历史推荐电影..."
  },
  "rejected": {
    "from": "gpt",
    "value": "比如图像识别、语音识别等都是机器学习的应用。"
  }
}
```

#### 🔧 LLaMA-Factory 配置

如果您使用LLaMA-Factory进行DPO训练，可以使用以下配置：

```json
{
  "dpo_dataset": {
    "file_name": "dpo_simple_dataset.json",
    "formatting": "sharegpt",
    "ranking": true,
    "columns": {
      "messages": "conversations",
      "chosen": "chosen", 
      "rejected": "rejected"
    }
  }
}
```

### 4. 数据集输出

- 生成的DPO数据集会自动保存为 `dpo_simple_dataset.json` 文件
- 位置：项目根目录下
- 格式：标准的Sharegpt格式，可直接用于各种DPO训练框架
- 实时保存：每次选择回复后立即保存，数据安全有保障

## 🌐 支持的大模型服务

该工具支持任何兼容OpenAI ChatCompletions API格式的服务：

- 🤖 **OpenAI API**：GPT-3.5、GPT-4系列、GPT-4o系列
- 🏠 **本地vLLM服务**：Qwen、LLaMA、Mistral、ChatGLM等开源模型  
- 🔧 **Ollama服务**：本地部署的各种开源模型
- ☁️ **云端API服务**：阿里云百炼、智谱AI、讯飞星火等（通过代理）
- 🔌 **其他兼容服务**：任何实现了OpenAI API格式的推理服务

## ⚙️ 配置示例

### 🏠 vLLM本地服务
```bash
API地址: http://localhost:8000/v1
API密钥: your-key
模型名称: Qwen/Qwen2-7B-Instruct
温度A: 0.2  # 确定性回复
温度B: 1.0  # 创造性回复
```

### 🤖 OpenAI API
```bash
API地址: https://api.openai.com/v1
API密钥: sk-proj-your-openai-key
模型名称: gpt-4o-mini
温度A: 0.3
温度B: 0.9
```

### 🔧 Ollama服务
```bash
API地址: http://localhost:11434/v1
API密钥: ollama
模型名称: qwen2.5:7b
温度A: 0.2
温度B: 1.0
```

### ☁️ 国内API服务（示例）
```bash
# 智谱AI GLM-4
API地址: https://open.bigmodel.cn/api/paas/v4
API密钥: your-zhipu-api-key
模型名称: glm-4

# 阿里云百炼
API地址: https://dashscope.aliyuncs.com/compatible-mode/v1
API密钥: sk-your-dashscope-key  
模型名称: qwen-turbo
```

## 🛠️ 故障排除

### 常见问题解决

**1. API连接失败**
- ✅ 检查API地址是否正确（注意末尾的 `/v1`）
- ✅ 验证API密钥是否有效
- ✅ 确认模型名称是否正确
- ✅ 检查网络连接和防火墙设置

**2. 模型回复生成失败**
- ✅ 确认模型支持聊天补全API
- ✅ 检查温度参数是否在合理范围内(0-2)
- ✅ 验证系统提示词格式是否正确

**3. 数据保存问题**
- ✅ 确认有写入文件的权限
- ✅ 检查磁盘空间是否充足
- ✅ 确认项目目录可写

**4. 前端界面异常**
- ✅ 清除浏览器缓存
- ✅ 检查浏览器控制台错误信息
- ✅ 确认后端服务正常运行

### 📊 性能优化建议

**温度参数设置：**
- 🎯 **温度A (0.1-0.3)**：适合生成准确、一致的回复
- 🎨 **温度B (0.8-1.2)**：适合生成创造性、多样化的回复
- ⚖️ **差值建议**：两个温度差值建议在0.5以上，确保回复多样性

**系统提示词建议：**
- 📝 明确定义AI的角色和行为准则
- 🎯 包含具体的回复质量要求
- 🔧 根据应用场景选择合适的预设模板

## 🤝 贡献指南

我们欢迎任何形式的贡献！以下是参与方式：

### 🐛 报告问题
- 在GitHub Issues中报告bug
- 提供详细的复现步骤
- 包含错误信息和环境信息

### 💡 功能建议
- 通过Issues提出新功能建议
- 详细描述功能需求和使用场景
- 参与功能设计讨论

### 🔧 代码贡献
- Fork项目到您的GitHub
- 创建功能分支进行开发
- 提交Pull Request
- 详细说明：[CONTRIBUTING.md](CONTRIBUTING.md)

### 📚 文档改进
- 改进README和文档说明
- 添加使用示例和教程
- 翻译多语言文档

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- 感谢所有为此项目做出贡献的开发者
- 感谢开源社区提供的优秀工具和库
- 特别感谢使用并反馈的每一位用户

## ⭐ Star History

如果这个项目对您有帮助，请考虑给我们一个Star！⭐

## 📞 联系我们

如果您有任何问题或建议，欢迎通过以下方式联系：

- 📧 **GitHub Issues**: [提交问题或建议](https://github.com/KelvinJiang2333/dpo-dataset-generator/issues)
- 🐛 **Bug报告**: [报告问题](https://github.com/KelvinJiang2333/dpo-dataset-generator/issues/new?template=bug_report.md)  
- 💡 **功能请求**: [功能建议](https://github.com/KelvinJiang2333/dpo-dataset-generator/issues/new?template=feature_request.md)

---

---

**🎉 项目地址**: https://github.com/KelvinJiang2333/dpo-dataset-generator

**⭐ 如果这个项目对您有帮助，请给我们一个Star！**

## 📅 更新日志

### v1.3.0 (最新)
🚀 **重大新功能**
- ✨ **连续问答模式**: 支持基于已选择回复的上下文继续对话，生成多轮对话DPO数据
- 🎯 **智能状态管理**: 清晰的继续问答状态提示和退出机制  
- 🎨 **视觉优化**: 继续模式下的输入框高亮和专门的按钮样式
- ↩️ **撤回功能**: 支持撤销上一步操作，方便调整选择
- 🌐 **完整多语言**: 中英文双语界面全面优化

🔧 **功能改进**
- 📝 简化数据集管理（移除编辑功能，专注生成）
- 🎯 优化用户交互逻辑和状态反馈
- 🐛 修复多项稳定性问题

### v1.2.0
- 新增完整的配置管理功能
- 支持配置导出/导入（JSON格式）
- 添加清除配置功能
- 改进温度参数标签说明
- 优化配置按钮布局
- 增强安全性（导出时不包含API密钥）

### v1.1.0
- 新增系统提示词可视化编辑器
- 支持多种预设系统提示词模板（默认助手、创意写作、技术专家、教育导师、商务专业）
- 实时预览系统提示词效果
- 字符计数和智能提醒
- 系统提示词配置持久化保存

### v1.0.0
- 初始版本发布
- 支持多种大模型API
- 流式响应显示
- DPO数据集生成和管理
- 可视化数据编辑界面