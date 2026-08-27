import streamlit as st

def kelime_bul(dosya_adi, harfler):
    aranan_harfler = set(harfler.lower())
    bulunanlar = []
    with open(dosya_adi, 'r', encoding='utf-8') as f:
        for kelime in f:
            kelime = kelime.strip().lower()
            if aranan_harfler.issubset(set(kelime)):
                bulunanlar.append(kelime)
    return bulunanlar

st.title("Kelime Bulucu 🕵️‍♀️")
harfler = st.text_input("Aranacak harfleri bitişik şekilde girin:")

if harfler:
    # Dosya yolu düzeltildi
    sonuclar = kelime_bul("KelimeBulucu/temiz_kelimeler.txt", harfler)
    
    # Kelimeler en kısadan en uzuna sıralanıyor
    sonuclar.sort(key=len)
    
    st.success(f"Tam {len(sonuclar)} adet kelime bulundu!")
    
    # Kutular yerine aralarına virgül koyarak düz metin halinde yazdırıyoruz
    st.write(", ".join(sonuclar))
