import hashlib
def ternary_hash(nodes):
    new_level = []
    for i in range(0, len(nodes), 3):
        group = nodes[i:i+3]
        combined = "".join(group).encode('utf-8')
        new_level.append(hashlib.sha256(combined).hexdigest())
    return ternary_hash(new_level) if len(new_level) > 1 else new_level[0]

with open("manifest.sha256", "r") as f:
    leaves = [line.split()[0] for line in f.readlines()]
root = ternary_hash(leaves)
print(f"Master Root Verified: {root}")
with open("master_root.txt", "w") as f: f.write(root)
