# 🎮 Python FPS Mini Game

Welcome to **Python FPS Mini Game**! Ini adalah Project iseng game tembak-tembakan sederhana dengan perspective orang pertama (FPS) yang dibuat menggunakan [Ursina Engine](https://www.ursinaengine.org/).

---

## ✨ Fitur Utama
- **First Person Controller**: Gerakan normal WASD dan lompat.
- **Dua Mode Musuh**:
  - Musuh Diam
  - Musuh Bergerak (Strafing)
- **Sistem Menembak**: Tembak musuh dengan klik kiri.
- **Obstacle & Platform**: Arena penuh rintangan dan platform bertingkat.
- **Menu Start & Finish**: Pilih mode musuh dan ulangi permainan.
- **Pause Menu**: Tekan `ESC` untuk jeda dan keluar.
- **Visual 3D Tanpa Texture Pack**

---

## 🕹️ Kontrol
| Tombol         | Fungsi                |
| -------------- | --------------------- |
| W, A, S, D     | Bergerak              |
| Mouse          | Mengarahkan kamera    |
| Shift          | Jalan pelan           |
| Ctrl           | Jongkok               |
| Klik Kiri      | Menembak              |
| ESC            | Pause/Keluar          |

---

## 🚀 Cara Instalasi & Menjalankan
1. **Clone repo ini**
   ```bash
   git clone https://github.com/Cryztalzz/Python-Game
   cd Game_UI
   ```
2. **Install dependensi**
   ```bash
   pip install -r requirements.txt
   ```
3. **Jalankan game**
   ```bash
   python main.py
   ```

> **Catatan:** Pastikan Python 3.8+ dan [Ursina](https://www.ursinaengine.org/) sudah terinstall.

---

## 🗂️ Struktur Project
```mermaid
---
graph TD;
  A[main.py] -->|import| B[enemy.py]
  A -->|import| C[obstacle.py]
  A -->|import| D[platform_utils.py]
  A -->|import| E[ui.py]
  A -->|import| F[shooting.py]
  A -->|load| G[resources/environments/sky.exr]
  subgraph Resources
    G
  end
  subgraph Utils
    B
    C
    D
    F
    E
  end
  A --> H[requirements.txt]
```

---

## 🏞️ Aset & Kredit
- **Sky Texture**: `resources/environments/sky.exr`
- **Engine**: [Ursina Engine](https://www.ursinaengine.org/)

---

## 📄 Lisensi
    -

---

> Alz was here