dictionary = {
    "ъуъ": "современный синоним к 'ух'",
    "трэш": "что-то, что вызывает чувство испанского стыда",
    "шо": "Разговорный вариант вопросительного слова", 
}
while True:
    question = input("Какое слово вас интересует?")
    if not question: 
        break
    question = question.lower()
    if question in dictionary:
        print(dictionary[question])
    else:
        print("Ошибка: Слова нет в словаре")
        
        
        
    #Альтернативное решение    
    print(dictionary.get(question, "Ошибка: Слова нет в словаре"))
