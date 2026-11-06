def fahrenheit(temp_celcius):
    return 32 + 1.8 * temp_celcius


def gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid):
    return temp_celcius - luchtvochtigheid / 100 * windsnelheid


def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    gevoel = gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid)

    if gevoel < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"
    elif gevoel < 0 and windsnelheid <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
    elif 0 <= gevoel < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"
    elif 0 <= gevoel < 10 and windsnelheid <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
    elif 10 <= gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm."
    else:
        return "Warm! Airco aan!"


def vraag_getal(vraag, minimum=None, maximum=None, geheel=False):
    """Vraagt net zo lang om invoer tot die geldig is.
    Geeft None terug bij lege invoer (= stoppen)."""
    while True:
        invoer = input(vraag).strip()
        if invoer == "":
            return None
        try:
            waarde = int(invoer) if geheel else float(invoer.replace(",", "."))
        except ValueError:
            print("Ongeldige invoer, voer een getal in.")
            continue
        if minimum is not None and waarde < minimum:
            print(f"De waarde moet minimaal {minimum} zijn.")
            continue
        if maximum is not None and waarde > maximum:
            print(f"De waarde mag maximaal {maximum} zijn.")
            continue
        return waarde


def weerstation():
    totaal = 0
    for dag in range(1, 8):
        temp = vraag_getal(f"Wat is op dag {dag} de temperatuur[C]: ")
        if temp is None:
            print("Lege invoer ontvangen, het weerstation wordt afgesloten.")
            return

        wind = vraag_getal(f"Wat is op dag {dag} de windsnelheid[m/s]: ", minimum=0)
        if wind is None:
            print("Lege invoer ontvangen, het weerstation wordt afgesloten.")
            return

        vocht = vraag_getal(f"Wat is op dag {dag} de vochtigheid[%]: ",
                            minimum=0, maximum=100, geheel=True)
        if vocht is None:
            print("Lege invoer ontvangen, het weerstation wordt afgesloten.")
            return

        totaal += temp
        gemiddelde = totaal / dag

        print(f"Het is {temp:.1f}C ({fahrenheit(temp):.1f}F)")
        print(weerrapport(temp, wind, vocht))
        print(f"Gem. temp tot nu toe is {gemiddelde:.1f}")
        print("=" * 38)


if __name__ == "__main__":
    weerstation()