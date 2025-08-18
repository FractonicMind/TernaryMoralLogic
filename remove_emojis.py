import sys
import regex  # Using the powerful 'regex' library
import os

# This pattern specifically targets Unicode characters that are emoji/pictographs.
# It will NOT touch Markdown characters like #, *, or -.
EMOJI_PATTERN = regex.compile(r'\p{Extended_Pictographic}')

def clean_file(filename):
    """Reads a file, removes only emojis using a precise regex, and overwrites the file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f_read:
            content = f_read.read()

        # Replace only the characters matching our specific emoji pattern
        cleaned_content = EMOJI_PATTERN.sub('', content)

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
        print("Usage: python3 remove_emojis.py <file1> <file2> ...", file=sys.stderr)
        sys.exit(1)

    for path in sys.argv[1:]:
        if os.path.isfile(path):
            clean_file(path)
        else:
            print(f"Skipping (not a file): {path}", file=sys.stderr)
