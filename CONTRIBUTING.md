# 贡献指南

**语言版本:** **中文** | [English](CONTRIBUTING_EN.md)

感谢您对DPO数据集生成工具的关注！我们欢迎任何形式的贡献，包括但不限于：

- 报告bug
- 提出新功能建议
- 提交代码改进
- 完善文档
- 分享使用经验

## 开发环境设置

### 1. 克隆仓库

```bash
git clone https://github.com/your-username/dpo-dataset-generator.git
cd dpo-dataset-generator
```

### 2. 安装依赖

```bash
# 安装Python依赖
pip install -r requirements.txt
```

### 3. 启动开发环境

```bash
# 启动后端服务
cd backend
python app.py

# 在另一个终端启动前端服务
cd frontend
python -m http.server 8080
```

然后在浏览器中访问 `http://localhost:8080`

## 代码贡献流程

### 1. Fork 仓库

点击仓库页面右上角的 "Fork" 按钮，将项目 fork 到您的 GitHub 账户下。

### 2. 创建分支

```bash
git checkout -b feature/your-feature-name
# 或者
git checkout -b fix/your-bug-fix
```

### 3. 进行开发

- 确保代码遵循项目的编码规范
- 添加必要的注释
- 如果是新功能，请更新相关文档

### 4. 测试

```bash
# 确保后端API正常工作
cd backend
python app.py

# 在浏览器中测试前端功能
# 测试主要功能：
# - 配置大模型连接
# - 生成DPO数据
# - 编辑数据集
# - 撤回操作
```

### 5. 提交代码

```bash
git add .
git commit -m "feat: 添加新功能描述"
# 或者
git commit -m "fix: 修复bug描述"
```

### 6. 推送并创建Pull Request

```bash
git push origin feature/your-feature-name
```

然后在GitHub上创建Pull Request。

## 代码规范

### Python代码规范

- 使用4个空格缩进
- 函数和类命名使用下划线命名法
- 添加适当的文档字符串
- 导入语句按标准库、第三方库、本地模块的顺序排列

示例：
```python
def generate_dpo_data(question: str, temperature_a: float, temperature_b: float) -> dict:
    """
    生成DPO数据对
    
    Args:
        question: 用户问题
        temperature_a: 生成chosen回复的温度
        temperature_b: 生成rejected回复的温度
    
    Returns:
        包含chosen和rejected回复的字典
    """
    # 实现代码...
```

### JavaScript代码规范

- 使用2个空格缩进
- 使用const/let而不是var
- 函数命名使用驼峰命名法
- 添加适当的注释

### CSS代码规范

- 使用2个空格缩进
- 类名使用连字符分隔
- 按功能分组排列属性

## 提交信息规范

请使用以下格式的提交信息：

```
<类型>: <简短描述>

[可选的详细描述]

[可选的相关issue]
```

类型包括：
- `feat`: 新功能
- `fix`: bug修复
- `docs`: 文档更新
- `style`: 代码格式调整
- `refactor`: 代码重构
- `test`: 添加测试
- `chore`: 构建过程或辅助工具的变动

示例：
```
feat: 添加流式响应支持

实现了流式显示模型生成过程，提升用户体验。
包括前端EventSource处理和后端流式响应。

Closes #123
```

## 报告问题

如果您发现bug或有功能建议，请通过GitHub Issues报告：

1. 检查是否已存在类似的issue
2. 使用清晰的标题描述问题
3. 提供详细的重现步骤
4. 包含您的环境信息（操作系统、Python版本等）
5. 如果是bug，请提供错误日志

### Bug报告模板

```markdown
**描述**
简要描述bug。

**重现步骤**
1. 进入页面...
2. 点击按钮...
3. 看到错误...

**预期行为**
描述您期望的正常行为。

**实际行为**
描述实际发生的情况。

**环境信息**
- 操作系统: [如 Windows 10]
- Python版本: [如 3.9.0]
- 浏览器: [如 Chrome 91.0]

**截图**
如果适用，添加截图帮助解释问题。

**附加信息**
添加任何其他相关信息。
```

### 功能建议模板

```markdown
**功能描述**
简要描述您希望添加的功能。

**使用场景**
描述这个功能的使用场景和价值。

**实现建议**
如果您有实现想法，请描述。

**替代方案**
描述您考虑过的其他解决方案。

**附加信息**
添加任何其他相关信息、截图或参考链接。
```

## 文档贡献

我们同样欢迎文档方面的贡献：

- 改进README.md
- 更新API文档
- 添加使用示例
- 翻译文档到其他语言

## 社区准则

请遵守以下准则，营造友好的社区环境：

- 尊重所有贡献者
- 使用友好和包容的语言
- 接受建设性的批评
- 专注于对社区最有利的事情
- 对其他社区成员表示同理心

## 许可证

通过贡献代码，您同意您的贡献将在MIT许可证下发布。

## 联系方式

如果您有任何问题，可以通过以下方式联系：

- 创建GitHub Issue
- 发送邮件到 [维护者邮箱]

感谢您的贡献！
