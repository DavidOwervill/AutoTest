from faker import Faker


class WebTabletsGen(Faker):
    first_name_gen = Faker().name().split(" ")[0]
    last_name_gen = Faker().name().split(" ")[0]
    email_gen = Faker().ascii_email()
    age_gen = Faker().random.randint(18, 56)
    solary_gen = Faker().random.randint(10000, 100000)
    dep_gen = Faker().company()
    first_name_gen_changes = Faker().name().split(" ")[0]


if __name__ == "__main__":
    print(WebTabletsGen.first_name_gen,
          WebTabletsGen.last_name_gen,
          WebTabletsGen.email_gen,
          )
