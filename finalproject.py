import googletrans as gt

translator = gt.Translator()

print("Англійська - en, Українська - uk, Французька - fr, Німецька - de, Польська - pl, Іспанька - es")

language1 = input("Мова з якої перекладати(введіть скорочений код): ").lower()
language2 = input("На яку мову перекладати(введіть скорочений код): ").lower()
text = input("Введіть текст: ")
translated = translator.translate(text, src=language1, dest=language2)

print("Переклад :", translated.text)
