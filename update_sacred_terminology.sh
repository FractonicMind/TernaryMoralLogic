#!/bin/bash
# update_sacred_terminology.sh

echo "Creating backup..."
cp -r . ../TML_backup_$(date +%Y%m%d_%H%M%S)

declare -a SACRED_ZERO_PATTERNS=(
    "s/Sacred Pause triggers/Sacred Zero triggers/g"
    "s/Sacred Pause activation/Sacred Zero activation/g"
    "s/Sacred Pause logging/Sacred Zero logging/g"
    "s/Sacred Pause events/Sacred Zero events/g"
    "s/Sacred Pause threshold/Sacred Zero threshold/g"
    "s/Sacred Pause detection/Sacred Zero detection/g"
    "s/Sacred Pause Protocol/Sacred Zero Protocol/g"
    "s/Sacred Pause consultation/Sacred Zero consultation/g"
    "s/Sacred Pause for complex moral/Sacred Zero for complex moral/g"
)

declare -a ALWAYS_MEMORY_PATTERNS=(
    "s/Sacred Pause framework/Always Memory framework/g"
    "s/Sacred Pause technology/Always Memory technology/g"
    "s/Sacred Pause principle/Always Memory principle/g"
    "s/The Sacred Pause must/Always Memory must/g"
    "s/Sacred Pause philosophy/Always Memory philosophy/g"
)

ALL_FILES=$(find . -type f \( -name "*.md" -o -name "*.py" -o -name "*.yaml" -o -name "*.json" \) -not -path "./Research_Reports/*" -not -path "./.git/*")

for file in $ALL_FILES; do
    if [ -f "$file" ]; then
        count=$(grep -c "Sacred Pause" "$file" 2>/dev/null || echo "0")
        if [ "$count" -gt 0 ]; then
            echo "Processing $file ($count occurrences)..."
            for pattern in "${SACRED_ZERO_PATTERNS[@]}"; do
                sed -i "$pattern" "$file"
            done
            for pattern in "${ALWAYS_MEMORY_PATTERNS[@]}"; do
                sed -i "$pattern" "$file"
            done
            sed -i 's/Sacred Pause/Sacred Zero/g' "$file"
            sed -i 's/sacred pause/sacred zero/g' "$file"
        fi
    fi
done

echo "Complete! Checking remaining instances..."
grep -r "Sacred Pause" --include="*.md" --include="*.py" . | wc -l
