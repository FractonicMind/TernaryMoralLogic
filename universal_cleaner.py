import sys
import regex # The 'regex' library is required for its superior Unicode support
import os

def clean_file(filename):
    """
    Cleans a file using a universal, comprehensive emoji regex pattern based on
    Unicode ranges. This is the most robust and portable method.
    """
    try:
        # A universal pattern that matches the vast majority of emojis and symbols.
        UNIVERSAL_EMOJI_PATTERN = regex.compile(
            "["
            "\U0001F1E0-\U0001F1FF"  # Flags
            "\U0001F300-\U0001F5FF"  # Symbols & Pictographs
            "\U0001F600-\U0001F64F"  # Emoticons
            "\U0001F680-\U0001F6FF"  # Transport & Map
            "\U0001F900-\U0001F9FF"  # Supplemental Symbols
            "\U0001FA70-\U0001FAFF"  # Symbols Extended
            "\u2600-\u27BF"          # Miscellaneous Symbols & Dingbats
            "\uFE0F"                # Variation Selector
            "]+"
        )
        
        with open(filename, 'r', encoding='utf-8') as f_read:
            content = f_read.read()

        # Remove all characters that match the universal emoji pattern
        cleaned_content = UNIVERSAL_EMOJI_PATTERN.sub('', content)

        if content != cleaned_content:
            with open(filename, 'w', encoding='utf-8') as f_write:
                f_write.write(cleaned_content)
            print(f"✅ Cleaned emojis from: {filename}")
        else:
            print(f"ℹ️ No emojis found in: {filename}")

    except Exception as e:
        print(f"Error processing {filename}: {e}", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 universal_cleaner.py <file1> <file2> ...", file=sys.stderr)
        sys.exit(1)

    for path in sys.argv[1:]:
        if os.path.isfile(path):
            clean_file(path)
