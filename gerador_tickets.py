import customtkinter as ctk

def gerar_ticket():
    ticket_num = entry_numero.get()
    descricao = text_descricao.get("1.0", ctk.END).strip()
    comentarios = text_comentarios.get("1.0", ctk.END).strip()
    resolucao = text_resolucao.get("1.0", ctk.END).strip()
    situacao = combo_situacao.get()

    icones = {
        "COMENTADO": "💬",
        "ENCAMINHADO": "⤵️",
        "ENCERRADO": "✅",
        "SUSPENSO": "⚠️"
    }
    icone = icones.get(situacao, "")
    
    texto_final = f"Ticket n°: {ticket_num}\n\n"
    texto_final += f"Descrição:\n- {descricao}\n\n"
    if comentarios:
        texto_final += f"Comentários:\n- {comentarios}\n\n"
    texto_final += f"Resolução:\n- {resolucao}\n\n"
    texto_final += f"[{situacao}] {icone}"

    text_resultado.configure(state=ctk.NORMAL)
    text_resultado.delete("1.0", ctk.END)
    text_resultado.insert("1.0", texto_final)
    text_resultado.configure(state=ctk.DISABLED)

def limpar_campos():
    entry_numero.delete(0, ctk.END)
    text_descricao.delete("1.0", ctk.END)
    text_comentarios.delete("1.0", ctk.END)
    text_resolucao.delete("1.0", ctk.END)
    combo_situacao.set("ENCERRADO")
    text_resultado.configure(state=ctk.NORMAL)
    text_resultado.delete("1.0", ctk.END)
    text_resultado.configure(state=ctk.DISABLED)

# Tema e estilo
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("RyTemplate - Gerador de Tickets")
root.geometry("600x870")
root.configure(fg_color="#121212")  # fundo preto

main_frame = ctk.CTkFrame(root, fg_color="#1e1e1e")
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

WIDGET_WIDTH = 380
TEXTBOX_HEIGHT = 90
ENTRY_HEIGHT = 30
LABEL_STYLE = {"text_color": "#ff4444", "font": ctk.CTkFont(weight="bold", size=14)}

ctk.CTkLabel(main_frame, text="N° DO TICKET:", **LABEL_STYLE).pack(pady=(10, 0))
entry_numero = ctk.CTkEntry(main_frame, width=WIDGET_WIDTH, height=ENTRY_HEIGHT, placeholder_text="Número do Ticket")
entry_numero.pack()

ctk.CTkLabel(main_frame, text="DESCRIÇÃO:", **LABEL_STYLE).pack(pady=(10, 0))
text_descricao = ctk.CTkTextbox(main_frame, height=TEXTBOX_HEIGHT, width=WIDGET_WIDTH)
text_descricao.pack()

ctk.CTkLabel(main_frame, text="COMENTÁRIOS:", **LABEL_STYLE).pack(pady=(10, 0))
text_comentarios = ctk.CTkTextbox(main_frame, height=TEXTBOX_HEIGHT, width=WIDGET_WIDTH)
text_comentarios.pack()

ctk.CTkLabel(main_frame, text="RESOLUÇÃO:", **LABEL_STYLE).pack(pady=(10, 0))
text_resolucao = ctk.CTkTextbox(main_frame, height=TEXTBOX_HEIGHT, width=WIDGET_WIDTH)
text_resolucao.pack()

ctk.CTkLabel(main_frame, text="SITUAÇÃO:", **LABEL_STYLE).pack(pady=(10, 0))
status_options = ["COMENTADO", "ENCAMINHADO", "ENCERRADO", "SUSPENSO"]
combo_situacao = ctk.CTkComboBox(main_frame, values=status_options, width=WIDGET_WIDTH)
combo_situacao.pack()
combo_situacao.set("ENCERRADO")

button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
button_frame.pack(pady=20)

btn_gerar = ctk.CTkButton(
    button_frame,
    text="GERAR TICKET",
    command=gerar_ticket,
    height=40,
    width=170,
    font=ctk.CTkFont(size=15, weight="bold"),
    fg_color="#8b0000",
    hover_color="#ff4444"
)
btn_gerar.pack(side=ctk.LEFT, padx=10)

btn_limpar = ctk.CTkButton(
    button_frame,
    text="LIMPAR TUDO",
    command=limpar_campos,
    height=40,
    width=170,
    font=ctk.CTkFont(size=15, weight="bold"),
    fg_color="#444444",
    hover_color="#777777"
)
btn_limpar.pack(side=ctk.RIGHT, padx=10)

ctk.CTkLabel(main_frame, text="RESULTADO:", **LABEL_STYLE).pack()
text_resultado = ctk.CTkTextbox(main_frame, height=150, width=WIDGET_WIDTH, state=ctk.DISABLED)
text_resultado.pack()

# Assinatura
ctk.CTkLabel(
    root,
    text="Version 1.1.2 by Ridravy",
    font=ctk.CTkFont(size=10),
    text_color="#555"
).pack(pady=5)

root.mainloop()
