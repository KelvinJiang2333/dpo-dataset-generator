# 故障排除指南

## 常见问题及解决方案

### 1. SystemExit: 3 错误

**问题描述：**
```
发生异常: SystemExit
3
File "app.py", line 395, in <module>
app.run(debug=True, host='0.0.0.0', port=5000)
```

**原因：**
- 端口5000被其他程序占用
- 调试模式重启时出现套接字错误
- 权限不足

**解决方案：**

#### 方案1：使用提供的启动脚本
```bash
# Windows
run.bat

# 或使用Python启动器
python start_server.py
```

#### 方案2：手动检查端口占用
```bash
# Windows - 查看端口占用
netstat -ano | findstr :5000

# 终止占用进程（替换PID）
taskkill /F /PID <进程ID>
```

#### 方案3：使用不同端口
修改 `backend/app.py` 最后一行：
```python
app.run(debug=True, host='127.0.0.1', port=5001)
```

同时更新 `frontend/script.js` 中的API地址：
```javascript
const API_BASE_URL = 'http://localhost:5001/api';
```

### 2. WinError 10038 套接字错误

**问题描述：**
```
OSError: [WinError 10038] 在一个非套接字上尝试了一个操作。
```

**解决方案：**
1. 重启命令提示符/终端
2. 使用管理员权限运行
3. 重启计算机（如果问题持续）

### 3. 模块导入错误

**问题描述：**
```
ModuleNotFoundError: No module named 'flask'
```

**解决方案：**
```bash
# 安装依赖
pip install -r requirements.txt

# 或单独安装
pip install flask flask-cors requests
```

### 4. 跨域(CORS)错误

**问题描述：**
前端无法连接到后端API

**解决方案：**
1. 确保后端服务器正在运行
2. 检查前端的API_BASE_URL配置
3. 确认防火墙设置

### 5. 数据集文件权限错误

**问题描述：**
无法读写数据集文件

**解决方案：**
1. 确保有文件写入权限
2. 检查磁盘空间
3. 使用管理员权限运行

## 最佳启动流程

### 推荐方式1：使用批处理脚本（Windows）
```bash
run.bat
```

### 推荐方式2：使用Python启动器
```bash
python start_server.py
```

### 推荐方式3：手动启动
```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 启动后端
cd backend
python app.py

# 3. 在新终端启动前端
cd frontend
python -m http.server 8080
```

## 环境要求检查

### Python版本
```bash
python --version
# 应该显示 Python 3.7 或更高版本
```

### 依赖包检查
```bash
pip list | findstr -i "flask requests"
```

### 端口可用性检查
```bash
# Windows
netstat -ano | findstr :5000
netstat -ano | findstr :8080

# 如果有输出，说明端口被占用
```

## 开发环境配置

### VS Code配置
如果使用VS Code开发，可以配置 `.vscode/launch.json`：

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Flask",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/backend/app.py",
            "console": "integratedTerminal",
            "justMyCode": true,
            "env": {
                "FLASK_ENV": "development"
            }
        }
    ]
}
```

### 环境变量
可以设置以下环境变量：
```bash
set FLASK_ENV=development
set FLASK_DEBUG=1
```

## 性能优化建议

1. **生产环境部署**
   - 使用 gunicorn 或 waitress 替代开发服务器
   - 配置反向代理（nginx）
   - 使用HTTPS

2. **开发环境优化**
   - 关闭调试模式的自动重载
   - 使用多线程模式
   - 定期清理临时文件

## 联系支持

如果以上解决方案都无效，请：

1. 记录完整的错误信息
2. 提供系统环境信息（操作系统、Python版本）
3. 通过GitHub Issues报告问题
4. 包含重现步骤

## 日志记录

启用详细日志记录：
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

查看Flask日志：
```bash
export FLASK_ENV=development
export FLASK_DEBUG=1
python app.py
```
