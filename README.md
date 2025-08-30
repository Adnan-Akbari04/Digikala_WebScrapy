# Digikala Laptop Data Scraper

A Python web scraper that extracts detailed laptop information from Digikala.com using Selenium. This tool gathers product data including names, prices, discounts, ratings, images, and technical specifications.

## 📦 Required Files Download

**Before running the script, you must download additional resources:**

1. Go to the repository's main page
2. Download the `Digikala_WebScrapy.rar` file
3. Extract it into the main project folder
4. The extracted folder should contain:
   - `chromedriver.exe` (required for the scraper to work)
   - `asus-vivobook.csv` (example of collected data)
## 🚀 Features

Extracts a comprehensive dataset for each laptop product, including:
-   **Product Title** and Brand
-   **Current Price** and Original Price (if on discount)
-   **Discount Percentage**
-   **User Rating** and Review Count
-   **Image URLs** for the product gallery
-   **Technical Specifications** (e.g., CPU, RAM, GPU, Storage, etc.)
-   Product URL

The scraped data is automatically cleaned and saved into a structured `.csv` file for easy analysis in Excel, Pandas, or any data analysis tool.

## ⚙️ Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Adnan-Akbari04/Digikala_WebScrapy.git
    cd Digikala_WebScrapy
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *The `requirements.txt` file includes: `selenium`, `pandas`*

4.  **WebDriver Setup:**
    - The project uses the ChromeDriver provided in the `resources.rar` file
    - Ensure you have Google Chrome installed
    - Keep the `chromedriver.exe` file in the main project folder


## 📖 Usage

1.  Navigate to the Digikala laptop category page and decide on your scope:
    -   **Single Page:** Scrape the first page of results (default).
    -   **Multiple Pages:** To scrape *all* available pages, uncomment the loop in the main section of the script (look for the `#TODO` comment) and adjust the range as needed. Use this cautiously to avoid sending too many requests in a short time.

2.  Run the script:
    ```bash
    python digikala_scraper.py
    ```

3.  The script will open a Chrome browser window, navigate through the pages, and extract the data. A progress log will be printed to the console.

4.  Upon completion, the data will be saved to a timestamped CSV file in the project directory (e.g., `Laptop_Type.csv`).

## ⚠️ Important Notes

-   **Website Changes:** Web scrapers are fragile. If Digikala updates its HTML structure, CSS classes, or layout, the scraper will break and will need to be updated accordingly.
-   **Responsible Scraping:** This script includes intentional delays (`time.sleep()`) to avoid overloading Digikala's servers. Please be respectful and do not aggressively run the scraper. Consider scraping during off-peak hours.
-   **Dependencies:** Ensure all libraries are installed to avoid `ModuleNotFoundError`.
-   **Network Stability:** A slow or unstable connection may cause timeouts. The script includes basic error handling for common issues, but may not cover all edge cases.

For questions or issues, please check that you've downloaded and extracted the required `Digikala_WebScrapy.rar` file first.

