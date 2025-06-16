import csv
import random

# Some messy data samples
NAMES = ['John Doe', 'Jane Smith', 'Alice Cooper', 'Bob Lee',
          'Charlie Brown', 'Eve Adams', 'Dave O', 'Grace Harper',
          'Heidi Lopez', 'Ivan Petrov', 'Jasper Hill',
          '', 'Mike Ross', 'Harvey Specter']

EMAILS = ['johndoe[at]gmail.com', 'jane.smith@example.com', 'invalidemail.com',
          'bob.lee@', 'alice@doe.org', 'carol.king@gmail',
          'dave.o@example.com', 'eve.adams@example.com',
          'h.i@foo.com']

STREETS = ['123 Elm St', '456 Oak St', '789 Pine St',
            '303 Cedar Blvd', '404 Spruce St',
            '505 Aspen Way', '606 Palm St']

CITIES = ['Metropolis', 'Gotham', 'Star City',
          'Smallville', 'Central City',
          'Coast City', 'Blüdhaven']

COUNTRIES = ['USA', 'United States', 'Unites States',
              'Canada', 'Canad', 'United Kindgom',
              'UK', 'German', 'Frnce', 'Italy']

# Generate messy CSV with 50 entries
with open('sample_input.csv', mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'email', 'street', 'city', 'country'])

    for _ in range(50):
        row = [
            random.choice(NAMES),
            random.choice(EMAILS),
            random.choice(STREETS),
            random.choice(CITIES),
            random.choice(COUNTRIES)
        ]
        writer.writerow(row)


print("sample_input.csv with messy data successfully created.")
