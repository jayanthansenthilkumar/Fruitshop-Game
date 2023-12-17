import random
fruitbag = ["Apple","Orange","Banana","Pear","Grapes","Strawberry","Blueberry","Watermelon","Pineapple","Mango","Peach","Cherry","Kiwi",
    "Lemon","Lime","Plum","Raspberry","Blackberry","Cantaloupe","Fig","Grapefruit","Pomegranate","Apricot","Nectarine","Papaya","Coconut",
    "Passion Fruit","Guava","Lychee","Persimmon","Dragon Fruit","Avocado","Tangerine","Cranberry","Date","Kumquat","Star Fruit","Honeydew Melon",
    "Jackfruit","Mangosteen","Quince","Ugli Fruit","Soursop","Tamarind","Plantain","Feijoa","Bilberry","Salak","Ackee","Barbados Cherry","Longan",
    "Kiwano (Horned Melon)","Rambutan","Sapodilla","Breadfruit","Cherimoya","Durian","Jujube","Mulberry","Pawpaw","Prickly Pear","Feijoa",
    "Surinam Cherry","Sweetsop","Tamarillo","Yangmei (Yumberry)"]
print("Guess the fruits in the bag of fruits :")
print("\n",fruitbag)
shopkeeper = random.choice(fruitbag)
#print("\nShopkeepers Selection =",shopkeeper)
print("\nLet's move on to the game")
while True:
    player=input("\nEnter the fruitname :")
    if player not in fruitbag:
        Print("\nThere is no fruit like this")
    if player == shopkeeper:
        print("\nYou Won this game")
        print("Your Selection =",shopkeeper)
        print("\nDo you want to continue the game again ???[Yes(y/Y),No(n/N)]")
        play_again = input("Please Select anyone :")
        if play_again == "y" or "Y":
            shopkeeper = random.choice(fruitbag)
            #print("\nShopkeepers Selection =",shopkeeper)
        elif play_again == "n" or "N":
            print("\nThank you for your participation in this game")
            print("You are welcome again...")
            break
    else:
        print("\nYou lost the winning chance")
        print("Try again to Win this game")
    shopkeeper = random.choice(fruitbag)
