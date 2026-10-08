# coding: utf-8
import os
import shutil
import subprocess

import sys

if sys.platform == "win32":
    APP_DIR = os.path.join(os.getenv('LOCALAPPDATA', ''), 'Programs', 'antigravity')
    RESOURCES_DIR = os.path.join(APP_DIR, "resources")
elif sys.platform == "darwin":
    APP_DIR = "/Applications/Antigravity.app"
    RESOURCES_DIR = os.path.join(APP_DIR, "Contents", "Resources")
else:
    print("[错误] 当前仅支持 Windows 和 macOS 系统。")
    sys.exit(1)

ASAR_PATH = os.path.join(RESOURCES_DIR, "app.asar")
DISABLED_PATH = ASAR_PATH + ".disabled"
UNPACKED_APP_DIR = os.path.join(RESOURCES_DIR, "app")

def restore():
    print("==================================================================")
    print("                                                                ")
    print("             Antigravity v2.21.1 桌面端 纯净版还原工具              ")
    print("Github 开源项目地址：https://github.com/MIMICTE/Antigravity-zh-CN")
    print("                                                                ")
    print("==================================================================")
    print("                                                                   ")
    print("[执行] 正在为您关闭 Antigravity 程序...")
    if sys.platform == "win32":
        os.system("taskkill /F /IM Antigravity.exe >nul 2>&1")
    elif sys.platform == "darwin":
        os.system("pkill -f Antigravity >/dev/null 2>&1")

    if os.path.exists(DISABLED_PATH):
        print("[执行] 找到已禁用的原始语言包: app.asar.disabled")
        print("[执行] 正在恢复官方原版核心文件...")
        print("                                                                   ")
        
        if os.path.exists(ASAR_PATH):
            try:
                os.remove(ASAR_PATH)
            except Exception as e:
                print(f"[错误] 无法删除当前的 app.asar: {e}")
                return

        try:
            os.rename(DISABLED_PATH, ASAR_PATH)
            if os.path.exists(UNPACKED_APP_DIR):
                shutil.rmtree(UNPACKED_APP_DIR, ignore_errors=True)
            print("==================================================================")
            print("                                                                   ")
            print("  还原成功！正在为您自动启动纯净版 Antigravity...")
            print("                                                                   ")
            print("==================================================================")
            
            if sys.platform == "win32":
                exe_path = os.path.join(APP_DIR, "Antigravity.exe")
                if os.path.exists(exe_path):
                    DETACHED_PROCESS = 0x00000008
                    CREATE_NEW_PROCESS_GROUP = 0x00000200
                    subprocess.Popen(
                        [exe_path],
                        stdin=subprocess.DEVNULL,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                        creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP,
                        close_fds=True
                    )
            elif sys.platform == "darwin":
                subprocess.Popen(["open", APP_DIR])
        except Exception as e:
            print(f"[错误] 恢复文件时出错: {e}")
    else:
        if os.path.exists(UNPACKED_APP_DIR):
            print("[状态] 未发现已禁用的语言包 (app.asar.disabled)，但发现注入工作区。")
            print("[执行] 正在清理汉化注入残留文件...")
            shutil.rmtree(UNPACKED_APP_DIR, ignore_errors=True)
            print("==================================================================")
            print("  清理成功！软件当前已是原版状态。")
            print("==================================================================")
        else:
            print("[状态] 未发现已禁用的语言包 (app.asar.disabled)。")
            print("[状态] 软件当前已经是原版纯净状态。")
            print("                                                                   ")
            print("==================================================================")

if __name__ == "__main__":
    try:
        restore()
        input("\n执行完毕，按 Enter 键退出...")
    except KeyboardInterrupt:
        print("\n\n[提示] 用户取消操作。")
        input("\n按 Enter 键退出...")
    except Exception as e:
        print(f"\n[错误] 执行过程中出现异常: {e}")
        print("\n如果问题持续，请访问 GitHub 提交 Issue:")
        print("https://github.com/MIMICTE/Antigravity-zh-CN/issues")
        input("\n按 Enter 键退出...")
        raise
