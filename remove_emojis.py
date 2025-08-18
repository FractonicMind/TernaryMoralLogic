import sys
import emoji
import os

def clean_file(filename):
    """Reads a file, removes all emojis, and overwrites the file."""
    try:
        # Read the original file content
        with open(filename, 'r', encoding='utf-8', errors='ignore') as f_read:
            content = f_read.read()

        # Remove emojis using the library
        cleaned_content = emoji.replace_emoji(content, replace='')

        # If changes were made, write them back to the file
        if content != cleaned_content:
            with open(filename, 'w', encoding='utf-8') as f_write:
                f_write.write(cleaned_content)
            print(f"Cleaned emojis from: {filename}")

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
