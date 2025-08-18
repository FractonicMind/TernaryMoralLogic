import sys
import regex
import os

def clean_file(filename):
    """
    A verbose, self-contained script to clean emojis and provide step-by-step
    feedback. It reads the file, cleans it, and writes it back internally.
    """
    print(f"--- Starting process for: {filename} ---")

    if not os.path.isfile(filename):
        print(f"❌ ERROR: File not found at '{filename}'. Please check the path.")
        return

    try:
        # Step 1: Read the original file content
        with open(filename, 'r', encoding='utf-8') as f_read:
            content = f_read.read()
        print(f"✅ Step 1: Successfully read {len(content)} characters from the file.")

        if not content.strip():
            print("❌ ERROR: File is empty or contains only whitespace. Aborting.")
            return

        # Step 2: Clean the content using the universal emoji pattern
        UNIVERSAL_EMOJI_PATTERN = regex.compile(
            "["
            "\U0001F1E0-\U0001F1FF" "\U0001F300-\U0001F5FF" "\U0001F600-\U0001F64F"
            "\U0001F680-\U0001F6FF" "\U0001F900-\U0001F9FF" "\U0001FA70-\U0001FAFF"
            "\u2600-\u27BF" "\uFE0F"
            "]+"
        )
        cleaned_content = UNIVERSAL_EMOJI_PATTERN.sub('', content)
        print(f"✅ Step 2: Cleaned content down to {len(cleaned_content)} characters.")

        if not cleaned_content.strip():
            print("❌ ERROR: Cleaned content is empty. This should not happen. Aborting.")
            return

        # Step 3: Write the cleaned content back to the file
        with open(filename, 'w', encoding='utf-8') as f_write:
            f_write.write(cleaned_content)
        print(f"✅ Step 3: Successfully wrote cleaned content back to the file.")
        print("--- Process Complete ---")

    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: python3 bulletproof_cleaner.py <file>")
    clean_file(sys.argv[1])
