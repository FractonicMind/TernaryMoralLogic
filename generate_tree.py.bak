import os
import html

def generate_html_tree(startpath):
    output = ['''
    <html>
    <head>
        <style>
            body { font-family: monospace; }
            ul { list-style-type: none; }
            li { margin: 2px 0; }
        </style>
    </head>
    <body>
    <h2>TernaryMoralLogic Repository Structure</h2>
    <ul>
    ''']
    
    exclude_dirs = {'.git', '__pycache__', '.pytest_cache', 'node_modules'}
    exclude_files = {'.DS_Store', '*.pyc', '.gitignore'}
    
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        level = root.replace(startpath, '').count(os.sep)
        indent = '  ' * (level + 1)
        
        if level < 3:  # Limit depth
            folder_name = os.path.basename(root)
            if folder_name:
                output.append(f'{indent}<li>📁 <b>{html.escape(folder_name)}/</b>')
                output.append(f'{indent}  <ul>')
            
            for file in sorted(files):
                if not file.startswith('.') and not file.endswith('.pyc'):
                    output.append(f'{indent}    <li>📄 {html.escape(file)}</li>')
            
            if folder_name:
                output.append(f'{indent}  </ul>')
                output.append(f'{indent}</li>')
    
    output.append('</ul></body></html>')
    
    with open('repository-tree.html', 'w', encoding='utf-8') as f:
        f.write('\n'.join(output))
    
    print("Generated repository-tree.html")

# Run it
generate_html_tree('.')
