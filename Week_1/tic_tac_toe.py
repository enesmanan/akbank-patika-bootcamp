import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk

def kazanma_durumu(tahta, simge, boyut):
    for i in range(boyut):
        for j in range(boyut - 2):
            if all(tahta[str(i * boyut + j + k + 1)] == simge for k in range(3)):
                return True
            if all(tahta[str((j + k) * boyut + i + 1)] == simge for k in range(3)):
                return True
    for i in range(boyut - 2):
        for j in range(boyut - 2):
            if all(tahta[str((i + k) * boyut + j + k + 1)] == simge for k in range(3)):
                return True
            if all(tahta[str((i + k) * boyut + j + 3 - k)] == simge for k in range(3)):
                return True
    return False

class TicTacToe:
    def __init__(self, root, boyut, bg_path):
        self.root = root
        self.boyut = boyut
        self.tahta = {str(i): '' for i in range(1, boyut * boyut + 1)}
        self.sembol = 'X'
        self.buttons = []
        
        self.bg_image = ImageTk.PhotoImage(Image.open(bg_path))
        
        self.canvas = tk.Canvas(root, width=self.bg_image.width(), height=self.bg_image.height())
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.create_widgets()

    def create_widgets(self):
        for i in range(self.boyut):
            row = []
            for j in range(self.boyut):
                button = tk.Button(self.root, text='', font=('Arial', 30, 'bold'), width=5, height=2,
                                   command=lambda i=i, j=j: self.cell_click(i, j))
                self.canvas.create_window(j * 135 + 80, i * 135 + 200, window=button)
                row.append(button)
            self.buttons.append(row)

    def cell_click(self, i, j):
        index = i * self.boyut + j + 1
        if self.tahta[str(index)] == '':
            self.tahta[str(index)] = self.sembol
            self.buttons[i][j].config(text=self.sembol)
            if self.kazanma_durumu(self.sembol):
                messagebox.showinfo("Oyun Bitti", f"{self.sembol} kazandı!")
                self.root.after(2000, self.root.destroy)
            elif all(self.tahta[str(i)] != '' for i in range(1, self.boyut * self.boyut + 1)):
                messagebox.showinfo("Oyun Bitti", "Berabere!")
                self.root.after(2000, self.root.destroy)
            else:
                self.sembol = 'O' if self.sembol == 'X' else 'X'
            self.buttons[i][j].config(fg='red' if self.sembol == 'X' else 'blue')
        else:
            messagebox.showwarning("Geçersiz Hamle", "Bu hücre zaten dolu!")

    def kazanma_durumu(self, simge):
        return kazanma_durumu(self.tahta, simge, self.boyut)

def main():
    root = tk.Tk()
    root.title("Tic Tac Toe")
    root.geometry("1350x800")
    
    boyut = simpledialog.askinteger("Tahta Boyutu", "Tahtanın boyutunu giriniz (3 veya daha büyük bir sayı):",
                                    initialvalue=3, minvalue=3)
    if boyut is None:
        return  
    
    bg_path = "arkaplan.png"

    app = TicTacToe(root, boyut, bg_path)
    root.mainloop()

if __name__ == "__main__":
    main()
