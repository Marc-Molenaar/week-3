def ledematen_tellen(mensen):
    aantal_hoofden = mensen
    aantal_schouders = mensen * 2
    aantal_knieen = mensen * 2
    aantal_tenen = mensen * 10

    print(f"Aantal hoofden: {aantal_hoofden}")
    print(f"Aantal schouders: {aantal_schouders}")
    print(f"Aantal knieen: {aantal_knieen}")
    print(f"Aantal tenen: {aantal_tenen}")


if __name__ == '__main__':
    ledematen_tellen(5)
