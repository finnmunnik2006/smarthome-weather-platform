def lees_regels(inputFile):
    """Leest het invoerbestand en slaat de kolomnamen over."""
    with open(inputFile, "r") as f:
        regels = [r.strip() for r in f.readlines()]
    return [r for r in regels[1:] if r]


def aantal_dagen(inputFile):
    return len(lees_regels(inputFile))


def auto_bereken(inputFile, outputFile):
    regels = lees_regels(inputFile)
    with open(outputFile, "w") as f:
        for regel in regels:
            delen = regel.split()
            datum = delen[0]
            personen = int(delen[1])
            setpoint = float(delen[2])
            buiten = float(delen[3])
            neerslag = float(delen[4])

            verschil = setpoint - buiten
            if verschil >= 20:
                cv = 100
            elif verschil >= 10:
                cv = 50
            else:
                cv = 0

            ventilatie = min(personen + 1, 4)
            bewatering = neerslag < 3

            f.write(f"{datum};{cv};{ventilatie};{bewatering}\n")


def overwrite_settings(outputFile):
    datum = input("Welke datum wil je aanpassen (bijv. 08-10-2024)? ").strip()

    with open(outputFile, "r") as f:
        regels = [r.strip().split(";") for r in f.readlines() if r.strip()]

    gevonden = None
    for i, delen in enumerate(regels):
        if delen[0] == datum:
            gevonden = i
            break
    if gevonden is None:
        return -1

    systeem = input("Welk systeem? (1: CV ketel, 2: ventilatie, 3: bewatering) ").strip()
    if systeem not in ("1", "2", "3"):
        return -3

    waarde = input("Nieuwe waarde: ").strip()
    try:
        getal = int(waarde)
    except ValueError:
        return -3

    if systeem == "1" and 0 <= getal <= 100:
        regels[gevonden][1] = str(getal)
    elif systeem == "2" and 0 <= getal <= 4:
        regels[gevonden][2] = str(getal)
    elif systeem == "3" and getal in (0, 1):
        regels[gevonden][3] = "True" if getal == 1 else "False"
    else:
        return -3

    with open(outputFile, "w") as f:
        for delen in regels:
            f.write(";".join(delen) + "\n")
    return 0


def smart_app_controller():
    inputFile = "input.txt"
    outputFile = "output.txt"

    while True:
        print("\n=== Smart App Controller ===")
        print("1. Aantal dagen weergeven")
        print("2. Automatisch alle actuatoren berekenen en opslaan")
        print("3. Een waarde overschrijven")
        print("4. Stoppen")
        keuze = input("Maak een keuze (1-4): ").strip()

        if keuze == "1":
            print(f"Er zijn {aantal_dagen(inputFile)} dagen aanwezig.")
        elif keuze == "2":
            auto_bereken(inputFile, outputFile)
            print(f"Berekening gelukt, opgeslagen in {outputFile}.")
        elif keuze == "3":
            resultaat = overwrite_settings(outputFile)
            if resultaat == 0:
                print("De waarde is overschreven in het uitvoerbestand.")
            elif resultaat == -1:
                print("Fout: datum niet gevonden.")
            elif resultaat == -3:
                print("Fout: ongeldig systeem gekozen of ongeldige waarde ingevoerd.")
        elif keuze == "4":
            print("Tot ziens!")
            break
        else:
            print("Ongeldige keuze, kies 1, 2, 3 of 4.")


if __name__ == "__main__":
    smart_app_controller()