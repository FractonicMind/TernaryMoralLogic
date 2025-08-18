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
       # The only change is adding the '+' on the last line of the pattern
          emoji_pattern = regex.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # Flags
    # ... other lines ...
    "\uFE0F"                # Variation Selector (for things like )
    "]+" # <--- ADD THIS PLUS SIGN
)
        
        with open(filename, 'r', encoding='utf-8') as f_read:
            content = f_read.read()

        cleaned_content = emoji_pattern.sub('', content)

        if content != cleaned_content:
            with open(filename, 'w', encoding='utf-8') as f_write:
                f_write.write(cleaned_content)
            print(f" Cleaned remaining emojis from: {filename}")
        else:
            print(f"ℹ No emojis found in: {filename}")

    except Exception as e:
        print(f"Error processing {filename}: {e}", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 remove_emojis.py <file1> <file2> ...", file=sys.stderr)
        sys.exit(1)

    for path in sys.argv[1:]:
        if os.path.isfile(path):
            clean_file(path)
