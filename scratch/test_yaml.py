import yaml
import sys

try:
    with open('_posts/2026-01-01-episode-09-en.md', 'r') as f:
        content = f.read()
        # Extract front matter
        if content.startswith('---'):
            parts = content.split('---')
            if len(parts) >= 3:
                yaml_content = parts[1]
                data = yaml.safe_load(yaml_content)
                print("Successfully parsed YAML")
                print(data)
            else:
                print("Front matter delimiters not found correctly")
        else:
            print("File does not start with ---")
except Exception as e:
    print(f"Error: {e}")
