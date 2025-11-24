import re
from deep_translator import GoogleTranslator

def translate_to_chinese(text: str) -> str:
    """Translate English text to Chinese."""
    try:
        # Corrected language code for Simplified Chinese
        return GoogleTranslator(source='en', target='zh-CN').translate(text)
    except Exception as e:
        print(f"Translation error: {e}")
        return text  # fallback: return original

def convert_to_bilingual_srt(input_file: str, output_file: str):
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Debugging: print the raw content read from the file
    print("Raw content read from file:\n", content[:500])  # Show the first 500 characters

    # Updated regex pattern to handle multi-line subtitle texts with or without commas in timestamps
    pattern = r"(\d+)\s+([\d:.]+ --> [\d:.]+)\s+((?:[^\n]+(?:\n[^\n]+)*))"
    blocks = re.findall(pattern, content)

    # Debugging: Check what we extracted from the .srt file
    print(f"Extracted {len(blocks)} blocks")
    print(blocks[:2])  # Show first 2 blocks for debugging

    bilingual_output = []

    for index, timestamp, text in blocks:
        english_text = text.strip()
        chinese_text = translate_to_chinese(english_text)

        bilingual_block = f"""{index}
        {timestamp}
        {english_text}
        {chinese_text}
        """
        bilingual_output.append(bilingual_block)

    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(bilingual_output)

    print(f"✔ Bilingual subtitle saved to: {output_file}")


if __name__ == "__main__":
    input_srt = "subtitle_files/Welcome to Machine Learning!-en.srt"      # your input English subtitle file
    output_srt = "subtitle_files/Welcome to Machine Learning!-bilingual.srt" # output bilingual file
    convert_to_bilingual_srt(input_srt, output_srt)
