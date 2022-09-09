from get_href import get_href as getlink
from bat_maker import list_href as getlist
from bat_maker import generate_bat as genbat


if __name__ == "__main__":
    try:
        a = getlink()
        c = getlist()
        b = genbat()
    except OSError as e:
        print(f"{e}")
