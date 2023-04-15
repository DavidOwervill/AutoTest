from faker import Faker


class TextBoxGen:
    name_gen = Faker().name()
    email_gen = Faker().ascii_email()
    current_address_gen = Faker().street_address()
    permanent_address_gen = Faker().street_address()
