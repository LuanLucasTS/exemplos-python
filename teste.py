from faker import Faker


fake = Faker()

for i in range (100):
    nascimento = fake.date_of_birth()
    print(nascimento)
