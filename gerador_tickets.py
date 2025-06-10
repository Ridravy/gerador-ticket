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

def colar_texto(widget):
    try:
        texto = root.clipboard_get()
        if isinstance(widget, ctk.CTkTextbox):
            widget.insert(ctk.INSERT, texto)
        else:
            widget.insert(0, texto)
    except:
        pass

def copiar_resultado():
    try:
        texto = text_resultado.get("1.0", ctk.END).strip()
        root.clipboard_clear()
        root.clipboard_append(texto)
    except:
        pass

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
BUTTON_STYLE = {"fg_color": "#8b0000", "hover_color": "#ff4444"}

# N° do Ticket
ctk.CTkLabel(main_frame, text="N° DO TICKET:", **LABEL_STYLE).pack(pady=(10, 0))
ticket_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
ticket_frame.pack()
entry_numero = ctk.CTkEntry(ticket_frame, width=WIDGET_WIDTH - 40, height=ENTRY_HEIGHT, placeholder_text="Número do Ticket")
entry_numero.pack(side=ctk.LEFT)
ctk.CTkButton(ticket_frame, text="📋", width=30, command=lambda: colar_texto(entry_numero), **BUTTON_STYLE).pack(padx=(5, 0), side=ctk.LEFT)

# Descrição
ctk.CTkLabel(main_frame, text="DESCRIÇÃO:", **LABEL_STYLE).pack(pady=(10, 0))
desc_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
desc_frame.pack()
text_descricao = ctk.CTkTextbox(desc_frame, height=TEXTBOX_HEIGHT, width=WIDGET_WIDTH - 40)
text_descricao.pack(side=ctk.LEFT)
ctk.CTkButton(desc_frame, text="📋", width=30, command=lambda: colar_texto(text_descricao), **BUTTON_STYLE).pack(padx=(5, 0), side=ctk.LEFT)

# Comentários
ctk.CTkLabel(main_frame, text="COMENTÁRIOS:", **LABEL_STYLE).pack(pady=(10, 0))
coment_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
coment_frame.pack()
text_comentarios = ctk.CTkTextbox(coment_frame, height=TEXTBOX_HEIGHT, width=WIDGET_WIDTH - 40)
text_comentarios.pack(side=ctk.LEFT)
ctk.CTkButton(coment_frame, text="📋", width=30, command=lambda: colar_texto(text_comentarios), **BUTTON_STYLE).pack(padx=(5, 0), side=ctk.LEFT)

# Resolução
ctk.CTkLabel(main_frame, text="RESOLUÇÃO:", **LABEL_STYLE).pack(pady=(10, 0))
resol_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
resol_frame.pack()
text_resolucao = ctk.CTkTextbox(resol_frame, height=TEXTBOX_HEIGHT, width=WIDGET_WIDTH - 40)
text_resolucao.pack(side=ctk.LEFT)
ctk.CTkButton(resol_frame, text="📋", width=30, command=lambda: colar_texto(text_resolucao), **BUTTON_STYLE).pack(padx=(5, 0), side=ctk.LEFT)

# Situação
ctk.CTkLabel(main_frame, text="SITUAÇÃO:", **LABEL_STYLE).pack(pady=(10, 0))
status_options = ["COMENTADO", "ENCAMINHADO", "ENCERRADO", "SUSPENSO"]
combo_situacao = ctk.CTkComboBox(main_frame, values=status_options, width=WIDGET_WIDTH)
combo_situacao.pack()
combo_situacao.set("ENCERRADO")

# Botões
button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
button_frame.pack(pady=20)

btn_gerar = ctk.CTkButton(
    button_frame,
    text="GERAR TICKET",
    command=gerar_ticket,
    height=40,
    width=170,
    font=ctk.CTkFont(size=15, weight="bold"),
    **BUTTON_STYLE
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

# Resultado
ctk.CTkLabel(main_frame, text="RESULTADO:", **LABEL_STYLE).pack()
resultado_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
resultado_frame.pack()
text_resultado = ctk.CTkTextbox(resultado_frame, height=150, width=WIDGET_WIDTH - 40, state=ctk.DISABLED)
text_resultado.pack(side=ctk.LEFT)
ctk.CTkButton(resultado_frame, text="📤", width=30, command=copiar_resultado, **BUTTON_STYLE).pack(padx=(5, 0), side=ctk.LEFT)

# Assinatura
ctk.CTkLabel(
    root,
    text="Version 1.2.0 by Ridravy",
    font=ctk.CTkFont(size=10),
    text_color="#555"
).pack(pady=5)

root.mainloop()
