#!/usr/bin/env python3
"""
DPO数据集生成工具 - 安装和环境检查脚本
"""

import sys
import os
import subprocess
import importlib
from pathlib import Path

def check_python_version():
    """检查Python版本"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ 错误: 需要 Python 3.7 或更高版本")
        print(f"当前版本: Python {version.major}.{version.minor}.{version.micro}")
        print("请升级Python后重试")
        return False
    else:
        print(f"✅ Python版本检查通过: {version.major}.{version.minor}.{version.micro}")
        return True

def check_package(package_name, import_name=None):
    """检查Python包是否已安装"""
    if import_name is None:
        import_name = package_name
    
    try:
        importlib.import_module(import_name)
        print(f"✅ {package_name} 已安装")
        return True
    except ImportError:
        print(f"❌ {package_name} 未安装")
        return False

def install_requirements():
    """安装依赖包"""
    requirements_file = Path(__file__).parent / 'requirements.txt'
    
    if not requirements_file.exists():
        print("❌ 错误: 找不到 requirements.txt 文件")
        return False
    
    print("📦 正在安装依赖包...")
    try:
        subprocess.run([
            sys.executable, '-m', 'pip', 'install', '-r', str(requirements_file)
        ], check=True)
        print("✅ 依赖包安装完成")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ 安装依赖包失败: {e}")
        return False

def check_files():
    """检查必要文件"""
    base_dir = Path(__file__).parent
    required_files = [
        'backend/app.py',
        'backend/simple_dpo_utils.py',
        'frontend/index.html',
        'frontend/script.js',
        'frontend/style.css',
        'requirements.txt'
    ]
    
    print("📁 检查项目文件...")
    all_exist = True
    for file_path in required_files:
        full_path = base_dir / file_path
        if full_path.exists():
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} 缺失")
            all_exist = False
    
    return all_exist

def main():
    """主函数"""
    print("=" * 60)
    print("🚀 DPO数据集生成工具 - 环境检查和安装")
    print("=" * 60)
    
    # 检查Python版本
    if not check_python_version():
        sys.exit(1)
    
    print()
    
    # 检查文件
    if not check_files():
        print("❌ 项目文件不完整，请重新下载项目")
        sys.exit(1)
    
    print()
    
    # 检查依赖包
    print("📦 检查依赖包...")
    packages_to_check = [
        ('Flask', 'flask'),
        ('flask-cors', 'flask_cors'),
        ('requests', 'requests')
    ]
    
    missing_packages = []
    for package_name, import_name in packages_to_check:
        if not check_package(package_name, import_name):
            missing_packages.append(package_name)
    
    if missing_packages:
        print(f"\n缺少 {len(missing_packages)} 个依赖包")
        choice = input("是否自动安装? (Y/n): ").strip().lower()
        
        if choice in ['', 'y', 'yes']:
            if not install_requirements():
                print("❌ 安装失败，请手动运行: pip install -r requirements.txt")
                sys.exit(1)
        else:
            print("请手动安装依赖包: pip install -r requirements.txt")
            sys.exit(1)
    
    print()
    print("🎉 环境检查完成！所有依赖都已就绪")
    print()
    print("📋 接下来的步骤:")
    print("1. 运行 'python start_server.py' 启动后端服务")
    print("2. 在浏览器中打开前端页面 (frontend/index.html)")
    print("3. 配置您的大模型API信息")
    print("4. 开始生成DPO数据集！")
    print()
    print("📚 详细使用说明请查看 README.md")
    print("🐛 遇到问题请访问: https://github.com/KelvinJiang2333/dpo-dataset-generator/issues")

if __name__ == '__main__':
    main()
