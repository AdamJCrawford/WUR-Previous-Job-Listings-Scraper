import os
from time import sleep
import csv
import pdfkit

urls = []
start_dates = []

months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06",
          "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}

with open("data.csv", 'r') as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        urls.append(line[0])
        start_dates.append(
            f"{line[1][-4:]}_{months[line[1][:3]]}_{line[1][4:line[1].find(',')]}")


# Specify the path to the WkHTMLtoPDF executable (change this path accordingly)
path_wkhtmltopdf = 'C:/Users/adamc/Downloads/wkhtmltopdf/bin/wkhtmltopdf.exe'

# Configure pdfkit options
options = {
    "javascript-delay": 500
}

# Generate PDF from the website and save it to a file
for i, (url, start_date) in enumerate(zip(urls[::-1], start_dates[::-1])):
    if not os.path.exists(f"pdfs/{start_date}_{url[url.rfind('/') + 1:-4]}.pdf"):

        index_of_htm = url.find("htm")

        # Check if "htm" is found in the string
        if index_of_htm != -1:
            # Find the index of the question mark after "htm"
            index_of_question_mark = url.find("?", index_of_htm)

            # Check if a question mark is found after "htm"
            if index_of_question_mark != -1:
                url = url[:index_of_question_mark]

        print(url)
        try:
            pdfkit.from_url(url, f"pdfs/{start_date}_{url[url.rfind('/') + 1:-4]}.pdf", configuration=pdfkit.configuration(
                wkhtmltopdf=path_wkhtmltopdf), options=options)
        except IOError:
            pass
