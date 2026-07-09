import glob
import os

exclude_dirs = {'./proofs', './Research_Reports', './.git'}

def get_files():
    files = []
    for pattern in ['**/*.md', '**/*.html']:
        for f in glob.glob(f'./{pattern}', recursive=True):
            skip = any(f.startswith(ex) for ex in exclude_dirs)
            if not skip:
                files.append(f)
    return files

# All replacements to apply across all files
replacements = [
    # Old org emails -> governance portal
    ('- Technical Infrastructure Institution (open seat): info@eff.org', '- Contact via: https://governance.tml.org/seats/SC-1'),
    ('- Human Rights Institution (open seat): contactus@amnesty.org', '- Contact via: https://governance.tml.org/seats/SC-2'),
    ('- Earth Protection Institution (open seat): ien@ienearth.org', '- Contact via: https://governance.tml.org/seats/SC-3'),
    ('- AI Ethics Research Institution (open seat): info@media.mit.edu', '- Contact via: https://governance.tml.org/seats/SC-4'),
    ('- AI Ethics Research Institution (open seat): hai-info@stanford.edu', '- Alternative SC-4 contact: https://governance.tml.org/seats/SC-4'),
    ('- Medical Research Institution (open seat): publicaffairs@mskcc.org', '- Contact via: https://governance.tml.org/seats/SC-5'),

    # Old seat descriptions with "- 1 seat" suffix
    ('**Human Rights Partner** - 1 seat', '**Human Rights Enforcement Custodian (open seat -- SC-2)**'),
    ('**Earth Protection Partner** - 1 seat', '**Earth Protection Custodian (open seat -- SC-3)**'),
    ('**AI Ethics Research Partner** - 1 seat', '**AI Ethics Research Custodian (open seat -- SC-4)**'),
    ('**Memorial Fund Administrator** - 1 seat', '**Medical and Victim Compensation Custodian (open seat -- SC-5)**'),
    ('**Community Representative** (elected) - 1 seat', '**Community Representative (elected -- SC-9)**'),
    ('Human Rights Partner - 1 seat', 'Human Rights Enforcement Custodian (open seat -- SC-2)'),
    ('Earth Protection Partner - 1 seat', 'Earth Protection Custodian (open seat -- SC-3)'),
    ('AI Ethics Research Partner - 1 seat', 'AI Ethics Research Custodian (open seat -- SC-4)'),
    ('Memorial Fund Administrator - 1 seat', 'Medical and Victim Compensation Custodian (open seat -- SC-5)'),
    ('Community Representative (elected) - 1 seat', 'Community Representative (elected -- SC-9)'),

    # Double open seat patterns
    ('Technical Infrastructure Institution (open seat) (open seat)', 'Technical Infrastructure Custodian (open seat -- SC-1)'),
    ('open seat) (open seat)', 'open seat -- SC-1)'),

    # Remaining "open seat)" without SC number -- institution type patterns
    ('Human Rights Institution (open seat)', 'Human Rights Enforcement Custodian (open seat -- SC-2)'),
    ('Earth Protection Institution (open seat)', 'Earth Protection Custodian (open seat -- SC-3)'),
    ('AI Ethics Research Institution (open seat) / AI Ethics Research Institution (open seat)', 'AI Ethics Research Custodian (open seat -- SC-4)'),
    ('AI Ethics Research Institution (open seat)', 'AI Ethics Research Custodian (open seat -- SC-4)'),
    ('Medical Research Institution (open seat)', 'Medical and Victim Compensation Custodian (open seat -- SC-5)'),
    ('Technical Infrastructure Institution (open seat)', 'Technical Infrastructure Custodian (open seat -- SC-1)'),

    # Remaining "recommended Stewardship Custodians" phrases
    ('recommended Stewardship Custodians', 'Tri-Cameral Stewardship Custodians'),
    ('recommended for enhanced oversight through six institutional nodes', 'active -- see governance/Tri_Cameral_Constitution.md'),

    # Tagging notification
    ('Tagging priority custodian organizations for notification.', 'Notifying open seat holders per governance/SEAT_SELECTION.md'),

    # Community Representative Elected Position
    ('Community Representative (Elected Position)', 'Community Representative (elected -- SC-9)'),

    # Succession launch guide 6-seat council structure
    ('### Council Structure\nActivate the **TML Tri-Cameral Stewardship Custodians** (11 open seats):\n1. **Technical Infrastructure Custodian (open seat -- SC-1)**\n2. **Human Rights Enforcement Custodian (open seat -- SC-2)**\n3. **Earth Protection Custodian (open seat -- SC-3)**\n4. **AI Ethics Research Custodian (open seat -- SC-4)**\n5. **Medical and Victim Compensation Custodian (open seat -- SC-5)**\n6. **Community Representative (elected -- SC-9)**',
     '### Chamber Structure\nActivate the **TML Tri-Cameral Governance Architecture**:\n\n**Technical Council (9 seats, TC-1 through TC-9)** -- proposal rights only\n**Stewardship Custodians (11 seats, SC-1 through SC-11)** -- binding veto authority\n**Smart Contract Treasury** -- automatic execution, no admin key\n\nSeats filled per governance/SEAT_SELECTION.md'),
]

files = get_files()
total_fixed = 0

for fpath in files:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            original = f.read()
        content = original
        for old, new in replacements:
            content = content.replace(old, new)
        if content != original:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            total_fixed += 1
            print(f'Fixed: {fpath}')
    except Exception as e:
        print(f'Error {fpath}: {e}')

print(f'\nTotal files fixed: {total_fixed}')
