import requests

# Baca file email.txt
with open('email.txt', 'r') as file:
    emails = [line.strip() for line in file]

# URL API dan payload dasar
url = "https://api.candy-land.club/api/user/register?lang=id"
payload_template = {
    "account": "",
    "captcha": "",
    "code": "984064",
    "email_code": "",
    "pwd": "d7c3901d7a0cd3c84cf7c84ad5ec7036",
    "safety_pwd": "d7c3901d7a0cd3c84cf7c84ad5ec7036",
    "te": "",
    "user_type": 1,
    "ws": ""
}

# Loop melalui email dan kirim permintaan POST
for email in emails:
    payload = payload_template.copy()
    payload["account"] = email  # Set email dari daftar
    
    response = requests.post(url, json=payload)  # Kirim POST request
    
    # Cek status kode untuk konfirmasi registrasi
    if response.status_code == 200:
        print(f"Register {email} - Done")
    else:
        print(f"Register {email} - Failed. Status code: {response.status_code}")
