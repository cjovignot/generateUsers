import random
import math
import json
import string
import requests
import unicodedata
import copy
from geopy.geocoders import Nominatim

# nicotest reference data
nicotest_reference = {
    "email": "",
    "password": "$2b$10$0dhYS4M.UQPwp6aYJnAg0u8MzNQzTHl3kjMhVrlvPdTEPKywCkTEO",
    "premium": False,
    "geoloc": [
        48.859,
        2.347
    ],
    "languages": [
        "Java",
        "Python"
    ],
    "attraction": [
        "Female"
    ],
    "pictures": [],
    "matched": [],
    "rejected": [],
    "chatIds": [],
    "__v": 0,
    "address": "",
    "age": "1920-06-09",
    "city": "",
    "firstName": "",
    "lastName": "",
    "name": "",
    "profilePicture": "",
    "profileStatus": "Merge",
    "sex": "Female"
}

# prout@prout reference data
prout_reference = {
    "premium": False,
    "email": "",
    "password": "$2b$10$gXUUmMr8hi/uehbSlso04.Ua6km7Sq7hqxwj9MgoOoZ1nFsQEr9Wm",
    "geoloc": [
        47.239367,
        -1.555335
    ],
    "languages": [
        "Go",
        "C++"
    ],
    "attraction": [
        "Female"
    ],
    "pictures": [],
    "matched": [],
    "rejected": [],
    "chatIds": [],
    "__v": 0,
    "profileStatus": "Const",
    "address": "",
    "age": "2002-02-28",
    "city": "Nantes",
    "firstName": "",
    "lastName": "",
    "name": "",
    "profilePicture": "",
    "sex": "Female",
    "swipe": 20,
    "timerSwipe": ""
}

# bijou@bijou reference data
bijou_reference = {
    "premium": False,
    "email": "",
    "password": "$2b$10$OrAQWrdRVbe9RLbUnUJqkuYpsxqpOCTKu/Sr1Z1J54Gm8W/HGh3ly",
    "geoloc": [
        47.239367,
        -1.555335
    ],
    "languages": [
        "JavaScript",
        "Rust"
    ],
    "attraction": [
        "Female"
    ],
    "pictures": [],
    "matched": [],
    "rejected": [],
    "chatIds": [],
    "__v": 0,
    "address": "",
    "age": "1999-06-09",
    "city": "Paris",
    "firstName": "tutut",
    "lastName": "prout",
    "name": "bijou2",
    "profilePicture": "",
    "profileStatus": "Merge",
    "sex": "Female",
    "swipe": 20,
}

# seb@seb reference data
seb_reference = {
  "premium": False,
  "email": "",
  "password": "$2b$10$gXUUmMr8hi/uehbSlso04.Ua6km7Sq7hqxwj9MgoOoZ1nFsQEr9Wm",
  "geoloc": [
    48.894215,
    2.286846
  ],
  "languages": [
    "Go",
    "C#"
  ],
  "attraction": [
    "Male"
  ],
  "matched": [],
  "rejected": [],
  "chatIds": [],
  "__v": 0,
  "address": "27 Avenue de la Fontaine 94290 Villeneuve-le-Roi",
  "age": "2002-02-28",
  "city": "Levallois-perret",
  "firstName": "testtut",
  "lastName": "hello",
  "name": "user1",
  "pictures": [],
  "profilePicture": "",
  "profileStatus": "Merge",
  "sex": "Male",
  "swipe": 20,
}

# random reference data
random_reference = {
    "premium": False,
    "email": "",
    "password": "$2b$10$gXUUmMr8hi/uehbSlso04.Ua6km7Sq7hqxwj9MgoOoZ1nFsQEr9Wm",
    "geoloc": [
        "latitude",
        "longitude"
    ],
    "languages": [
        "Java",
        "Go",
        "C",
        "C#",
        "C++",
        "Rust",
        "JavaScript",
        "Python",
    ],
    "attraction": [
        "Female",
        "Male",
        "Other"
    ],
    "pictures": [],
    "matched": [],
    "rejected": [],
    "chatIds": [],
    "__v": 0,
    "profileStatus": [
        "Const",
        "Merge"
    ],
    "address": "",
    "age": "2002-02-28",
    "city": "",
    "firstName": "",
    "lastName": "",
    "name": "",
    "profilePicture": "",
    "sex": [
        "Female",
        "Male",
        "Other"
    ],
    "swipe": 20,
    "timerSwipe": ""
}

