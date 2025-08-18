import sys
import os

def clean_file(filename):
    """
    Cleans a file using a hardcoded list of emoji characters and a highly
    efficient translation table. This avoids all regex and Unicode library
    inconsistencies.
    """
    try:
        # A definitive string containing every single emoji character found in the original file.
        EMOJI_CHARACTERS = (
            "\u2705"  # 
            "\u274C"  # 
            "\u27A1"  # 
            "\u2696"  # 
            "\u26A1"  # 
            "\u267F"  # 
            "\U0001F6E1"  # 
            "\U0001F4DE"  # 
            "\U0001F4DD"  # 
            "\U0001F454"  # 
            "\U0001F4B0"  # 
            "\U0001F4B8"  # 
            "\U0001F4CA"  # 
            "\U0001F6D1"  # 
            "\U0001F527"  # 
            "\U0001F510"  # 
            "\U0001F6A8"  # 
            "\U0001F504"  # 
            "\U0001F6AB"  # 
            "\U0001F494"  # 
            "\U0001F3E0"  # 
            "\U0001F697"  # 
            "\U0001F3EB"  # 
            "\U0001F3E5"  # 
            "\U0001F474"  # 
            "\U0001F476"  # 
            "\U0001F465"  # 
            "\U0001F30D"  # 
            "\U0001F4DA"  # 
            "\u26A0"      #  (base character)
            "\uFE0F"      # Invisible variation selector
        )

        with open(filename, 'r', encoding='utf-8') as f_read:
            content = f_read.read()

        # Use a translation table for the most efficient, direct character removal.
        translation_table = str.maketrans('', '', EMOJI_CHARACTERS)
        cleaned_content = content.translate(translation_table)

        if content != cleaned_content:
            with open(filename, 'w', encoding='utf-8') as f_write:
                f_write.write(cleaned_content)
            print(f" File has been definitively cleaned: {filename}")
        else:
            print(f"ℹ No targeted emojis found in: {filename}")

    except Exception as e:
        print(f"Error processing {filename}: {e}", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 final_cleaner.py <file1> <file2> ...", file=sys.stderr)
        sys.exit(1)

    for path in sys.argv[1:]:
        if os.path.isfile(path):
            clean_file(path)
