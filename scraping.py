# importing the necessary packages
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import xlsxwriter

#List for storing the results
element_list = list()

#Scraping the web pages using a for loop
for page in range(1, 3, 1):
    page_url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=" + str(page)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(page_url)
    title = driver.find_elements_by_class_name('title')
    price = driver.find_elements_by_class_name('price')
    description = driver.find_elements_by_class_name('description')
    rating = driver.find_elements_by_class_name('ratings')

    for i in range(len(title)):
        element_list.append([title[i].text, price[i].text, description[i].text, rating[i].text])

# print(element_list)

#Closing the driver
driver.close()


#storing the data in an excel file
with xlsxwriter.Workbook('result3.xlsx') as workbook:
    worksheet = workbook.add_worksheet()

    for row_num, data in enumerate(element_list):
        worksheet.write_row(row_num, 0, data)