geolocator = Nominatim(user_agent="my_application")




# Generate random distance between 1km and 30km
def generate_random_distance():
    return random.uniform(1, 30)

# Generate random geolocation coordinates based on the reference geolocation and distance
def generate_random_geolocation(reference_geoloc, distance):
    lat, lon = reference_geoloc
    r = distance / 111.32
    theta = random.random() * 2 * math.pi
    dx = r * math.cos(theta)
    dy = r * math.sin(theta)
    new_lon = lat + dx
    new_lat = lon + dy
    return [new_lon, new_lat]


# Generate random French geolocation coordinates
def generate_geoloc_fr():
    return random.choice([
        [48.85341, 2.3488],
        [43.29695, 5.38107],
        [45.74846, 4.84671],
        [43.60426, 1.44367],
        [43.70313, 7.26608],
        [47.21725, -1.55336],
        [48.58392, 7.74553],
        [43.61093, 3.87635],
        [44.84044, -0.5805],
        [50.63297, 3.05858],
        [48.11198, -1.67429],
        [49.26526, 4.02853],
        [49.4938, 0.10767],
        [45.43389, 4.39],
        [43.12442, 5.92836],
        [47.47381, -0.54774],
        [45.17869, 5.71479],
        [47.31667, 5.01667],
        [43.5283, 5.44973],
        [48.39029, -4.48628]
    ])

# Generate random female first name
def generate_female_first_name():
    return random.choice([
        "Emma", "Olivia", "Ava", "Isabella", "Sophia", "Mia", "Charlotte", "Amelia", "Harper", "Evelyn"
    ])

# Generate random male first name
def generate_male_first_name():
    return random.choice([
        "Liam", "Noah", "Oliver", "Elijah", "William", "James", "Benjamin", "Lucas", "Henry", "Alexander"
    ])

# Generate random last name
def generate_last_name():
    return random.choice([
        "Smith", "Johnson", "Brown", "Davis", "Miller", "Wilson", "Moore", "Anderson", "Taylor", "Thomas"
    ])

# Generate random email
def generate_random_email():
    domain = ["gmail.com", "yahoo.com", "hotmail.com", "example.com"]  # Add more domains if needed
    username = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
    email = f"{username}@{random.choice(domain)}"
    return email

# PHOTOS
# Generate random female pictures using the Unsplash API
def generate_female_pictures():
    num_pictures = random.randint(2, 5)
    pictures = []
    for _ in range(num_pictures):
        url = get_random_unsplash_image("female")
        pictures.append(url)
    return pictures

# Generate random male pictures using the Unsplash API
def generate_male_pictures():
    num_pictures = random.randint(2, 5)
    pictures = []
    for _ in range(num_pictures):
        url = get_random_unsplash_image("male")
        pictures.append(url)
    return pictures

# Get a random image URL of the specified category from the Unsplash API
def get_random_unsplash_image(category):
    # Replace "YOUR_UNSPLASH_API_KEY" with your actual Unsplash API key
    api_key = "zKSy3DvIFwZT4Dw2PDcG_zd0-iw0X8KdwkJzUAHUDAA"
    endpoint = f"https://api.unsplash.com/photos/random?query={category}&client_id={api_key}"
    response = requests.get(endpoint)
    if response.status_code == 200:
        data = response.json()
        if "urls" in data and "regular" in data["urls"]:
            return data["urls"]["regular"]
    return ""  # Return an empty string if image URL cannot be retrieved
# END PHOTOS

