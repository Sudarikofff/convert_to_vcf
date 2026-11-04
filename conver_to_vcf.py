import json

with open("primorsky_numbers.json", "r", encoding="utf-8") as f:
    numbers = json.load(f)

with open("contacts.vcf", "w", encoding="utf-8", newline="") as f:
    for i, number in enumerate(numbers, start=1):
        phone = str(number).strip()

        if not phone:
            continue

        if phone.startswith("8") and len(phone) == 11:
            phone = "+7" + phone[1:]
        elif phone.startswith("7") and len(phone) == 11:
            phone = "+" + phone

        name = f"Контакт {phone}"

        vcard = [
            "BEGIN:VCARD",
            "VERSION:2.1",
            f"N:;{name};;;",
            f"FN:{name}",
            f"TEL;CELL:{phone}",
            "END:VCARD"
        ]

        f.write("\r\n".join(vcard) + "\r\n")

print("Готово! Создан contacts.vcf")