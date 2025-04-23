# Vraag gegevens aan de gebruiker
naam = input("Wat is je naam? ")
leeftijd = input("Hoe oud ben je? ")
hobby = input("Wat is je hobby? ")
favoriete_kleur = input("Wat is je favoriete kleur? ")
favoriete_dier = input("Wat is je favoriete dier? ")

# Bereken leeftijd over 10 jaar (eerst omzetten naar een getal)
leeftijd_over_10 = int(leeftijd) + 10

# Print een profiel met f-strings
print("\n🔍 Gebruikersprofiel")
print("---------------------")
print(f"Naam: {naam}")
print(f"Leeftijd: {leeftijd}")
print(f"Hobby: {hobby}")
print(f"Favoriete kleur: {favoriete_kleur}")
print(f"Favoriete dier: {favoriete_dier}")
print(f"Over 10 jaar ben je {leeftijd_over_10} jaar oud!")
