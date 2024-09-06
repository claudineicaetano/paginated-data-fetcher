# Paginated Data Fetcher using JWT Authentication

This Python script fetches paginated data from a RESTful API endpoint using JWT authentication. It automatically handles token expiration, allowing users to input a new token when the current one expires, and continues fetching data from the last successfully processed page. The fetched data is saved in a CSV file.

## Features

- Fetches paginated data from an API using JWT tokens.
- Automatically prompts for a new token when the current one expires (e.g., due to a 401 or 403 HTTP status code).
- Continues fetching data from the last successfully saved page if interrupted.
- Saves data to a CSV file with columns `page`, `userId`, `companyId`, and `identifierCode`.

## Prerequisites

Before running the script, ensure that you have the following:

- Python 3.x installed.
- The `requests` library installed. If not, install it by running:
  ```bash
  pip install requests

## How to Use

1. **Clone the repository**:
    ```bash
    git clone https://github.com/claudineicaetano/paginated-data-fetcher.git
    cd paginated-data-fetcher
    ```

2. **Run the script**:
    To start fetching data, simply run the script in your terminal or command prompt:
    ```bash
    python fetch_data.py
    ```

3. **Enter the JWT token**:
   When prompted, provide your JWT token for authentication:
   ```bash
   Enter the JWT token: your_token_here

4. **New token input on expiration:** 
   If the token expires during execution, the script will automatically pause and ask you to provide a new JWT token. After providing the new token, the script will resume from the last successfully saved page.

5. **Output**:
   The data will be saved in a CSV file named `paginated_data.csv` located in the current working directory. Each row in the CSV file will contain the following columns:
   - **`page`**: The page number of the API request.
   - **`userId`**: The unique identifier of the user.
   - **`companyId`**: The company ID associated with the user.
   - **`identifierCode`**: A code representing the user's identifiers.

## File Structure
.
├── fetch_data.py        # Main script to fetch and save paginated data
├── README.md            # Documentation
└── paginated_data.csv   # Output file with the fetched data (generated after running the script)

## Code Overview

- **`get_headers(jwt_token)`**: 
  Generates the request headers containing the JWT token.

- **`get_page(page, jwt_token)`**: 
  Makes a GET request to the API endpoint to fetch data for the specified page. Handles token expiration by checking for HTTP status codes 401 or 403.

- **`save_to_csv(page, data, csv_file)`**: 
  Saves the retrieved data to the specified CSV file. Each entry includes the page number, user ID, company ID, and identifier code.

- **`get_last_page_processed(csv_file)`**: 
  Checks the CSV file for the last successfully processed page and returns the page number to resume from. Returns 0 if the file is empty or does not exist.

- **`fetch_all_data(csv_file)`**: 
  Manages the entire process of fetching data, handling token expiration, and saving results. Continues from the last successfully saved page and handles token prompts and data saving.

## Example

Here is an example of how the data will be saved in the `paginated_data.csv` file:

| page | userId                               | companyId | identifierCode |
|------|--------------------------------------|-----------|----------------|
| 1    | 123e4567-e89b-12d3-a456-426614174000 | 1001      | 98765          |
| 1    | 123e4567-e89b-12d3-a456-426614174000 | 1001      | 12345          |
| 2    | 789e4567-e89b-12d3-a456-426614174001 | 1002      | 56789          |

- **`page`**: The page number of the API request.
- **`userId`**: The unique identifier of the user.
- **`companyId`**: The company ID associated with the user.
- **`identifierCode`**: A code representing the user's identifiers.

## Notes

- The script includes a small delay (`time.sleep(0.1)`) between API requests to avoid overwhelming the server. You can adjust this delay if needed based on the server's response time and load.

- If the script is interrupted or stopped, the CSV file will be appended to rather than overwritten. This ensures that no data is lost, but it also means that data will not be duplicated. The script will continue from the last successfully saved page when restarted.

- Ensure that your CSV file has proper write permissions and that there is enough disk space to accommodate the potentially large amount of data being fetched.

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0). See the [LICENSE](LICENSE) file for more details.

### Summary of the GPL-3.0 License

- **Freedom to Use**: You can use the software for any purpose.
- **Freedom to Study and Modify**: You can study how the program works, and change it to make it do what you wish. Access to the source code is a precondition for this.
- **Freedom to Distribute Copies**: You can redistribute copies of the original program so you can help others.
- **Freedom to Distribute Modified Versions**: You can distribute copies of your modified versions to others. By doing this you can give the whole community a chance to benefit from your changes. Access to the source code is a precondition for this.

For a detailed explanation of the GPL-3.0 license, please refer to the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html).


---

Created with ❤️ by [claudineicaetano](https://github.com/claudineicaetano)

_"Freedom" is not a freedom if you don't feel free. My requirement to participate in projects: challenge, know-how and counterparty. Live long and prosper!_
