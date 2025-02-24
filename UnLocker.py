import os
import platform

def get_vmware_preferences_file():
    system = platform.system()
    
    # 운영체제에 따라 경로를 설정
    if system == "Windows":
        vmware_preferences_file = os.path.join(os.getenv("APPDATA"), "VMware", "preferences")
    elif system == "Darwin":  # macOS
        vmware_preferences_file = os.path.expanduser("~/Library/Preferences/VMware/preferences")
    elif system == "Linux":
        vmware_preferences_file = os.path.expanduser("~/.vmware/preferences")
    else:
        raise Exception("지원되지 않는 운영체제입니다.")
    
    return vmware_preferences_file

# VMware UI 언어를 한글로 변경하는 함수
def set_language_to_korean():
    try:
        preferences_file = get_vmware_preferences_file()
        
        # 설정 파일이 존재하는지 확인
        if not os.path.exists(preferences_file):
            raise FileNotFoundError(f"{preferences_file} 파일을 찾을 수 없습니다.")

        with open(preferences_file, 'r') as file:
            preferences = file.readlines()

        language_found = False
        for idx, line in enumerate(preferences):
            if line.startswith("gui.language"):
                preferences[idx] = "gui.language = ko_KR\n"
                language_found = True
                break

        if not language_found:
            preferences.append("gui.language = ko_KR\n")

        with open(preferences_file, 'w') as file:
            file.writelines(preferences)

        print("VMware UI 언어를 한글로 변경했습니다.")
    except Exception as e:
        print(f"언어 설정 변경 중 오류가 발생했습니다: {e}")

# VMware UI 한글화 적용
set_language_to_korean()
