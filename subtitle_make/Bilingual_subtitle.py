import re
from deep_translator import GoogleTranslator

def translate_to_chinese(text: str) -> str:
    """Translate English text to Chinese."""
    try:
        return GoogleTranslator(source='en', target='zh-cn').translate(text)
    except Exception:
        return text  # fallback: return original


def convert_to_bilingual_srt(input_file: str, output_file: str):
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # SRT block regex
    pattern = r"(\d+)\s+([\d:,]+ --> [\d:,]+)\s+([\s\S]*?)(?=\n\n|\Z)"
    blocks = re.findall(pattern, content)

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
    input_srt = "input.srt"      # your input English subtitle file
    output_srt = "bilingual.srt" # output bilingual file
    convert_to_bilingual_srt(input_srt, output_srt)
