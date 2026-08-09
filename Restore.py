# coding: utf-8
import os
import shutil
import platform

if platform.system() == 'Darwin':
    APP_DIR = '/Applications/Antigravity.app'
    RESOURCES_DIR = os.path.join(APP_DIR, 'Contents', 'Resources')
else:
    APP_DIR = os.path.join(os.environ.get('LOCALAPPDATA', ''), 'Programs', 'antigravity')
    RESOURCES_DIR = os.path.join(APP_DIR, "resources")

ASAR_PATH = os.path.join(RESOURCES_DIR, "app.asar")
DISABLED_PATH = ASAR_PATH + ".disabled"

def restore():
    print("=======================================================")
    print("          Antigravity v2.5.0 桌面端 纯净版还原工具")
    print("=======================================================")
    print("\n正在为您关闭 Antigravity 程序...")
    if platform.system() == 'Darwin':
        os.system("pkill -9 -f Antigravity >/dev/null 2>&1")
    else:
        os.system("taskkill /F /IM Antigravity.exe >nul 2>&1")

    if os.path.exists(DISABLED_PATH):
        print(f"\n[执行] 找到已禁用的原始语言包: app.asar.disabled")
        print("正在恢复...")
        
        if os.path.exists(ASAR_PATH):
            try:
                os.remove(ASAR_PATH)
            except Exception as e:
                print(f"[错误] 无法删除当前的 app.asar: {e}")
                return

        try:
            os.rename(DISABLED_PATH, ASAR_PATH)
            unpacked_dir = os.path.join(RESOURCES_DIR, "app")
            if os.path.exists(unpacked_dir):
                shutil.rmtree(unpacked_dir, ignore_errors=True)
            print("\n=======================================================")
            print("  还原成功！正在为您自动启动纯净版 Antigravity v2.5.0...")
            print("=======================================================")
            if platform.system() == 'Darwin':
                os.system(f"open '{APP_DIR}'")
            else:
                exe_path = os.path.join(APP_DIR, "Antigravity.exe")
                if os.path.exists(exe_path):
                    os.startfile(exe_path)
        except Exception as e:
            print(f"[错误] 恢复文件时出错: {e}")
    else:
        print("\n[状态] 未发现已禁用的语言包 (app.asar.disabled)。")
        print("或者软件当前已经是原版状态。")
        print("=======================================================")

if __name__ == "__main__":
    try:
        restore()
    except KeyboardInterrupt:
        print("\n\n[提示] 用户取消操作。")
    except Exception as e:
        print(f"\n[错误] 执行过程中出现异常: {e}")
        print("\n如果问题持续，请访问 GitHub 提交 Issue:")
        print("https://github.com/MIMICTE/Antigravity-zh-CN/issues")
        input("\n按任意键退出...")
        raise
