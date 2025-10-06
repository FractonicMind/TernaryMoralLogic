import sys
import regex
import os

def diagnose_file(filename):
    """
    Reads a file and prints the cleaned content to the terminal
    WITHOUT saving any changes to disk.
    """
    try:
        UNIVERSAL_EMOJI_PATTERN = regex.compile(
            "["
            "\U0001F1E0-\U0001F1FF"
            "\U0001F300-\U0001F5FF"
            "\U0001F600-\U0001F64F"
            "\U0001F680-\U0001F6FF"
            "\U0001F900-\U0001F9FF"
            "\U0001FA70-\U0001FAFF"
            "\u2600-\u27BF"
            "\uFE0F"
            "]+"
        )
        with open(filename, 'r', encoding='utf-8') as f_read:
            content = f_read.read()

        cleaned_content = UNIVERSAL_EMOJI_PATTERN.sub('', content)

        # Print the cleaned content directly to the terminal
        print("--- Diagnostic Output (Not Saved to File) ---")
        print(cleaned_content)

    except Exception as e:
        print(f"Error processing {filename}: {e}", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: python3 diagnostic_cleaner.py <file>")
    diagnose_file(sys.argv[1])
