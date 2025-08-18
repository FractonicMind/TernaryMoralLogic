import sys
import regex # Using the 'regex' library for its superior Unicode handling
import os

def clean_file(filename):
    """
    Reads a file, removes all emojis using a comprehensive set of Unicode ranges,
    and overwrites the file. This method is highly compatible.
    """
    try:
        # This pattern explicitly lists the Unicode character ranges for emojis.
        # It does not rely on the environment's Unicode property support.
        emoji_pattern = regex.compile(
            "["
            "\U0001F1E0-\U0001F1FF"  # Flags
            "\U0001F300-\U0001F5FF"  # Symbols & Pictographs
            "\U0001F600-\U0001F64F"  # Emoticons
            "\U0001F680-\U0001F6FF"  # Transport & Map
            "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
            "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
            "\u2600-\u26FF"          # Miscellaneous Symbols
            "\u2700-\u27BF"          # Dingbats
            "\uFE0F"                # Variation Selector (for things like ⚖️)
            "]"
        )
        
        with open(filename, 'r', encoding='utf-8') as f_read:
            content = f_read.read()

        cleaned_content = emoji_pattern.sub('', content)

        if content != cleaned_content:
            with open(filename, 'w', encoding='utf-8') as f_write:
                f_write.write(cleaned_content)
            print(f"✅ Cleaned remaining emojis from: {filename}")
        else:
            print(f"ℹ️ No emojis found in: {filename}")

    except Exception as e:
        print(f"Error processing {filename}: {e}", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 remove_emojis.py <file1> <file2> ...", file=sys.stderr)
        sys.exit(1)

    for path in sys.argv[1:]:
        if os.path.isfile(path):
            clean_file(path)
