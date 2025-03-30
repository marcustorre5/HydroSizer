import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import txt_af

def aplicar_tema_claro():
    root.configure(bg="#f5f7fa")
    style.configure("TLabel", background="#f5f7fa", foreground="#333")
    style.configure("TEntry", relief="flat", fieldbackground="#fff", foreground="#000")
    style.configure("TButton", background="#007acc", foreground="#fff")
    style.map("TButton", background=[("active", "#005f99")])

def aplicar_tema_escuro():
    root.configure(bg="#333")
    style.configure("TLabel", background="#333", foreground="#fff")
    style.configure("TEntry", relief="flat", fieldbackground="#555", foreground="#fff")
    style.configure("TButton", background="#444", foreground="#fff")
    style.map("TButton", background=[("active", "#005f99")])

def alternar_tema():
    global tema_atual
    if tema_atual == 'claro':
        aplicar_tema_escuro()
        tema_atual = 'escuro'
    else:
        aplicar_tema_claro()
        tema_atual = 'claro'

def calcular():
    try:
        vasos = int(txt_vasos.get()) if txt_vasos.get() else 0
        lavatorios = int(txt_lavatorios.get()) if txt_lavatorios.get() else 0
        chuveiros = int(txt_chuveiros.get()) if txt_chuveiros.get() else 0
        pias = int(txt_pias.get()) if txt_pias.get() else 0
        maquinas_lavar = int(txt_maquinas_lavar.get()) if txt_maquinas_lavar.get() else 0
        tanques = int(txt_tanques.get()) if txt_tanques.get() else 0
        lava_loucas = int(txt_lava_loucas.get()) if txt_lava_loucas.get() else 0
        bidets = int(txt_bidets.get()) if txt_bidets.get() else 0
        mictorios = int(txt_mictorios.get()) if txt_mictorios.get() else 0
        banheiras = int(txt_banheiras.get()) if txt_banheiras.get() else 0
        valvulas_descarga = int(txt_valvulas_descarga.get()) if txt_valvulas_descarga.get() else 0

        perda_carga_total = calcular_perda_carga(vasos, lavatorios, chuveiros, pias, maquinas_lavar, tanques,
                                                 lava_loucas, bidets, mictorios, banheiras, valvulas_descarga)
        diametro = calcular_diametro(perda_carga_total)

        lbl_resultado.config(text=f"Diâmetro: {diametro:.2f} mm\nPerda de carga: {perda_carga_total:.2f} m.c.a")
        lbl_detalhes.config(text=f"Detalhes:\n"
                                 f"Vasos: {vasos}, Lavatórios: {lavatorios}, Chuveiros: {chuveiros}, Pias: {pias},\n"
                                 f"Máquinas de Lavar: {maquinas_lavar}, Tanques: {tanques}, Lava-Louças: {lava_loucas},\n"
                                 f"Bidês: {bidets}, Mictórios: {mictorios}, Banheiras: {banheiras}, Válvulas: {valvulas_descarga}")

        messagebox.showinfo("Sucesso", "Cálculo realizado com sucesso!")

        return diametro, perda_carga_total

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

def calcular_perda_carga(vasos, lavatorios, chuveiros, pias, maquinas_lavar, tanques, lava_loucas, bidets, mictorios,
                         banheiras, valvulas_descarga):
    peso_hidraulico = {
        'vaso': 0.3,
        'lavatorio': 0.3,
        'chuveiro': 0.4,
        'pia': 0.7,
        'maquina_lavar': 1,
        'tanque': 0.7,
        'lava_loucas': 1,
        'bidet': 0.1,
        'mictorio': 2.8,
        'banheira': 1,
        'valvula_descarga': 32
    }

    return (vasos * peso_hidraulico['vaso'] +
            lavatorios * peso_hidraulico['lavatorio'] +
            chuveiros * peso_hidraulico['chuveiro'] +
            pias * peso_hidraulico['pia'] +
            maquinas_lavar * peso_hidraulico['maquina_lavar'] +
            tanques * peso_hidraulico['tanque'] +
            lava_loucas * peso_hidraulico['lava_loucas'] +
            bidets * peso_hidraulico['bidet'] +
            mictorios * peso_hidraulico['mictorio'] +
            banheiras * peso_hidraulico['banheira'] +
            valvulas_descarga * peso_hidraulico['valvula_descarga'])

