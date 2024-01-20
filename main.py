from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import date, timedelta

def create_pdf(output_filename):
    c = canvas.Canvas(output_filename, pagesize=letter)
    c.setFont("Times-Roman", 22)

    start_date = date.today()

    current_date = start_date
    while current_date <= date(2024,12,31):
        c.setFillColorRGB(1, 1, 0.8)  # RGB values for a yellowish color
        c.rect(0, 0, letter[0], letter[1], fill=True)
        
        c.setFont("Times-Roman", 22)
        c.setFillColorRGB(0, 0, 0)  # Cor do texto é preta
        formatted_date = current_date.strftime("%Y-%m-%d")
        weekday_name = current_date.strftime("%A")  # Obtém o nome do dia da semana
        text = f"Date: {formatted_date} ({weekday_name})"
        c.drawString(100, 750, text)
       
        c.setStrokeColorRGB(138/255, 138/255, 138/255)  # Cor do texto é preta
        line_height = 20
        for y in range(700, 100, -line_height):
            c.line(100, y, 500, y)

        c.showPage()
        current_date += timedelta(days=1)

    c.save()

if __name__ == "__main__":
    pdf_filename = "calendario.pdf"
    create_pdf(pdf_filename)
    print(f"PDF gerado com sucesso: {pdf_filename}")

