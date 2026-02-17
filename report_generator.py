import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors


def read_data(file_name):
    try:
        df = pd.read_csv(file_name)
        return df
    except Exception as e:
        print("ERROR reading CSV file:", e)
        return pd.DataFrame()


def analyze_data(df):
    if df.empty:
        print("ERROR: CSV file is empty or incorrect!")
        return 0, 0, "N/A", 0, 0

    total_sales = df["Sales"].sum()
    total_target = df["Target"].sum()

    best_product = df.loc[df["Sales"].idxmax(), "Product"]
    best_sales = df["Sales"].max()

    achievement_percent = (total_sales / total_target) * 100 if total_target != 0 else 0

    return total_sales, total_target, best_product, best_sales, achievement_percent


def create_bar_chart(df):
    plt.figure(figsize=(10, 5))

    plt.bar(df["Product"], df["Sales"], label="Sales")
    plt.bar(df["Product"], df["Target"], alpha=0.5, label="Target")

    plt.xticks(rotation=90)
    plt.title("Sales vs Target Report")
    plt.xlabel("Products")
    plt.ylabel("Amount")
    plt.legend()

    plt.tight_layout()
    plt.savefig("chart.png")
    plt.close()


def generate_pdf(df, summary):
    total_sales, total_target, best_product, best_sales, achievement_percent = summary

    c = canvas.Canvas("report.pdf", pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 18)
    c.drawString(170, height - 50, "Sales Performance Report")

    c.setStrokeColor(colors.black)
    c.line(50, height - 70, width - 50, height - 70)

    # Summary
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 110, "Summary:")

    c.setFont("Helvetica", 12)
    c.drawString(70, height - 140, f"Total Sales: {total_sales}")
    c.drawString(70, height - 165, f"Total Target: {total_target}")
    c.drawString(70, height - 190, f"Achievement: {achievement_percent:.2f}%")
    c.drawString(70, height - 215, f"Best Product: {best_product} (Sales: {best_sales})")

    # Table Heading
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 260, "Product")
    c.drawString(250, height - 260, "Sales")
    c.drawString(400, height - 260, "Target")

    c.line(50, height - 270, width - 50, height - 270)

    # Table Data
    y = height - 295
    c.setFont("Helvetica", 11)

    for _, row in df.iterrows():
        c.drawString(50, y, str(row["Product"]))
        c.drawString(250, y, str(row["Sales"]))
        c.drawString(400, y, str(row["Target"]))
        y -= 20

        if y < 100:
            c.showPage()
            y = height - 50

    # Chart Page
    c.showPage()
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, height - 50, "Sales vs Target Chart")

    c.drawImage("chart.png", 60, 200, width=480, height=300)

    # Footer
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(50, 30, "Generated Automatically using Python + Matplotlib + ReportLab")

    c.save()
    print("✅ Report Generated Successfully: report.pdf")


if __name__ == "__main__":
    df = read_data("data.csv")

    if not df.empty:
        summary = analyze_data(df)
        create_bar_chart(df)
        generate_pdf(df, summary)
    else:
        print("❌ No report generated because CSV is empty.")
