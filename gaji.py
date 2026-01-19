import pandas as pd

# Data Awal
data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

print("--- DataFrame Awal ---")
print(df)
print("\n")

# ---------------------------------------------------------
# Pertanyaan 1: Loop for & Lambda untuk kenaikan 5%
# ---------------------------------------------------------
naik_5_persen = lambda x: x * 1.05

# Menggunakan iterrows untuk loop (sesuai instruksi menggunakan loop)
for index, row in df.iterrows():
    gaji_baru = naik_5_persen(row['Gaji'])
    df.at[index, 'Gaji'] = gaji_baru

# ---------------------------------------------------------
# Pertanyaan 2: Tampilkan DataFrame & Ringkasan
# ---------------------------------------------------------
print("--- Hasil Pertanyaan 1 & 2 (Kenaikan 5% Semua Karyawan) ---")
print(df)
print("Ringkasan: Semua karyawan telah menerima kenaikan gaji sebesar 5%.")
print("\n")

# ---------------------------------------------------------
# Pertanyaan 3: Evaluasi Usia > 30 (Loop & Lambda +2%)
# ---------------------------------------------------------
naik_2_persen = lambda x: x * 1.02

for index, row in df.iterrows():
    # Evaluasi jika usia di atas 30 (Strictly > 30, jadi 30 tidak termasuk)
    if row['Usia'] > 30:
        gaji_tambahan = naik_2_persen(row['Gaji'])
        df.at[index, 'Gaji'] = gaji_tambahan

# ---------------------------------------------------------
# Pertanyaan 4: Tampilkan Hasil Akhir & Ringkasan
# ---------------------------------------------------------
print("--- Hasil Pertanyaan 3 & 4 (Tambahan 2% untuk Usia > 30) ---")
print(df)
print("Ringkasan: Karyawan dengan usia di atas 30 tahun (Jane) mendapatkan tambahan 2%.")