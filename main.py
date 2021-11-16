# https://hu.wikipedia.org/wiki/Ad%C3%B3azonos%C3%ADt%C3%B3_jel
from datetime import date

def generate_tax_number(birth_date, serial_number):
    reference_date = date(1867, 1, 1)
    customer_elapsed_days = str((birth_date - reference_date).days)

    part1 = str(8)
    part2 = customer_elapsed_days.zfill(5)
    part3 = serial_number.zfill(3)

    tax_number_without_checksum = part1 + part2 + part3

    checksum = generate_checksum(tax_number_without_checksum)

    if checksum == 10:
        print("Invalid customer_serial_number, checksum mod 11 cannot be 10!")
        raise SystemExit

    tax_number = tax_number_without_checksum + str(checksum)

    return tax_number


def validate_tax_number(tax_number):
    original_tax_number_without_checksum = str(tax_number)[:9]
    original_checksum = str(tax_number)[9:]

    checksum = generate_checksum(original_tax_number_without_checksum)
    checksum = checksum % 11

    return original_checksum == str(checksum)


def generate_checksum(tax_number_without_checksum):
    position = 1
    checksum = 0
    for i in tax_number_without_checksum:
        checksum = checksum + int(i) * position
        position = position + 1
    checksum = checksum % 11

    return checksum


# 1) input parameters to generate tax number from:
customer_birth_date = date(1978, 6, 7)
customer_serial_number = str(13)

print(f"Generált Adóazonosító : {generate_tax_number(customer_birth_date, customer_serial_number)}")

# 2) validate an arbitrary tax number:
tax_number_to_validate = 8385960139

if validate_tax_number(tax_number_to_validate):
    print("A megadott adószám valid")
else:
    print("A megadott adószám NEM valid")


