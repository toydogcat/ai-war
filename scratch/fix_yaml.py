import os
import re

posts_dir = '_posts'
files_to_fix = [
    '2026-01-01-episode-01-en.md',
    '2026-01-09-episode-09-en.md',
    '2026-01-10-episode-10-en.md',
    '2026-01-14-episode-14-en.md',
    '2026-01-15-episode-15-en.md',
    '2026-01-25-episode-25-en.md',
    '2026-01-26-episode-26-en.md',
    '2026-01-27-episode-27-en.md',
    '2026-01-28-episode-28-en.md',
    '2026-01-30-episode-30-en.md',
    '2026-02-02-episode-33-en.md',
    '2026-02-03-episode-34-en.md',
    '2026-02-04-episode-35-en.md',
    '2026-02-06-episode-37-en.md',
    '2026-02-10-episode-41-en.md'
]

for filename in files_to_fix:
    path = os.path.join(posts_dir, filename)
    if not os.path.exists(path):
        continue
    
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    fixed = False
    for line in lines:
        if line.startswith('twitter_text:'):
            # Replace \' with ''
            if "\\'" in line:
                line = line.replace("\\'", "''")
                fixed = True
        new_lines.append(line)
    
    if fixed:
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"Fixed {filename}")
    else:
        print(f"No fix needed for {filename}")
