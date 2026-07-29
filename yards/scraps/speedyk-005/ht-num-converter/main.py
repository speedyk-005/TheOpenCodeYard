"""Haitian Creole number-to-text converter."""

text_to_num_map = {
    "milya": 1_000_000_000,
    "milyon": 1_000_000,
    "mil": 1000,
    "sen": 100,
    "katreven diz nèf": 99,
    "katreven diz uit": 98,
    "katreven diz sèt": 97,
    "katreven sèz": 96,
    "katreven kinz": 95,
    "katreven katòz": 94,
    "katreven trèz": 93,
    "katreven douz": 92,
    "katreven onz": 91,
    "katreven dis": 90,
    "katreven": 80,
    "swasant dis": 70,
    "swasant": 60,
    "senkant": 50,
    "karant": 40,
    "trent": 30,
    "ven": 20,
    "diz nèf": 19,
    "diz uit": 18,
    "diz sèt": 17,
    "sèz": 16,
    "kinz": 15,
    "katòz": 14,
    "trez": 13,
    "douz": 12,
    "onz": 11,
    "dis": 10,
    "nèf": 9,
    "uit": 8,
    "set": 7,
    "sis": 6,
    "senk": 5,
    "kat": 4,
    "twa": 3,
    "de": 2,
    "en": 1,
}

num_pad = {
    2: "de",
    3: "twa",
    4: "kat",
    5: "senk",
    6: "sis",
    7: "set",
    8: "uit",
    9: "nèf",
}


def num_to_text(number):
    "convert any num to ht text"
    if number == 0:
        return "zewo"
    result = []
    for text, num in text_to_num_map.items():
        q, number = divmod(number, num)
        match q:
            case 0:
                pass
            case 1:
                result.append(text)
            case n if 1 < n < 10:
                result.append(f"{num_pad[q]} {text}")
    return " ".join(result)


if __name__ == "__main__":
    print("Konvèsyon chif/nomb an lèt")
    while (inp := input("chif/nomb: ")) != "fen":
        try:
            print(num_to_text(int(inp)), "\n")
        except ValueError:
            print("Ekri yon chif oubyen nomb pito")