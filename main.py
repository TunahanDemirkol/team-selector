import random
import tkinter as tk
from tkinter import ttk
import time

# 2023-2024 sezonu güncel takım verileri
TEAMS = {
    "Turkey": [
        "Galatasaray", "Fenerbahçe", "Beşiktaş", "Trabzonspor",
        "Adana Demirspor", "Antalyaspor", "Kasımpaşa", "Kayserispor",
        "Alanyaspor", "Başakşehir", "Konyaspor", "Gaziantep FK",
        "Sivasspor", "Hatayspor", "Pendikspor", "Ankaragücü",
        "İstanbulspor", "Samsunspor", "Rizespor", "Karagümrük"
    ],
    "England": [
        "Manchester City", "Arsenal", "Manchester United", "Liverpool",
        "Chelsea", "Tottenham", "Newcastle", "Brighton",
        "Aston Villa", "Brentford", "Crystal Palace", "Fulham",
        "West Ham", "Nottingham Forest", "Everton", "Luton Town",
        "Burnley", "Sheffield United", "Bournemouth", "Wolves"
    ],
    "France": [
        "PSG", "Marseille", "Lens", "Monaco",
        "Lille", "Rennes", "Lyon", "Nice",
        "Reims", "Strasbourg", "Toulouse", "Montpellier",
        "Clermont", "Nantes", "Metz", "Le Havre",
        "Lorient", "Brest", "PSG", "Reims"
    ],
    "Germany": [
        "Bayern Munich", "Borussia Dortmund", "RB Leipzig", "Union Berlin",
        "Freiburg", "Bayer Leverkusen", "Eintracht Frankfurt", "Wolfsburg",
        "Mainz 05", "Borussia Mönchengladbach", "Werder Bremen", "Augsburg",
        "Hoffenheim", "VfL Bochum", "FC Köln", "Heidenheim",
        "Stuttgart", "Darmstadt", "VfL Bochum", "RB Leipzig"
    ]
}

def select_teams():
    # İki farklı lig seç
    selected_leagues = random.sample(list(TEAMS.keys()), 2)
    
    # Her ligden birer takım seç
    team1 = random.choice(TEAMS[selected_leagues[0]])
    team2 = random.choice(TEAMS[selected_leagues[1]])
    
    return team1, team2, selected_leagues

class FootballTeamSelector:
    def __init__(self, root):
        self.root = root
        self.root.title("Futbol Takımı Seçici")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")  # Açık gri arka plan
        
        # Stil tanımlamaları
        style = ttk.Style()
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TButton",
                       padding=10,
                       font=('Helvetica', 12))
        style.configure("Title.TLabel",
                       font=('Helvetica', 24, 'bold'),
                       background="#f0f0f0",
                       foreground="#2c3e50")
        style.configure("Team.TLabel",
                       font=('Helvetica', 14),
                       background="#ffffff",
                       padding=15)
        
        # Ana çerçeve
        main_frame = ttk.Frame(root, padding="30", style="TFrame")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        main_frame.grid_columnconfigure(0, weight=1)
        
        # Başlık
        title_label = ttk.Label(main_frame,
                               text="Rastgele Futbol Takımı Seçici",
                               style="Title.TLabel")
        title_label.grid(row=0, column=0, pady=(0, 30))
        
        # Takım gösterme çerçevesi
        teams_frame = ttk.Frame(main_frame, style="TFrame")
        teams_frame.grid(row=2, column=0, pady=20)
        teams_frame.grid_columnconfigure(0, weight=1)
        
        # Takım etiketleri için beyaz arka planlı çerçeveler
        self.team1_frame = tk.Frame(teams_frame,
                                  bg="white",
                                  relief="raised",
                                  bd=0,
                                  highlightthickness=1,
                                  highlightbackground="#dcdcdc")
        self.team1_frame.grid(row=0, column=0, pady=5, sticky="ew")
        
        self.team2_frame = tk.Frame(teams_frame,
                                  bg="white",
                                  relief="raised",
                                  bd=0,
                                  highlightthickness=1,
                                  highlightbackground="#dcdcdc")
        self.team2_frame.grid(row=1, column=0, pady=5, sticky="ew")
        
        # Takım etiketleri
        self.team1_label = ttk.Label(self.team1_frame,
                                   text="",
                                   style="Team.TLabel")
        self.team1_label.pack(fill="x")
        
        self.team2_label = ttk.Label(self.team2_frame,
                                   text="",
                                   style="Team.TLabel")
        self.team2_label.pack(fill="x")
        
        # Butonlar için çerçeve
        button_frame = ttk.Frame(main_frame, style="TFrame")
        button_frame.grid(row=3, column=0, pady=30)
        
        # Seçim butonu
        self.select_button = ttk.Button(button_frame,
                                      text="🎲 Takımları Seç",
                                      command=self.select_and_display,
                                      style="TButton")
        self.select_button.grid(row=0, column=0, padx=10)
        
        # Çıkış butonu
        exit_button = ttk.Button(button_frame,
                               text="✖ Çıkış",
                               command=root.quit,
                               style="TButton")
        exit_button.grid(row=0, column=1, padx=10)
        
        # Pencereyi ortala
        self.center_window()
        
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def select_and_display(self):
        # Buton devre dışı bırakılır
        self.select_button.configure(state='disabled')
        self.team1_label.configure(text="Takımlar seçiliyor...")
        self.team2_label.configure(text="")
        self.root.update()
        
        # Animasyon efekti için kısa bekleme
        time.sleep(0.5)
        
        # Takımları seç
        team1, team2, leagues = select_teams()
        
        # Sonuçları göster
        self.team1_label.configure(text=f"🏆  {team1} ({leagues[0]})")
        self.team2_label.configure(text=f"🏆  {team2} ({leagues[1]})")
        
        # Buton tekrar aktif edilir
        self.select_button.configure(state='normal')

def main():
    root = tk.Tk()
    app = FootballTeamSelector(root)
    root.mainloop()

if __name__ == "__main__":
    main()
