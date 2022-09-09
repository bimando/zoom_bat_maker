import os
import get_href

cwd_path = os.getcwd()
chrome_path_exe = f"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
links = []


def list_href():
    with open(f"{get_href.export_file_name}", "r") as file:
        global links
        links = [line.strip() for line in file]
    print(f"[+] Jumlah link : {len(links)}")


def generate_bat():
    x: int = 1
    y: int = 1
    num_item = int(input(">>> Masukkan jumlah link per file .bat: "))
    while len(links) != 0:
        for item in list(links[:num_item]):
            with open(f"{cwd_path}\\export\\bat{x}.bat", "a") as exportlink:
                exportlink.write(f"@ECHO OFF\n")
                exportlink.write(f"start \"Chrome\" \"{chrome_path_exe}\" \"{item}\""
                                 f" --profile-directory=\"Profile {y}\"\n")
                y += 1
            links.remove(item)
        x += 1
    print(f"[+] File tersimpan di folder {cwd_path}\\export\\")


if __name__ == '__main__':

    try:
        print(f"{get_href.export_file_name}")
        list_href()
        generate_bat()
    except OSError as e:
        print(e)
