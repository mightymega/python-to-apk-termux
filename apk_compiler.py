import os
import subprocess

def create_buildozer_spec(script_name):
    spec_template = f"""
[app]
title = {script_name.split('.')[0]}
package.name = {script_name.split('.')[0].lower()}
package.domain = org.termux.pythonapp
source.dir = ./
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1
    """
    with open("buildozer.spec", "w") as spec_file:
        spec_file.write(spec_template)

def compile_apk(script_path):
    script_name = os.path.basename(script_path)
    os.makedirs("app", exist_ok=True)
    os.system(f"cp {script_path} app/main.py")
    os.chdir("app")
    
    # Generate buildozer.spec
    create_buildozer_spec(script_name)
    
    # Build APK
    try:
        subprocess.run(["buildozer", "android", "debug"], check=True)
    except subprocess.CalledProcessError:
        print("Error: APK build failed.")
    else:
        print("APK build complete. Check the bin/ directory for your APK.")
    finally:
        os.chdir("..")

if __name__ == "__main__":
    script_path = input("Enter the path to your Python script: ").strip()
    if os.path.isfile(script_path):
        compile_apk(script_path)
    else:
        print("Invalid file path. Please provide a valid Python script path.")
