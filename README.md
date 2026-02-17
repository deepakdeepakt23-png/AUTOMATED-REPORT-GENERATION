# AUTOMATED-REPORT-GENERATION

PROJECT DESCRIPTION :
The Automated Report Generation System is a Python-based project that is designed to generate reports automatically using data stored in a file. In many companies and organizations, creating reports manually takes a lot of time and effort. People have to calculate totals, averages, and performance values by hand, which can also lead to mistakes. This project solves that problem by automating the entire report creation process.
The main objective of this project is to develop a program that can read sales information from a CSV file and generate a professional report in PDF format. The report includes important calculations and visual representation in the form of a bar chart. This makes it easy to understand business performance quickly.
In this project, the user provides a CSV file containing product details such as Product Name, Sales Amount, and Target Amount. The program reads this file using the Pandas library, which is used for handling and processing tabular data. After reading the file, the program analyzes the dataset and performs various calculations.

The program calculates the total sales, total target, and the achievement percentage, which shows how much of the target has been achieved. It also identifies the best-performing product, which is the product with the highest sales value. These calculations help in understanding overall sales performance.

After analysis, the program generates a bar chart using the Matplotlib library. The chart compares the sales and target values of all products. This graphical representation makes the report more attractive and helps users understand the performance visually.

Finally, the system creates a PDF report using the ReportLab library. The PDF includes a summary section, a detailed table showing product-wise sales and target values, and the bar chart image. The report is saved as a PDF file so that it can be easily shared or printed.

TECHNOLOGIES USED :

1.This project uses the following technologies:
2.Python (Main programming language)
3.Pandas (For reading and analyzing CSV data)
4.Matplotlib (For generating bar chart visualization)
5.ReportLab (For creating the PDF report)

Output

chart.png (Sales vs Target graph)

report.pdf (Final automated report)
