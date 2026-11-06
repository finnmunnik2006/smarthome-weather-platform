from weerstation import weerstation
3from controller import smart_app_controller
from api import huidige_temperatuur_utrecht


def toon_temperatuur():
    temp = huidige_temperatuur_utrecht()
    if temp is None:
        print("Kon de temperatuur niet ophalen (geen internet of API-fout).")
    else:
        print(f"De huidige temperatuur in Utrecht is {temp} graden Celsius.")


def main():
    while True:
        print("\n=== SMART APP ===")
        print("1. Weerstation")
        print("2. Smart App Controller")
        print("3. Huidige temperatuur in Utrecht")
        print("4. Stoppen")
        keuze = input("Maak een keuze (1-4): ").strip()

        if keuze == "1":
            weerstation()
        elif keuze == "2":
            smart_app_controller()
        elif keuze == "3":
            toon_temperatuur()
        elif keuze == "4":
            print("Tot ziens!")
            break
        else:
            print("Ongeldige keuze, kies 1, 2, 3 of 4.")


if __name__ == "__main__":
    main()