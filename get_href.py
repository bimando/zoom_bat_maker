import os
from bs4 import BeautifulSoup as bs

PATH = os.getcwd()

raw = str(input(f">>> Masukkan nama file (*file.txt): "))
export_dir = f"{PATH}\\export"
export_file_name = f"{PATH}\\export\\{raw}_exported.txt"


def get_href() -> str:
    filelink = open(f"{PATH}\\{raw}", "r", encoding="utf-8")
    soup = bs(filelink, 'html.parser')

    if os.path.exists(export_dir):
        os.rmdir(export_dir)

    os.mkdir(export_dir)

    with open(f"{export_file_name}", "a") as extract:
        for a in soup.find_all('a', href=True):
            # print(a['href'])
            extract.write(f"{a['href']} \n")
    return export_file_name


if __name__ == '__main__':

    try:
        print(os.path.exists(f"{PATH}\\export"))
    except OSError as e:
        print(f"{e}")
