import tkinter as tk
from tkinter import simpledialog, filedialog, font


class ShoppingListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Compras")

        # Configurações de cores
        self.escuro_bg = "#2e2e2e"
        self.escuro_fg = "#ffffff"

        # Configurar a interface para o modo escuro
        self.root.config(bg=self.escuro_bg)

        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=300, bg=self.escuro_bg, fg=self.escuro_fg)
        self.listbox.pack(pady=20)

        self.entry = tk.Entry(root, width=300, bg=self.escuro_bg, fg=self.escuro_fg)
        self.entry.pack(pady=50)

        button_frame = tk.Frame(root, bg=self.escuro_bg)
        button_frame.pack(pady=10)

        # Criando botões
        self.add_button = tk.Button(button_frame, text="Adicionar", command=self.adicionar_item, width=20, bg=self.escuro_bg, fg=self.escuro_fg)
        self.add_button.pack(side=tk.LEFT, padx=2)

        self.edit_button = tk.Button(button_frame, text="Editar", command=self.editar_item, width=20, bg=self.escuro_bg, fg=self.escuro_fg)
        self.edit_button.pack(side=tk.LEFT, padx=2)

        self.delete_button = tk.Button(button_frame, text="Excluir", command=self.excluir_item, width=20, bg=self.escuro_bg, fg=self.escuro_fg)
        self.delete_button.pack(side=tk.LEFT, padx=2)

        self.mark_button = tk.Button(button_frame, text="Marcar como Comprado", command=self.marcar_item, width=20, bg=self.escuro_bg, fg=self.escuro_fg)
        self.mark_button.pack(side=tk.LEFT, padx=2)

        self.export_button = tk.Button(button_frame, text="Exportar Lista", command=self.exportar_lista, width=20, bg=self.escuro_bg, fg=self.escuro_fg)
        self.export_button.pack(side=tk.LEFT, padx=2)

        self.help_button = tk.Button(button_frame, text="?", command=self.mostrar_ajuda, width=5, bg=self.escuro_bg, fg=self.escuro_fg)
        self.help_button.pack(side=tk.LEFT, padx=2)

        self.root.bind("<Return>", self.adicionar_item_evento)
        self.root.bind("<F2>", self.editar_item_evento)
        self.root.bind("<Delete>", self.excluir_item_evento)
        self.root.bind("<Control-s>", self.exportar_lista_evento)

    def adicionar_item(self):
        item = self.entry.get()
        if item:
            self.listbox.insert(tk.END, item)
            self.entry.delete(0, tk.END)

    def adicionar_item_evento(self, event):
        self.adicionar_item()

    def editar_item(self):
        selected_item_index = self.listbox.curselection()
        if selected_item_index:
            current_item = self.listbox.get(selected_item_index)
            new_item = simpledialog.askstring("Editar", "Edite o item:", initialvalue=current_item)
            if new_item:
                self.listbox.delete(selected_item_index)
                self.listbox.insert(selected_item_index, new_item)

    def editar_item_evento(self, event):
        self.editar_item()

    def excluir_item(self):
        selected_item_index = self.listbox.curselection()
        if selected_item_index:
            self.listbox.delete(selected_item_index)

    def excluir_item_evento(self, event):
        self.excluir_item()

    def marcar_item(self):
        selected_item_index = self.listbox.curselection()
        if selected_item_index:
            item = self.listbox.get(selected_item_index)
            if "(Comprado)" not in item:
                self.listbox.delete(selected_item_index)
                self.listbox.insert(selected_item_index, item + " (Comprado)")

    def exportar_lista(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                for item in self.listbox.get(0, tk.END):
                    file.write(item + "\n")

    def exportar_lista_evento(self, event):
        self.exportar_lista()

    def mostrar_ajuda(self):
        ajuda_window = tk.Toplevel(self.root)
        ajuda_window.title("Ajuda")
        ajuda_window.config(bg=self.escuro_bg)
        ajuda_window.geometry("400x300")

        text_widget = tk.Text(ajuda_window, bg=self.escuro_bg, fg=self.escuro_fg, wrap=tk.WORD)
        text_widget.pack(expand=True, fill=tk.BOTH)

        bold_font = font.Font(weight="bold")
        text_widget.tag_configure("bold", font=bold_font)

        text_widget.insert(tk.END, "Atalhos:\n", "bold")
        text_widget.insert(tk.END, "Enter - Adicionar item à lista\n")
        text_widget.insert(tk.END, "F2 - Editar item selecionado\n")
        text_widget.insert(tk.END, "Delete - Excluir item selecionado\n")
        text_widget.insert(tk.END, "Ctrl + S - Exportar lista para um arquivo\n")
        text_widget.insert(tk.END, "\nFunções dos Botões:\n", "bold")
        text_widget.insert(tk.END, "Adicionar - Adiciona o item do campo de entrada à lista.\n")
        text_widget.insert(tk.END, "Editar - Edita o item selecionado na lista.\n")
        text_widget.insert(tk.END, "Excluir - Remove o item selecionado da lista.\n")
        text_widget.insert(tk.END, "Marcar como Comprado - Marca o item selecionado como comprado.\n")
        text_widget.insert(tk.END, "Exportar Lista - Salva a lista em um arquivo de texto.")

        text_widget.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("820x400")
    app = ShoppingListApp(root)
    root.mainloop()
