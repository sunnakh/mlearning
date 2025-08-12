import os
import json
from deep_translator import GoogleTranslator  # ✅ Correct import

JSON_FILE = "translations.json"


def translate_to_uzbek(text):
    """Translate English text to Uzbek using Google Translate."""
    try:
        return GoogleTranslator(source="en", target="uz").translate(text)
    except Exception as e:
        return f"❌ Error: {str(e)}"


def load_translations():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []


def save_translation(word, translation):
    data = load_translations()
    data.append({"word": word, "translation": translation})
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def main():
    print("🔤 English ➝ Uzbek CLI Translator (Powered by Google Translate)")
    print("Type 'exit' to quit.\n")

    while True:
        text = input("Enter an English sentence: ").strip()
        if text.lower() == "exit":
            print(f"✅ Translations saved to '{JSON_FILE}'")
            break

        uzbek = translate_to_uzbek(text)
        print("🔄 Uzbek:", uzbek)

        save_translation(text, uzbek)
        print("💾 Saved.")
        print("-" * 40)


if __name__ == "__main__":
    main()
