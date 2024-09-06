import requests
import time
import csv

base_url = "https://api.security-api.com/data"
jwt_token = input("Enter the JWT token: ")  


def get_headers(jwt_token):
    return {"Authorization": f"Bearer {jwt_token}"}

def get_page(page, jwt_token):
    params = {
        "page": page, 
        "size": 20 
    }
    
    response = requests.get(base_url, headers=get_headers(jwt_token), params=params)
    
    if response.status_code in [401, 403]:
        print(f"Token expired while fetching page {page}.")
        return "token_expired"
    elif response.status_code == 200:
        return response.json() 
    else:
        print(f"Error: {response.status_code} while fetching page {page}")
        return None

def save_to_csv(page, data, csv_file):
    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        for user in data:
            user_id = user['userId']
            company_id = user['companyId']
            identifiers = user['identifiers']
            
            for identifier in identifiers:
                identifier_code = identifier['identifierCode']
                writer.writerow([page, user_id, company_id, identifier_code])

def get_last_page_processed(csv_file):
    try:
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = list(reader)
            if len(rows) > 1:
                return int(rows[-1][0]) 
            else:
                return 0 
    except FileNotFoundError:
        return 0  

def fetch_all_data(csv_file):
    page = get_last_page_processed(csv_file) + 1  
    
    if page == 1:
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["page", "userId", "companyId", "identifierCode"])
    
    while True:
        print(f"Fetching page {page}...")
        data = get_page(page, jwt_token)
        
        
        if data == "token_expired":
            jwt_token = input("Enter the new JWT token: ")  
            continue  
        
        if not data or not data['data']:
            break
        
        save_to_csv(page, data['data'], csv_file)
        page += 1 
        
        time.sleep(0.4)  # 15 TPS

if __name__ == "__main__":
    csv_file = "paginated_data.csv"
    fetch_all_data(csv_file)
    print(f"Data saved in the file {csv_file}")
