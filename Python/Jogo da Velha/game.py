import tkinter as tk
import random

class JogoDaVelha:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo da Velha")
        self.master.geometry("300x300")
        
        self.botoes = []
        for i in range(3):
            linha = []
            for j in range(3):
                botao = tk.Button(self.master, width=10, height=5, font=("Arial", 20), command=lambda row=i, col=j: self.jogada(row, col))
                botao.grid(row=i, column=j)
                linha.append(botao)
            self.botoes.append(linha)
        
        self.tabuleiro = [[" " for j in range(3)] for i in range(3)]
        self.turno = "X"
        
    def jogada(self, row, col):
        if self.tabuleiro[row][col] == " ":
            self.tabuleiro[row][col] = self.turno
            self.botoes[row][col].configure(text=self.turno)
            if self.ganhou():
                tk.messagebox.showinfo("Fim de jogo", f"O jogador {self.turno} ganhou!")
                self.master.destroy()
            elif self.empatou():
                tk.messagebox.showinfo("Fim de jogo", "Empate!")
                self.master.destroy()
            else:
                self.turno = "O"
                self.jogada_do_pc()
    
    def jogada_do_pc(self):
        vazios = [(i, j) for i in range(3) for j in range(3) if self.tabuleiro[i][j] == " "]
        if vazios:
            jogada = random.choice(vazios)
            self.tabuleiro[jogada[0]][jogada[1]] = self.turno
            self.botoes[jogada[0]][jogada[1]].configure(text=self.turno)
            if self.ganhou():
                tk.messagebox.showinfo("Fim de jogo", f"O jogador {self.turno} ganhou!")
                self.master.destroy()
            elif self.empatou():
                tk.messagebox.showinfo("Fim de jogo", "Empate!")
                self.master.destroy()
            else:
                self.turno = "X"
    
    def ganhou(self):
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] != " ":
                return True
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] != " ":
                return True
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != " ":
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != " ":
            return True
        return False
    
        def empatou(self):
            for i in range(3):
                for j in range(3):
                    if self.tabuleiro[i][j] == " ":
                        return False
        return True
