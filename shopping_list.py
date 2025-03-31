zakupy = {
    "Piekarnia": ["Chleb", "Pączek", "Bułki"],
    "Warzywniak": ["Marchew", "Seler", "Rukola"]
}
print("Lista zakupów:", zakupy)


for sklep, produkty in zakupy.items():
    sklep = sklep.capitalize()
    produkty_formatowane = [produkt.capitalize() for produkt in produkty]
    print(f"Idę do {sklep}, kupuję tu następujące rzeczy: {', '.join(produkty_formatowane)}")
