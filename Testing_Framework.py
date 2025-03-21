import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Hardcoded data from the Excel sheet (the data you provided)
data = [
    {"Full Name": "Aarav Sharma", "Email": "aarav.sharma@example.com", "Phone Number": "987-654-3210", "Address": "Delhi, Delhi", "Pincode": "110001"},
    {"Full Name": "Priya Patel", "Email": "priya.patel@example.com", "Phone Number": "998-765-4321", "Address": "Mumbai, Maharashtra", "Pincode": "400001"},
    {"Full Name": "Rohit Kumar", "Email": "rohit.kumar@example.com", "Phone Number": "912-345-6789", "Address": "Bangalore, Karnataka", "Pincode": "560001"},
    {"Full Name": "Ananya Desai", "Email": "ananya.desai@example.com", "Phone Number": "934-567-8901", "Address": "Chennai, Tamil Nadu", "Pincode": "600001"},
    {"Full Name": "Vikram Yadav", "Email": "vikram.yadav@example.com", "Phone Number": "945-678-9012", "Address": "Hyderabad, Telangana", "Pincode": "500001"},
    {"Full Name": "Neha Gupta", "Email": "neha.gupta@example.com", "Phone Number": "903-456-7890", "Address": "Pune, Maharashtra", "Pincode": "411001"},
    {"Full Name": "Rajesh Reddy", "Email": "rajesh.reddy@example.com", "Phone Number": "920-567-8901", "Address": "Ahmedabad, Gujarat", "Pincode": "380001"},
    {"Full Name": "Sunita Verma", "Email": "sunita.verma@example.com", "Phone Number": "930-678-9012", "Address": "Kolkata, West Bengal", "Pincode": "700001"},
    {"Full Name": "Karan Singh", "Email": "karan.singh@example.com", "Phone Number": "945-789-0123", "Address": "Jaipur, Rajasthan", "Pincode": "302001"},
    {"Full Name": "Aisha Khan", "Email": "aisha.khan@example.com", "Phone Number": "910-123-4567", "Address": "Lucknow, Uttar Pradesh", "Pincode": "226001"},
    {"Full Name": "Sameer Ahmed", "Email": "sameer.ahmed@example.com", "Phone Number": "922-234-5678", "Address": "Surat, Gujarat", "Pincode": "395001"},
    {"Full Name": "Priyanka Mehta", "Email": "priyanka.mehta@example.com", "Phone Number": "983-345-6789", "Address": "Indore, Madhya Pradesh", "Pincode": "452001"},
    {"Full Name": "Devendra Joshi", "Email": "devendra.joshi@example.com", "Phone Number": "970-456-7890", "Address": "Noida, Uttar Pradesh", "Pincode": "201301"},
    {"Full Name": "Deepika Rao", "Email": "deepika.rao@example.com", "Phone Number": "990-567-8901", "Address": "Kochi, Kerala", "Pincode": "682001"},
    {"Full Name": "Arvind Bhatia", "Email": "arvind.bhatia@example.com", "Phone Number": "904-678-9012", "Address": "Chandigarh, Chandigarh", "Pincode": "160001"},
]

# URL of the Google Form
form_url = "https://forms.gle/UH68hCXnKnZEWwVWA"

# Set up the WebDriver with webdriver_manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the Google Form
driver.get(form_url)

wait = WebDriverWait(driver, 10)

# Loop through the hardcoded data and fill out the form
for entry in data:
    # Full Name
    full_name_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-labelledby="i1 i4"]')))
    full_name_field.clear()
    full_name_field.send_keys(entry['Full Name'])

    # Email
    email_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-labelledby="i6 i9"]')))
    email_field.clear()
    email_field.send_keys(entry['Email'])

    # Phone Number
    phone_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-labelledby="i11 i14"]')))
    phone_field.clear()
    phone_field.send_keys(str(entry['Phone Number']))

    # Address
    address_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-labelledby="i16 i19"]')))
    address_field.clear()
    address_field.send_keys(entry['Address'])

    # Pincode
    pincode_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-labelledby="i21 i24"]')))
    pincode_field.clear()
    pincode_field.send_keys(str(entry['Pincode']))

    # Submit the form
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@class, "NPEfkd RveJvd snByac")]')))
    submit_button.click()

    # Wait for the form to submit and reload
    time.sleep(3)

    # Reload the form to fill out the next entry
    driver.get(form_url)
    time.sleep(2)

# Close the browser
driver.quit()
