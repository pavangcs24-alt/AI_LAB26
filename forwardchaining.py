
# Forward Chaining: Robert is Criminal or Not

print("FORWARD CHAINING ALGORITHM")
print("--------------------------")
print("Enter facts in predicate format.")
print("Example: American(Robert)")
print("Type 'done' to finish.\n")

# Get facts from user
facts = set()

while True:
    fact = input("Enter fact: ").strip()

    if fact.lower() == "done":
        break

    facts.add(fact)

# Rules in Knowledge Base
rules = [
    (["Enemy(A,America)"], "Hostile(A)"),

    (["Missile(M1)"], "Weapon(M1)"),

    (["Missile(M1)", "Owns(A,M1)"],
     "Sells(Robert,M1,A)"),

    (["American(Robert)", "Weapon(M1)",
      "Sells(Robert,M1,A)", "Hostile(A)"],
     "Criminal(Robert)")
]

# Forward Chaining function
def forward_chaining(facts, rules):

    while True:
        new_facts = set()

        for conditions, conclusion in rules:

            if all(c in facts for c in conditions):

                if conclusion not in facts:
                    print("Derived:", conclusion)
                    new_facts.add(conclusion)

        if not new_facts:
            break

        facts.update(new_facts)

    return "Criminal(Robert)" in facts


# Check the goal
print("\nApplying Forward Chaining...\n")

result = forward_chaining(facts, rules)

if result:
    print("\nRESULT: Robert is a Criminal.")
else:
    print("\nRESULT: Robert is NOT PROVED to be a Criminal.")
