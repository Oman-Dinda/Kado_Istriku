import streamlit as st
import time

# 1. Konfigurasi Halaman (Biar ada dekorasi emoji hati di tab browser)
st.set_page_config(page_title="Happy Birthday Sayang! 🎉", page_icon="❤️", layout="centered")

# Judul Utama
st.title("💖 Selamat Ulang Tahun, Istriku Tercinta! 💖")
st.caption("Sebuah aplikasi kecil yang dibuat dengan penuh cinta oleh suamimu di sela jarak kita.")

st.divider()

# 2. Fitur Tombol Kejutan Utama
st.subheader("🎁 Ada titipan kado digital buat kamu, coba klik di bawah:")
if st.button("KLIK UNTUK MEMBUKA"):
    with st.spinner("Sedang mengirimkan doa dan cinta melewati jarak..."):
        time.sleep(2) # Efek loading biar penasaran
    
    # Efek visual bawaan Streamlit (bukan gambar file)
    st.balloons() # Efek balon terbang banyak! 🎉
    st.snow()     # Efek salju turun romantis! ❄️
    
    st.success("✨ BARAKALLAHU FII UMRIK! ✨")
    
    # Surat Cinta Jarak Jauh
    st.markdown("""
    ### Dear Sayangku,
    Selamat ulang tahun yaa Meskipun ulang tahun kali ini kita masii harus terhalang jarak 
    dan belum bisa bareng-barengg, semoga bahagia dan doa kaka tetep sampai ke adee yaa.
    
    Terima kasih ya sudah menjadi calon istri yang luar biasa hebat, penyabar, dan selalu 
    mendukung kaka di sini. Semoga di milad ini adee selalu sehat lahir dan batin yaaa, dilimpahkan 
    kebahagiaan terusss, dan Allah mudahkan segala urusan adeee yaaa, Aamiiinnn. 
    
    Tunggu ketemu yaaa, *I love you so sooo muchhhh* 🌙❤️
    """)

st.divider()

# 3. Fitur Interaktif: Kupon Kado Jarak Jauh
st.subheader("🎫 Pilih Hadiah Ulang Tahunmu!")
st.write("Meskipun lagi jauh nii bolehh kann ngasihh. Pilih kado di bawah ini adee, kaka mau ngasihh 😉")

kado_pilihan = st.selectbox(
    "Pilih kupon hadiahmu di sini:",
    [
        "Pilih salah satu...",
        "Transferan buat Check Out Kebutuhann 🛍️",
        "Paket Skincare Langsung Dikirim ke Rumah nii 💄",
        "Kaka GoFood-in Makanan Favorit Adee 🍕",
        "Skin Baru Buat Main Mobile Legend Barengg 🎮",
        "Janji Liburan Berdua setelah Kita Ketemu Nantii ✈️"
    ]
)

if kado_pilihan != "Pilihan salah satu...":
    st.write(f"### Kamu memilih: **{kado_pilihan}**")
    
    # Tombol klaim kado
    if st.button("Klaim Kupon Sekarang 🚀"):
        st.write("🎉 **Kupon Berhasil Diklaim!**")
        st.info("Silakan screenshot bagian ini, lalu kirim ke WhatsApp kaka untuk langsung dicairkan! Ditunggu ya adee! ❤️")
