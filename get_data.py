# Get data for fortune choices
with open ("fortunes.txt", 'r') as file:
    content = file.read()
    fortune_leaves = [fortune.strip() for fortune in content.split('%') if fortune.strip()]

# Get data for tarot choices
with open("tarot_cards.txt", 'r') as file:
    content = file.read()
    tarot_cards = {lines[0].split(':')[0].strip(): {'Name': lines[0].strip(), 'Description': '\n'.join(lines[1:]).strip()}
                   for entry in content.split('%')
                   if (lines := entry.strip().split('\n')) and len(lines) >= 2
                   }
