meme_dict = {
    "КРИНЖ": "Что-то очень странное или стыдное",
    "ЛОЛ": "Что-то очень смешное",
    "РОФЛ": "Шутка",
    "ЩИЩ": "Одобрение или восторг",
    "КРИПОВЫЙ": "Страшный, пугающий",
    "АГРИТЬСЯ": "Злиться"
}
word = input("Введите непонятное слово (большими буквами!): ")
if word in meme_dict.keys():
    print(f"Значение слова' {word}': {meme_dict[word]}")
else:
    print("Слово не найдено в словаре.")