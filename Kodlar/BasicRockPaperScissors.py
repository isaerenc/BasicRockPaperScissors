__author__ = "isaerenc"

import random

while True:

    choices = ["taş","kağıt","makas"]

    bilgisayar = random.choice(choices)
    player = None

    while player not in choices:
        player = input("taş, kağıt ya da makas seç birini.: ").lower()

    if player == bilgisayar:
        print("Akıllı sistem", bilgisayar, "seçti")
        print("Sen ise", player, "seçtin")
        print("Berabere kaldınız!")

    elif player == "taş":
        if bilgisayar == "kağıt":
            print("Akıllı sistem", bilgisayar, "seçti")
            print("Sen ise", player, "seçtin")
            print("Bilgisayar kazandı!")
        if bilgisayar == "makas":
            print("Akıllı sistem", bilgisayar, "seçti")
            print("Sen ise", player, "seçtin")
            print("Sen kazandın!")

    elif player == "kağıt":
        if bilgisayar == "makas":
            print("Akıllı sistem", bilgisayar, "seçti")
            print("Sen ise", player, "seçtin")
            print("Bilgisayar kazandı!")
        if bilgisayar == "taş":
            print("Akıllı sistem", bilgisayar, "seçti")
            print("Sen ise", player, "seçtin")
            print("Sen kazandın!")

    elif player == "makas":
        if bilgisayar == "taş":
            print("Akıllı sistem", bilgisayar, "seçti")
            print("Sen ise", player, "seçtin")
            print("Bilgisayar kazandı!")
        if bilgisayar == "kağıt":
            print("Akıllı sistem", bilgisayar, "seçti")
            print("Sen ise", player, "seçtin")
            print("Sen kazandın!")
