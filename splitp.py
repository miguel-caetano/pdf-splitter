import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfWriter, PdfReader

class PDFProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Processor")

        self.label = tk.Label(root, text="Selecione um arquivo PDF:")
        self.label.pack(pady=10)

        self.browse_button = tk.Button(root, text="Procurar", command=self.browse_pdf)
        self.browse_button.pack(pady=10)

        self.output_label = tk.Label(root, text="Selecione a pasta de saída:")
        self.output_label.pack(pady=5)

        self.output_button = tk.Button(root, text="Procurar Pasta", command=self.browse_output)
        self.output_button.pack(pady=5)

        self.process_button = tk.Button(root, text="Processar PDF", command=self.process_pdf)
        self.process_button.pack(pady=10)

    def browse_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            self.pdf_path = file_path
            self.label.config(text=f"Arquivo PDF selecionado: {self.pdf_path}")

    def browse_output(self):
        output_dir = filedialog.askdirectory()
        if output_dir:
            self.output_path = output_dir
            self.output_label.config(text=f"Pasta de saída selecionada: {self.output_path}")

    def process_pdf(self):
        try:
            input_pdf = PdfReader(open(self.pdf_path, "rb"))

            for i, page in enumerate(input_pdf.pages):
                output = PdfWriter()
                output.add_page(page)

                output_path = f"{self.output_path}/document-page{i + 1}.pdf"
                with open(output_path, "wb") as output_stream:
                    output.write(output_stream)

            tk.messagebox.showinfo("Concluído", f"PDF dividido em {len(input_pdf.pages)} páginas.")
        except Exception as e:
            tk.messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFProcessorApp(root)
    root.mainloop()