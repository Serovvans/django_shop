import json


def load_contacts_to_json(name, number, message):
    data = {"name": name, "number": number, "message": message}
    contacts = []
    with open("data/contacts.json", "r", encoding="utf-8") as f:
        contacts = json.load(f)
    contacts.append(data)
    with open("data/contacts.json", "w", encoding="utf-8") as f:
        json.dump(contacts, f)
