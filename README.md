# Digikala Laptop Data Scraper

A Python web scraper that extracts detailed laptop information from Digikala.com using Selenium. This tool gathers product data including names, prices, discounts, ratings, images, and technical specifications.

## 📦 Required Files Download

**Before running the script, you must download additional resources:**

1. Go to the repository's main page
2. Download the `Digikala_WebScrapy.rar` file
3. Extract it into the main project folder
4. The extracted folder should contain:
   - `Digikala_WebScrapy.py` (main project module)
   - `chromedriver.exe` (required for the scraper to work)
   - `asus-vivobook.csv` (example of collected data)

## 🚀 Features

Extracts comprehensive laptop data:
- Product name and brand
- Current price and original price
- Discount percentage
- Customer rating and review count
- Product image URLs
- Detailed technical specifications
- Product page URL

Data is saved in structured CSV format for easy analysis.

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Adnan-Akbari04/Digikala_WebScrapy.git
   cd Digikala_WebScrapy
   ```

2. **Install required dependencies:**
   ```bash
   pip install selenium pandas
   ```

3. **WebDriver Setup:**
   - The project uses the ChromeDriver provided in the `Digikala_WebScrapy.rar` file
   - Ensure you have Google Chrome installed
   - Keep the `chromedriver.exe` file in the main project folder

## 📖 Usage

1. **Run the main module:**
   ```bash
   python Digikala_WebScrapy.py
   ```

2. **Scraping options:**
    -   Navigate to the Digikala laptop category page and decide on your scope:
    -   Single Page: Scrape the first page of results (default).
    -   Multiple Pages: To scrape *all* available pages, uncomment the loop in the main section of the script (look for the `#TODO` comment) and adjust the                range as needed. Use this cautiously to avoid sending too many requests in a short time.

3. **Output:**
   - The script creates a timestamped CSV file with all collected data
   - Progress is displayed in the console during scraping

## ⚠️ Important Notes

- **Required Files:** The scraper requires the files from the `Digikala_WebScrapy.rar` file, especially the main module `Digikala_WebScrapy.py`
- **Website Changes:** Digikala may update their layout, which could break the scraper
- **Scraping Ethics:** The script includes delays to avoid overwhelming Digikala's servers
- **Network Connection:** A stable internet connection is required for successful scraping
- **Browser Compatibility:** Ensure your Chrome version is compatible with the provided ChromeDriver
## 📄 Sample Output

The `asus-vivobook.csv` file shows the data structure collected by the scraper, including:
- Product names and prices
- Discount percentages
- Customer ratings
- Technical specifications
- Image links

## ❓ Troubleshooting & Support

Web scraping projects are inherently fragile as they depend on the website's structure, which can change without notice. If you encounter any issues:

1. **First,** ensure you have:
   - Downloaded and extracted the complete `Digikala_WebScrapy.rar` file
   - Installed all required dependencies (`selenium`, `pandas`, `numpy`, `requests`)
   - A stable internet connection
   - The latest version of Google Chrome browser

2. **If the problem persists**, please contact me via email at **adnanakbari@outlook.com** with:
   - A description of the issue
   - The full error message (if any)
   - Your operating system and Chrome version

I'll do my best to help you resolve the problem or update the scraper if Digikala's website structure has changed.

## 💼 Work Opportunities

I'm passionate about data extraction, web automation, and turning unstructured web data into valuable insights. If you:

- Have a web scraping project need
- Are looking for a data engineer or Python developer
- Need custom automation solutions
- Want to discuss potential collaboration

Please feel free to reach out to me at **adnanakbari@outlook.com**. I'm always interested in new challenges and opportunities in the field of data engineering and web automation.

You can also view my other projects on my [GitHub profile](https://github.com/Adnan-Akbari04).



For questions or issues, please check that you've downloaded and extracted the required `Digikala_WebScrapy.rar` file first and that the `Digikala_WebScrapy.py` module is present in your project folder.
