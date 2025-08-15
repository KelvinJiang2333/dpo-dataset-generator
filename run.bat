@echo off
echo ================================================
echo DPO数据集生成工具 - 启动脚本
echo ================================================

cd /d "%~dp0"

echo 检查Python环境...
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未找到Python，请确保Python已安装并添加到PATH
    pause
    exit /b 1
)

echo 检查依赖包...
python -c "import flask, flask_cors, requests" >nul 2>&1
if errorlevel 1 (
    echo 错误: 缺少必要的依赖包，正在安装...
    pip install -r requirements.txt
)

echo 启动后端服务器...
cd backend
python app.py

if errorlevel 1 (
    echo.
    echo 启动失败，可能的解决方案：
    echo 1. 端口5000被占用，请关闭占用端口的程序
    echo 2. 使用管理员权限运行此脚本
    echo 3. 手动运行: cd backend ^&^& python app.py
    echo.
    pause
)
