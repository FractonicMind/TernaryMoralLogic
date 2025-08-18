import sys
import regex
import os

def clean_file(filename):
    """
    Cleans a file by removing emojis and reformatting specific markdown lines
    from '- **Text**:' to '- __Text__'.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f_read:
            content = f_read.read()

        original_content = content

        # A universal pattern that matches the vast majority of emojis and symbols.
        UNIVERSAL_EMOJI_PATTERN = regex.compile(
            "["
            "\U0001F1E0-\U0001F1FF" "\U0001F300-\U0001F5FF" "\U0001F600-\U0001F64F"
            "\U0001F680-\U0001F6FF" "\U0001F900-\U0001F9FF" "\U0001FA70-\U0001FAFF"
            "\u2600-\u27BF" "\uFE0F"
            "]+"
        )
        
        # This single, powerful regex finds the entire pattern and rebuilds it.
        # It looks for: a hyphen, spaces, **, an optional emoji, the text, **, and an optional colon.
        # It then replaces it with: a hyphen, spaces, __, the text, and __.
        content = regex.sub(
            r'(^\s*-\s+)\*\*(?:' + UNIVERSAL_EMOJI_PATTERN.pattern + r')?\s*(.*?)\s*\*\*:?',
            r'\1__\2__',
            content,
            flags=regex.MULTILINE
        )

        if original_content != content:
            with open(filename, 'w', encoding='utf-8') as f_write:
                f_write.write(content)
            print(f"✅ Cleaned and reformatted: {filename}")
        else:
            print(f"ℹ️ No matching lines found in: {filename}")

    except Exception as e:
        print(f"Error processing {filename}: {e}", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: python3 master_cleaner.py <file1> <file2> ...")
    for path in sys.argv[1:]:
        if os.path.isfile(path):
            clean_file(path)
