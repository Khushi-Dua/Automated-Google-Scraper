# Google Search Results Scraper 🔎🎨

Welcome to the **Google Search Results Scraper** repository! 🌟 This project is designed to simplify your research and SEO analysis by automating Google searches and extracting valuable data from the top results. Built with the power of Python and automation libraries like Selenium and BeautifulSoup, this scraper gathers titles, links, and descriptions effortlessly. 



## Features 🔄

- **Automated Google Searches**: Perform searches on Google programmatically.
- **Data Extraction**: Fetch:
  - Titles 🔖
  - Links 🔗
  - Short Descriptions 📖
- **Highly Customizable**: Configure search queries, number of results, and more!
- **Easy-to-Use**: Built with simplicity and efficiency in mind.



## Tech Stack 🧠

- **Programming Language**: Python 🐍
- **Libraries Used**:
  - [Selenium](https://www.selenium.dev/): For browser automation.
  - [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/): For HTML parsing.
  - [Pandas](https://pandas.pydata.org/): To organize and save the data.
- **Browser**: ChromeDriver 🍽⭐

## How It Works 🚀

1. Input your search query.
2. The scraper uses Selenium to navigate to Google and fetch the search results.
3. BeautifulSoup extracts the desired details (titles, links, and descriptions).
4. Data is displayed neatly in the terminal or saved as a CSV file for your convenience

## Getting Started 🎮

### Prerequisites 

- Python 3.7+
- Google Chrome installed
- ChromeDriver (compatible with your browser version)

### Installation 

1. Clone this repository:
   ```bash
   git clone https://github.com/Khushi-Dua/google-search-scraper.git
   cd google-search-scraper
   ```

2. Install dependencies:
   ```bash
   pip install requests
   pip install beautifulsoup4
   pip install urllib
   ```

3. Make sure ChromeDriver is in your PATH.

### Usage 

1. Run the script:
   ```bash
   python scraper.py
   ```

2. Enter your search query when prompted.

3. View the results directly in the terminal or find them in the `output.csv` file.

## Code Structure 🌐

```
Google-Search-Scraper/
├── scraper.py          # Main script for scraping
├── requirements.txt    # Dependencies
├── README.md           # Project documentation
└── output.csv          # (Generated) Extracted data
```

## License 📚

This project is licensed under the [MIT License](LICENSE).

## 🤝 Acknowledgment
This project was completed as part of the CODEXINTERN Python Development Internship (December 2024). Grateful for the opportunity to learn and apply practical skills in Python development and API integration.

## Let's Connect! 📢

- **GitHub**: [Khushi-Dua](https://github.com/Khushi-Dua)
- **LinkedIn**: [Khushi Dua](https://linkedin.com/in/khushi-dua7)
- **Email**: khushidua110036@gmail.com

Happy Scraping! 🙌🌐

