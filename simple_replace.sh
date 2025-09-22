#!/bin/bash
echo "Starting replacements..."

# Count before
echo "Sacred Pause instances before: $(grep -r "Sacred Pause" --include="*.md" . | wc -l)"

# Simple direct replacements
find . -name "*.md" -type f | while read file; do
    if grep -q "Sacred Pause" "$file"; then
        echo "Updating: $file"
        # Create temp file
        sed 's/Sacred Pause triggers/Sacred Zero triggers/g; s/Sacred Pause logging/Sacred Zero logging/g; s/Sacred Pause activation/Sacred Zero activation/g; s/Sacred Pause framework/Always Memory framework/g; s/Sacred Pause principle/Always Memory principle/g; s/Sacred Pause/Sacred Zero/g' "$file" > "$file.tmp"
        mv "$file.tmp" "$file"
    fi
done

# Count after  
echo "Sacred Pause instances after: $(grep -r "Sacred Pause" --include="*.md" . | wc -l)"
echo "Done!"