# Prompt for reference choice
print("Choose a reference:")
print("1. Nicotest")
print("2. Prout")
print("3. Bijou")
print("4. Seb")
print("5. Random")

reference_choice = input("Enter the number of the reference you want to use: ")

if reference_choice == "1":
    user_reference = nicotest_reference
elif reference_choice == "2":
    user_reference = prout_reference
elif reference_choice == "3":
    user_reference = bijou_reference
elif reference_choice == "4":
    user_reference = seb_reference
elif reference_choice == "5":
    user_reference = random_reference


# Generate 10 user profiles
num_profiles = 10
generated_profiles = []




if user_reference != random_reference:
    for _ in range(num_profiles):
        # Create a new profile based on user reference
        new_profile = user_reference.copy()

        # Generate random distance
        distance = generate_random_distance()

        # Generate random geolocation based on the reference geolocation and distance
        new_geoloc = generate_random_geolocation(user_reference["geoloc"], distance)
        new_profile["geoloc"] = new_geoloc

        # Get the address based on the generated geolocation
        location = geolocator.reverse(new_geoloc, exactly_one=True)
        address = location.address if location else ""

        # Decode Unicode escape sequences in the address
        address = address.encode("utf-8", errors="ignore").decode("utf-8")
        address = address.encode("latin-1").decode("unicode_escape")

        # Extract the city name from the address
        street_number = location.raw.get("address", {}).get("house_number", "")
        road_name = location.raw.get("address", {}).get("road", "")
        postcode = location.raw.get("address", {}).get("postcode", "")
        city_name = location.raw.get("address", {}).get("city", "")

        if not street_number:
            street_number = str(random.randint(1, 100))

        if not road_name:
            road_name = location.raw.get("address", {}).get("pedestrian", "")
        if not road_name:
            road_name = location.raw.get("address", {}).get("footway", "")
        if not road_name:
            road_name = location.raw.get("address", {}).get("road_reference", "")
        if not road_name:
            road_name = location.raw.get("address", {}).get("residential", "")

        if not city_name:
            city_name = location.raw.get("address", {}).get("town", "")
        if not city_name:
            city_name = location.raw.get("address", {}).get("village", "")
        if not city_name:
            city_name = location.raw.get("address", {}).get("county", "")

        # Update formatted address with the desired components
        new_profile["city"] = city_name

        # Update address with formatted address
        formatted_address = f"{street_number}, {road_name}, {postcode}, {city_name}"
        new_profile["address"] = formatted_address

        # Update profileStatus, sex, and attraction
        if user_reference["profileStatus"] == "Const":
            new_profile["profileStatus"] = "Const"
        if user_reference["profileStatus"] == "Merge":
            new_profile["profileStatus"] = "Merge"

        if user_reference["sex"] == "Female":
            new_profile["attraction"] = "Female"
        if user_reference["sex"] == "Male":
            new_profile["attraction"] = "Male"

        if user_reference["attraction"] == "Male":
            new_profile["sex"] = "Male"
        if user_reference["attraction"] == "Female":
            new_profile["sex"] = "Female"

        # Update email
        first_name = generate_female_first_name() if new_profile["sex"] == "Female" else generate_male_first_name()
        last_name = generate_last_name()
        new_profile["email"] = generate_random_email()

# PHOTOS
        # Define the number of URLs you want to generate
        num_urls = random.randint(2, 5)

        # # Update pictures array with random female or male pictures
        if new_profile["sex"] == "Female":
            new_profile["pictures"] = generate_female_pictures()
        else:
            new_profile["pictures"] = generate_male_pictures()

        # Update profile picture with the first picture in the array
        if new_profile["pictures"]:
            new_profile["profilePicture"] = new_profile["pictures"][0]
