class Party:

    def __init__(self):
        self.people = []


party = Party()
command = input()
while command != 'End':
    party.people.append(command)
    command = input()

result = f"Going: {', '.join(party.people)}"
print(result)
print(f"Total: {len(party.people)}")
