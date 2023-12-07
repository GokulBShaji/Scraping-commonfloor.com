# Scraping-commonfloor.com
Educational purpose project for scraping commonfloor.com

## Objective
- Web Scrap Details of builder projects of Hyderabad listed in commonfloor.com
- And also scrap the property listings under this builder projects

## Procedure
- Install the following libraries - Selenium,Pandas,Openpyxl
- Install chromedriver[link](https://chromedriver.chromium.org/downloads) and place the chromdriver.exe file in the program folder(pythonProjectComm) here.
- First run builder_links_scraper.py with lines (14,42,63,215) uncommented, followed by commenting the above mentioned lines and uncommenting (15,43,64,216), followed by commenting the above mentioned lines and uncommenting (16,44,65,217), followed by commenting the above mentioned lines and uncommenting (17,45,66,218), followed by commenting the above mentioned lines and uncommenting (18,46,67,219).
- Then run combining.py file for geting all the builder links under single file i.e Hyderabad_Builders_links_Database.xlsx.
- Then run feature_scraping.py file for geting all the builder links under single file i.e hyderabad_builder_database_features.xlsx.
- Then run property_listings_scraper.py file for geting all the builder links under single file i.e property_listings_hyderabad.xlsx.