# END PHOTOS

        # Update password
        new_profile["password"] = user_reference["password"]

        # Update firstName, lastName, and name
        new_profile["firstName"] = first_name
        new_profile["lastName"] = last_name
        new_profile["name"] = first_name


        # Add the new profile to the list
        generated_profiles.append(new_profile)

            
    # Save profiles to a JSON file
    filename = "personnalizedUsers.json"

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(generated_profiles, file, indent=2, ensure_ascii=False)
        

    print("User profiles saved in:", filename)
    
else:
    for _ in range(num_profiles):
        # Create a new profile based on user reference
        new_profile = user_reference.copy()

        new_profile["email"] = generate_random_email()
        
        geoloc = generate_geoloc_fr()

        # Generate random distance
        distance = generate_random_distance()

        # Generate random geolocation based on the reference geolocation and distance
        new_geoloc = generate_random_geolocation(geoloc, distance)
        new_profile["geoloc"] = new_geoloc

        # Get the address based on the generated geolocation
        location = geolocator.reverse(new_geoloc, exactly_one=True)
        address = location.address if location else ""

        # Decode Unicode escape sequences in the address
        address = address.encode("utf-8", errors="ignore").decode("utf-8")
        address = address.encode("latin-1").decode("unicode_escape")

        # Extract the city name from the address
        street_number = location.raw.get("address", {}).get("house_number", "")
        road_name = location.raw.get("address", {}).get("road", "")
        postcode = location.raw.get("address", {}).get("postcode", "")
        city_name = location.raw.get("address", {}).get("city", "")

        if not street_number:
            street_number = str(random.randint(1, 100))

        if not road_name:
            road_name = location.raw.get("address", {}).get("pedestrian", "")
        if not road_name:
            road_name = location.raw.get("address", {}).get("footway", "")
        if not road_name:
            road_name = location.raw.get("address", {}).get("road_reference", "")
        if not road_name:
            road_name = location.raw.get("address", {}).get("residential", "")

        if not city_name:
            city_name = location.raw.get("address", {}).get("town", "")
        if not city_name:
            city_name = location.raw.get("address", {}).get("village", "")
        if not city_name:
            city_name = location.raw.get("address", {}).get("county", "")

        # Update formatted address with the desired components
        new_profile["city"] = city_name

        # Update address with formatted address
        formatted_address = f"{street_number}, {road_name}, {postcode}, {city_name}"
        new_profile["address"] = formatted_address

        # Random language generation
        languages = random.sample(user_reference["languages"], 2)
        new_profile["languages"] = [languages]

        # Random attraction generation
        attraction = random.choice(user_reference["attraction"])
        new_profile["attraction"] = [attraction]

        # Random profile status generation
        profile_status = random.choice(user_reference["profileStatus"])
        new_profile["profileStatus"] = [profile_status]

        # Random sex generation
        sex = random.choice(user_reference["sex"])
        new_profile["sex"] = sex

        # Random sex generation
        sex = random.choice(["Male", "Female", "Other"])

        # Random first name generation based on sex
        if sex == "Other":
            if random.choice([True, False]):
                first_name = generate_male_first_name()
            else:
                first_name = generate_female_first_name()
        elif sex == "Male":
            first_name = generate_male_first_name()
        else:
            first_name = generate_female_first_name()

        new_profile["firstName"] = first_name
        new_profile["name"] = first_name
        new_profile["lastName"] = generate_last_name()

# PHOTOS
        # Define the number of URLs you want to generate
        num_urls = random.randint(2, 5)

        # # Update pictures array with random female or male pictures
        if new_profile["sex"] == "Female":
            new_profile["pictures"] = generate_female_pictures()
        else:
            new_profile["pictures"] = generate_male_pictures()

        # Update profile picture with the first picture in the array
        if new_profile["pictures"]:
            new_profile["profilePicture"] = new_profile["pictures"][0]
# END PHOTOS

        # Update password
        new_profile["password"] = user_reference["password"]


        # Add the new profile to the list
        generated_profiles.append(new_profile)



    # Save profiles to a JSON file
    filename = "randomizedUsers.json"

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(generated_profiles, file, indent=2, ensure_ascii=False)
        

    print("User profiles saved in:", filename)