def calcular_diametro(perda_carga):
    if perda_carga <= 5:
        return 25
    elif perda_carga <= 15:
        return 32
    elif perda_carga <= 30:
        return 40
    else:
        return 50

def limpar_campos():
    for var_name in ["vasos", "lavatorios", "chuveiros", "pias", "maquinas_lavar", "tanques", "lava_loucas", "bidets",
                     "mictorios", "banheiras", "valvulas_descarga"]:
        globals()[f'txt_{var_name}'].delete(0, tk.END)
    lbl_resultado.config(text="")
    lbl_detalhes.config(text="")

def exportar_pdf(diametro, perda_carga):
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return

    doc = SimpleDocTemplate(file_path, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Título
    elements.append(Paragraph(txt_af.textoaf+
        "\nResultados do Dimensionamento de Água Fria", styles['Title']))
    elements.append(Paragraph("\n", styles['Normal']))

    # Resultados principais
    data = [
        ["Diâmetro (mm)", f"{diametro:.2f}"],
        ["Perda de carga (m.c.a)", f"{perda_carga:.2f}"],
    ]

    # Adicionar dados de entrada
    for label, var_name in fields:
        value = globals()[f'txt_{var_name}'].get()
        data.append([label.strip(":"), value if value else "0"])

    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    elements.append(table)
    doc.build(elements)

    messagebox.showinfo("Exportação", "Resultados exportados com sucesso!")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Dimensionamento de Água Fria")
root.geometry("1024x800")

# Estilo moderno
style = ttk.Style()
style.theme_use("clam")

# Tema padrão
tema_atual = 'claro'
aplicar_tema_claro()

# Frame para entradas
frame_entradas = ttk.Frame(root, padding=20)
frame_entradas.pack(pady=10)

# Criando os campos de entrada
fields = [
    ("Quantidades de Vasos Sanitários:", "vasos"),
    ("Quantidades de Lavatórios:", "lavatorios"),
    ("Quantidades de Chuveiros:", "chuveiros"),
    ("Quantidades de Pias:", "pias"),
    ("Quantidades de Máquinas de Lavar:", "maquinas_lavar"),
    ("Quantidades de Tanques:", "tanques"),
    ("Quantidades de Lava-Louças:", "lava_loucas"),
    ("Quantidades de Bidês:", "bidets"),
    ("Quantidades de Mictórios:", "mictorios"),
    ("Quantidades de Banheiras:", "banheiras"),
    ("Quantidades de Vasos Sanitários com Válvulas de Descarga:", "valvulas_descarga"),
]

# Criando Labels e Entrys dinamicamente
for i, (label_text, var_name) in enumerate(fields):
    ttk.Label(frame_entradas, text=label_text).grid(row=i, column=0, padx=15, pady=10, sticky="w")
    entry = ttk.Entry(frame_entradas)
    entry.grid(row=i, column=1, padx=15, pady=10)
    globals()[f'txt_{var_name}'] = entry

# Frame para botões
frame_botoes = ttk.Frame(root, padding=20)
frame_botoes.pack(pady=10)

# Botão de calcular
btn_calcular = ttk.Button(frame_botoes, text="Calcular", command=lambda: calcular())
btn_calcular.grid(row=0, column=0, padx=5)

# Botão de limpar
btn_limpar = ttk.Button(frame_botoes, text="Limpar", command=limpar_campos)
btn_limpar.grid(row=0, column=1, padx=5)

# Botão de exportar PDF
btn_exportar_pdf = ttk.Button(frame_botoes, text="Salvar PDF", command=lambda: exportar_pdf(*calcular()))
btn_exportar_pdf.grid(row=0, column=2, padx=5)

# Botão para alternar tema
btn_alternar_tema = ttk.Button(frame_botoes, text="Alternar Tema", command=alternar_tema)
btn_alternar_tema.grid(row=0, column=3, padx=5)

# Ajustando o título para a seção de resultados
lbl_titulo_resultado = ttk.Label(root, text="Resultados:", font=("Arial", 14))
lbl_titulo_resultado.pack(pady=(20, 5))

# Label para mostrar o resultado
lbl_resultado = ttk.Label(root, text="")
lbl_resultado.pack(pady=5)

# Label para mostrar os detalhes do cálculo
lbl_detalhes = ttk.Label(root, text="")
lbl_detalhes.pack(pady=5)

# Iniciando o loop da interface
root.mainloop()