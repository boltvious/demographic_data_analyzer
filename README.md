# Demographic Data Analyzer

Solusi proyek freeCodeCamp *Data Analysis with Python* — Demographic Data Analyzer.

## Deskripsi

Proyek ini menganalisis dataset demografi dari database Sensus Penduduk tahun 1994 menggunakan library **Pandas**. Terdapat 9 pertanyaan analisis yang harus dijawab dari dataset `adult.data.csv`.

## Struktur Project

| File | Keterangan |
|------|-----------|
| `demographic_data_analyzer.py` | Implementasi fungsi `calculate_demographic_data()` menggunakan Pandas |
| `adult.data.csv` | Dataset Sensus Penduduk 1994 |
| `main.py` | Entry point: menjalankan analisis data dan unit test |
| `test_module.py` | Unit test (unittest) untuk memvalidasi hasil analisis |
| `requirements.txt` | Dependensi (`pandas`) |

## Cara Pakai

```bash
# Install dependensi (Pandas)
pip install -r requirements.txt

# Jalankan program + unit test
python main.py
```

## 9 Pertanyaan Analisis

1. Berapa banyak orang dari masing-masing ras (race) dalam dataset ini?
2. Berapa rata-rata umur laki-laki?
3. Berapa persentase orang yang memiliki gelar Bachelor's?
4. Berapa persentase orang dengan pendidikan tinggi (Bachelors, Masters, Doctorate) yang berpenghasilan >50K?
5. Berapa persentase orang tanpa pendidikan tinggi yang berpenghasilan >50K?
6. Berapa jam kerja minimum seseorang per minggu?
7. Berapa persentase orang yang bekerja di jam minimum tersebut tetapi berpenghasilan >50K?
8. Negara mana yang memiliki persentase tertinggi orang berpenghasilan >50K?
9. Apa pekerjaan (occupation) paling populer bagi mereka yang berpenghasilan >50K di India?

## Contoh Output

```text
Number of each race:
 race
White                 27816
Black                  3124
Asian-Pac-Islander     1039
Amer-Indian-Eskimo      311
Other                   271
Name: count, dtype: int64
Average age of men: 39.4
Percentage with Bachelors degrees: 16.4%
Percentage with higher education that earn >50K: 46.5%
Percentage without higher education that earn >50K: 17.4%
Min work time: 1 hours/week
Percentage of rich among those who work fewest hours: 10.0%
Country with highest percentage of rich: Iran
Highest percentage of rich people in country: 41.9%
Top occupations in India: Prof-specialty
```

## Hasil Test

```text
Ran 1 test in 0.106s

OK
```
