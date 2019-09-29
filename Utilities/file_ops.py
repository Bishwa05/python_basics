from pathlib import Path
# Relative path
path = Path("ecommerce")
print(path.exists())

for file in path.glob('*.py'):
    print(file)
