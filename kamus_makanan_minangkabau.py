kamus = {
    "Rendang": {
        "arti": "Rendang",
        "deskripsi": "Masakan daging berbumbu rempah yang dimasak hingga kering.",
        "contoh": [
            "Rendang daging jadi makanan utama.",
            "Rendang ayam cocok untuk bekal."
        ]
    },
    "Gulai": {
        "arti": "Gulai",
        "deskripsi": "Gulai daging khas Minang dengan bumbu kuat.",
        "contoh": [
            "Gulai paku",
            "Gulai cubadak"
        ]
    }
}

def cari_kata(kata):
    kata_cap = kata.strip().title()
    if not kata_cap:
        return "Masukkan tidak boleh kosong."

    if kata_cap in kamus:
        data = kamus[kata_cap]
        hasil = f"<h2>{kata_cap}</h2>"
        hasil += f"<p><strong>Arti:</strong> {data['arti']}</p>"
        hasil += f"<p><strong>Deskripsi:</strong> {data['deskripsi']}</p>"
        hasil += "<p><strong>Contoh Penggunaan:</strong></p><ul>"
        for contoh in data["contoh"]:
            hasil += f"<li>{contoh}</li>"
        hasil += "</ul>"
        return hasil
    else:
        return "Makanan tidak ditemukan di kamus."
