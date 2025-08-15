#!/usr/bin/env python3
"""
DPO数据集生成工具 - 服务器启动脚本
支持自动端口检测和错误恢复
"""

import os
import sys
import socket
import subprocess
import signal
import time
from pathlib import Path

def check_port(host, port):
    """检查端口是否可用"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            return result != 0  # 返回True表示端口可用
    except:
        return False

def find_available_port(host='127.0.0.1', start_port=5000, max_attempts=10):
    """查找可用端口"""
    for port in range(start_port, start_port + max_attempts):
        if check_port(host, port):
            return port
    return None

def kill_process_on_port(port):
    """终止占用指定端口的进程（Windows）"""
    try:
        # 查找占用端口的进程
        result = subprocess.run(
            f'netstat -ano | findstr :{port}',
            shell=True,
            capture_output=True,
            text=True
        )
        
        if result.stdout:
            lines = result.stdout.strip().split('\n')
            for line in lines:
                if f':{port}' in line and 'LISTENING' in line:
                    parts = line.split()
                    if len(parts) > 4:
                        pid = parts[-1]
                        print(f"发现占用端口 {port} 的进程 PID: {pid}")
                        
                        # 询问是否终止进程
                        choice = input(f"是否终止进程 {pid}? (y/N): ").lower()
                        if choice == 'y':
                            subprocess.run(f'taskkill /F /PID {pid}', shell=True)
                            print(f"已终止进程 {pid}")
                            time.sleep(1)  # 等待进程完全终止
                            return True
        return False
    except Exception as e:
        print(f"检查端口进程时出错: {e}")
        return False

def start_server():
    """启动服务器"""
    # 获取脚本所在目录
    script_dir = Path(__file__).parent
    backend_dir = script_dir / 'backend'
    app_file = backend_dir / 'app.py'
    
    # 检查文件是否存在
    if not app_file.exists():
        print(f"错误: 找不到 {app_file}")
        print("请确保在项目根目录下运行此脚本")
        sys.exit(1)
    
    # 切换到backend目录
    os.chdir(backend_dir)
    
    print("=" * 50)
    print("DPO数据集生成工具 - 服务器启动器")
    print("=" * 50)
    
    # 查找可用端口
    host = '127.0.0.1'
    port = find_available_port(host)
    
    if port is None:
        print("错误: 找不到可用端口")
        print("尝试手动清理端口...")
        
        for p in range(5000, 5010):
            if not check_port(host, p):
                print(f"端口 {p} 被占用")
                if kill_process_on_port(p):
                    port = p
                    break
    
    if port is None:
        print("无法找到可用端口，请手动清理后重试")
        sys.exit(1)
    
    print(f"使用端口: {port}")
    print(f"服务器地址: http://{host}:{port}")
    
    # 更新前端配置中的API地址
    frontend_script = script_dir / 'frontend' / 'script.js'
    if frontend_script.exists() and port != 5000:
        print(f"提醒: 如果使用端口 {port}，请更新前端 script.js 中的 API_BASE_URL")
        print(f"将 'http://localhost:5000/api' 改为 'http://localhost:{port}/api'")
    
    print("\n启动服务器...")
    print("按 Ctrl+C 停止服务器")
    print("-" * 50)
    
    try:
        # 设置环境变量
        env = os.environ.copy()
        env['FLASK_APP'] = 'app.py'
        env['FLASK_ENV'] = 'development'
        
        # 启动Flask应用
        if port == 5000:
            # 使用默认端口直接运行
            subprocess.run([sys.executable, 'app.py'], env=env, check=True)
        else:
            # 使用自定义端口
            cmd = [
                sys.executable, '-c',
                f"""
import sys
sys.path.insert(0, '.')
from app import app
app.run(debug=True, host='{host}', port={port}, use_reloader=True, threaded=True)
"""
            ]
            subprocess.run(cmd, env=env, check=True)
            
    except KeyboardInterrupt:
        print("\n\n服务器已停止")
    except subprocess.CalledProcessError as e:
        print(f"启动服务器失败: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"发生未知错误: {e}")
        sys.exit(1)

if __name__ == '__main__':
    start_server()
