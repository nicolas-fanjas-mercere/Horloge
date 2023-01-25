import time
import threading

class Alarme:
    def __init__(self):
        self.alarme_active = False
        self.heure_alarme = (0, 0, 0)
        self.thread_alarme = None

    def definir_alarme(self, heure_alarme, minute_alarme, seconde_alarme):
        if 0 <= heure_alarme <= 23 and 0 <= minute_alarme <= 59 and 0 <= seconde_alarme <= 59:
            self.alarme_active = True
            self.heure_alarme = (heure_alarme, minute_alarme, seconde_alarme)
            self.thread_alarme = threading.Thread(target=self.check_alarme)
            self.thread_alarme.start()
        else:
            print("Entrez des valeurs valides pour l'heure et te RATE PAS sinon ADIOS les rdv, la minute et la seconde de l'alarme.")

    def arreter_alarme(self):
        self.alarme_active = False
        if self.thread_alarme:
            self.thread_alarme.join()

    def check_alarme(self):
        while self.alarme_active:
            heure_locale = time.localtime()
            if heure_locale.tm_hour == self.heure_alarme[0] and heure_locale.tm_min == self.heure_alarme[1] and heure_locale.tm_sec == self.heure_alarme[2]:
                print("Alarme ! REVEILLE TOI MEC !")
                self.alarme_active = False
            time.sleep(1)

alarme = Alarme()

def afficher_heure():
    while True:
        heure_locale = time.localtime()
        heure = heure_locale.tm_hour
        minute = heure_locale.tm_min
        seconde = heure_locale.tm_sec

        if heure < 10:
            heure = "0" + str(heure)
        else:
            heure = str(heure)

        if minute < 10:
            minute = "0" + str(minute)
        else:
            minute = str(minute)

        if seconde < 10:
            seconde = "0" + str(seconde)
        else:
            seconde = str(seconde)

        print(heure + ":" + minute + ":" + seconde)
        time.sleep(1)

thread_heure = threading.Thread(target=afficher_heure)
thread_heure.start()

while True:
    entree_utilisateur = input("Marque 'alarm' pour pouvoir en mettre une, 'stop' pour arrêter l'alarme ou 'quit' pour l'arreter: ")

    if entree_utilisateur == "alarm":
        alarme.definir_alarme(int(input("Entre l'heure (0-23) pour l'alarme: ")),
                              int(input("Entre la minute (0-59) pour l'alarme: ")),
                              int(input("Entre la seconde (0-59) pour l'alarme: ")))
    elif entree_utilisateur == "stop":
        alarme.arreter_alarme()
    elif entree_utilisateur == "quit":
        if alarme.thread_alarme:
            alarme.thread_alarme.join()
        thread_heure.join()
        break