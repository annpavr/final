from googletrans import Translator
import asyncio

async def main():
    translator = Translator()

    print("Англійська - en, Українська - uk, Французька - fr, Німецька - de, Польська - pl, Іспанська - es")

    language1 = input("Мова з якої перекладати (введіть скорочений код): ").lower()
    language2 = input("На яку мову перекладати (введіть скорочений код): ").lower()
    text = input("Введіть текст: ")

    translated = await translator.translate(text, src=language1, dest=language2)
    print("Переклад:", translated.text)

asyncio.run(main())
