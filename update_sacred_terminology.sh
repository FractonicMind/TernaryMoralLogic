#!/bin/bash
# update_sacred_terminology.sh
# Updates Sacred Pause to either Sacred Zero or Always Memory based on context

echo "Creating backup..."
cp -r . ../TML_backup_$(date +%Y%m%d_%H%M%S)

# Function to preview changes
preview_changes() {
    echo "Preview of changes in $1:"
    grep -n "Sacred Pause" "$1" | head -5
    echo "---"
}

# Phase 1: Replace "Sacred Pause" → "Sacred Zero" for operational/trigger contexts
echo "Phase 1: Updating operational references to Sacred Zero..."

# Specific phrases that should become Sacred Zero
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
    "s/Sacred Pause generates/Sacred Zero generates/g"
    "s/Sacred Pause creates/Sacred Zero creates/g"
    "s/Sacred Pause records/Sacred Zero records/g"
    "s/Sacred Pause documentation/Sacred Zero documentation/g"
)

# Phase 2: Replace "Sacred Pause" → "Always Memory" for framework/principle contexts
echo "Phase 2: Updating framework references to Always Memory..."

declare -a ALWAYS_MEMORY_PATTERNS=(
    "s/Sacred Pause framework/Always Memory framework/g"
    "s/Sacred Pause technology/Always Memory technology/g"
    "s/Sacred Pause principle/Always Memory principle/g"
    "s/The Sacred Pause must/Always Memory must/g"
    "s/Sacred Pause must outlive/Always Memory must outlive/g"
    "s/Sacred Pause philosophy/Always Memory philosophy/g"
    "s/Sacred Pause between question and answer/Always Memory between action and execution/g"
    "s/Sacred Pause serves humanity/Always Memory serves humanity/g"
    "s/with Sacred Pause technology/with Always Memory technology/g"
)

# Files to process
ALL_FILES=$(find . -type f \( -name "*.md" -o -name "*.py" -o -name "*.yaml" -o -name "*.json" \) -not -path "./Research_Reports/*" -not -path "./.git/*")

# Apply replacements
for file in $ALL_FILES; do
    if [ -f "$file" ]; then
        # Skip certain protected files
        if [[ "$file" == *"CHANGELOG.md"* ]] || [[ "$file" == *"memorial_quotes.md"* ]]; then
            echo "Skipping protected file: $file"
            continue
        fi
        
        # Count occurrences
        count=$(grep -c "Sacred Pause" "$file" 2>/dev/null || echo "0")
        
        if [ "$count" -gt 0 ]; then
            echo "Processing $file ($count occurrences)..."
            
            # First apply Sacred Zero patterns
            for pattern in "${SACRED_ZERO_PATTERNS[@]}"; do
                sed -i "$pattern" "$file"
            done
            
            # Then apply Always Memory patterns
            for pattern in "${ALWAYS_MEMORY_PATTERNS[@]}"; do
                sed -i "$pattern" "$file"
            done
            
            # Handle lowercase versions
            sed -i 's/sacred pause triggers/sacred zero triggers/g' "$file"
            sed -i 's/sacred pause logging/sacred zero logging/g' "$file"
            sed -i 's/sacred pause principle/always memory principle/g' "$file"
            sed -i 's/sacred pause framework/always memory framework/g' "$file"
        fi
    fi
done

# Phase 3: Special handling for specific files
echo "Phase 3: Special case handling..."

# Files that need careful review
REVIEW_FILES=(
    "./protection/legacy-preservation.md"
    "./theory/philosophical-foundations.md"
    "./memorial/MEMORIAL_FUND.md"
)

echo ""
echo "Files requiring manual review (may contain historical references):"
for file in "${REVIEW_FILES[@]}"; do
    if [ -f "$file" ]; then
        remaining=$(grep -c "Sacred Pause" "$file" 2>/dev/null || echo "0")
        if [ "$remaining" -gt 0 ]; then
            echo "  - $file: $remaining remaining instances"
        fi
    fi
done

# Phase 4: Clean up any generic "Sacred Pause" that wasn't caught
echo ""
echo "Phase 4: Generic replacements for remaining instances..."

# For remaining generic "Sacred Pause" → "Sacred Zero" (default for unmatched)
for file in $ALL_FILES; do
    if [ -f "$file" ]; then
        # Skip protected files
        if [[ "$file" == *"CHANGELOG.md"* ]] || [[ "$file" == *"memorial_quotes.md"* ]]; then
            continue
        fi
        
        # Only process files still containing "Sacred Pause"
        if grep -q "Sacred Pause" "$file" 2>/dev/null; then
            echo "Generic cleanup in: $file"
            # Generic replacement - defaults to Sacred Zero for safety
            sed -i 's/Sacred Pause/Sacred Zero/g' "$file"
            sed -i 's/sacred pause/sacred zero/g' "$file"
            sed -i 's/SACRED PAUSE/SACRED ZERO/g' "$file"
        fi
    fi
done

# Final report
echo ""
echo "========================================="
echo "Update complete! Summary:"
echo "========================================="

# Count remaining instances
total_remaining=0
for file in $ALL_FILES; do
    if [ -f "$file" ]; then
        count=$(grep -c "Sacred Pause" "$file" 2>/dev/null || echo "0")
        if [ "$count" -gt 0 ]; then
            echo "Remaining in $file: $count"
            total_remaining=$((total_remaining + count))
        fi
    fi
done

echo ""
echo "Total remaining 'Sacred Pause' instances: $total_remaining"
echo "Backup created in: ../TML_backup_$(date +%Y%m%d_%H%M%S)"
echo ""
echo "Please manually review files in the REVIEW_FILES list for historical context."
