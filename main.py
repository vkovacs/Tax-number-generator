# https://hu.wikipedia.org/wiki/Ad%C3%B3azonos%C3%ADt%C3%B3_jel
from datetime import date

reference_date = date(1867, 1, 1)

birth_date = date(1867, 2, 1)

elapsed_days = birth_date - reference_date

print(elapsed_days)

