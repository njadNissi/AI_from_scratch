"""
    Create a dictionary program for french and english
    ---------------------------------------------------
                English-French Dictionayr
    ---------------------------------------------------
        type word:
        Result
        ======
        french: xyz
        g.c.: 

   -----------------------------------------------------
    type work: 
"""

english_french_dict = {
    "hello": ["bonjour", "interjection"],
    "goodbye": ["au revoir", "interjection"],
    "thank you": ["merci", "interjection"],
    "please": ["s'il vous plaît", "adverb"],
    "yes": ["oui", "adverb"],
    "no": ["non", "adverb"],
    "one": ["un/une", "numeral"],
    "two": ["deux", "numeral"],
    "three": ["trois", "numeral"],
    "four": ["quatre", "numeral"],
    "five": ["cinq", "numeral"],
    "six": ["six", "numeral"],
    "seven": ["sept", "numeral"],
    "eight": ["huit", "numeral"],
    "nine": ["neuf", "numeral"],
    "ten": ["dix", "numeral"],
    "person": ["personne", "noun"],
    "man": ["homme", "noun"],
    "woman": ["femme", "noun"],
    "child": ["enfant", "noun"],
    "family": ["famille", "noun"],
    "friend": ["ami/amie", "noun"],
    "mother": ["mère", "noun"],
    "father": ["père", "noun"],
    "brother": ["frère", "noun"],
    "sister": ["sœur", "noun"],
    "cat": ["chat", "noun"],
    "dog": ["chien", "noun"],
    "house": ["maison", "noun"],
    "car": ["voiture", "noun"],
    "book": ["livre", "noun"],
    "pen": ["stylo", "noun"],
    "computer": ["ordinateur", "noun"],
    "phone": ["téléphone", "noun"],
    "time": ["temps", "noun"],
    "day": ["jour", "noun"],
    "night": ["nuit", "noun"],
    "week": ["semaine", "noun"],
    "month": ["mois", "noun"],
    "year": ["année", "noun"],
    "today": ["aujourd'hui", "adverb"],
    "tomorrow": ["demain", "adverb"],
    "yesterday": ["hier", "adverb"],
    "here": ["ici", "adverb"],
    "there": ["là", "adverb"],
    "where": ["où", "pronoun"],
    "what": ["quoi", "pronoun"],
    "who": ["qui", "pronoun"],
    "how": ["comment", "adverb"],
    "why": ["pourquoi", "adverb"],
    "this": ["ceci", "demonstrative"],
    "that": ["cela", "demonstrative"],
    "my": ["mon/ma/mes", "adjective"],
    "your": ["ton/ta/tes", "adjective"],
    "his": ["son/sa/ses", "adjective"],
    "her": ["son/sa/ses", "adjective"],
    "our": ["notre/nos", "adjective"],
    "their": ["leur/leurs", "adjective"],
    "big": ["grand/grande", "adjective"],
    "small": ["petit/petite", "adjective"],
    "good": ["bon/bonne", "adjective"],
    "bad": ["mauvais/mauvaise", "adjective"],
    "happy": ["heureux/heureuse", "adjective"],
    "sad": ["triste", "adjective"],
    "fast": ["rapide", "adjective"],
    "slow": ["lent/lente", "adjective"],
    "new": ["nouveau/nouvelle", "adjective"],
    "old": ["vieux/vieille", "adjective"],
    "red": ["rouge", "adjective"],
    "blue": ["bleu/bleue", "adjective"],
    "green": ["vert/verte", "adjective"],
    "yellow": ["jaune", "adjective"],
    "to eat": ["manger", "verb"],
    "to drink": ["boire", "verb"],
    "to sleep": ["dormir", "verb"],
    "to wake": ["se réveiller", "verb"],
    "to work": ["travailler", "verb"],
    "to play": ["jouer", "verb"],
    "to read": ["lire", "verb"],
    "to write": ["écrire", "verb"],
    "to speak": ["parler", "verb"],
    "to listen": ["écouter", "verb"],
    "to see": ["voir", "verb"],
    "to hear": ["entendre", "verb"],
    "to walk": ["marcher", "verb"],
    "to run": ["courir", "verb"],
    "to come": ["venir", "verb"],
    "to go": ["aller", "verb"],
    "to have": ["avoir", "verb"],
    "to be": ["être", "verb"],
    "to do": ["faire", "verb"],
    "to make": ["faire", "verb"],
    "to take": ["prendre", "verb"],
    "to give": ["donner", "verb"],
    "to get": ["obtenir", "verb"],
    "to know": ["savoir/connaître", "verb"],
    "to learn": ["apprendre", "verb"],
    "to teach": ["enseigner", "verb"],
    "and": ["et", "conjunction"],
    "or": ["ou", "conjunction"],
    "but": ["mais", "conjunction"],
    "because": ["parce que", "conjunction"],
    "with": ["avec", "preposition"],
    "without": ["sans", "preposition"],
    "in": ["dans", "preposition"],
    "on": ["sur", "preposition"],
    "under": ["sous", "preposition"],
    "above": ["au-dessus", "preposition"],
    "below": ["au-dessous", "preposition"],
    "between": ["entre", "preposition"],
    "through": ["à travers", "preposition"],
    "quickly": ["rapidement", "adverb"],
    "slowly": ["lentement", "adverb"],
    "well": ["bien", "adverb"],
    "badly": ["mal", "adverb"],
    "very": ["très", "adverb"]
}


print("="*30)
print("|| English-French Dictionary||")
print("="*30)
while True:
    word = input("English world: ")
    if word in english_french_dict.keys():
        french, gram_class = english_french_dict.get(word)
        print(f"French: {french}\ngramatical class.: {gram_class}")
        print("-+-"*15)
    else:
        print(f"Sorry, '{word}' has not been found!")
