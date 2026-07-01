import streamlit as st
import time

# 1. Konfigurasi Halaman (Biar ada dekorasi emoji hati di tab browser)
st.set_page_config(page_title="Happy Birthday Sayang! 🎉", page_icon="❤️", layout="centered")

# Custom tampilan sedikit biar teksnya rapi
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
    Selamat ulang tahun ya! Meskipun ulang tahun kali ini kita harus terhalang jarak 
    dan belum bisa tiup lilin bareng, semoga esensi bahagia dan doaku tetep sampai ke kamu.
    
    Terima kasih ya sudah menjadi istri yang luar biasa hebat, penyabar, dan selalu 
    mendukung aku di sini. Semoga di usia yang baru ini kamu selalu sehat, dilimpahkan 
    kebahagiaan, dan Allah mudahkan segala urusanmu. 
    
    Tunggu aku pulang ya, *I love you to the moon and back!* 🌙❤️
    """)

st.divider()

# 3. Fitur Interaktif: Kupon Kado Jarak Jauh
st.subheader("🎫 Pilih Hadiah Ulang Tahunmu!")
st.write("Meskipun lagi LDR, hadiah tetep jalan terus dong. Silakan pilih salah satu kado di bawah ini, suamimu siap mengabulkannya! 😉")

kado_pilihan = st.selectbox(
    "Pilih kupon hadiahmu di sini:",
    [
        "Pilih salah satu...",
        "Transferan Dana Kaget buat Check Out Shopee / Tokopedia 🛍️",
        "Paket Skincare / Kosmetik Pilihanmu yang Langsung Dikirim ke Rumah 💄",
        "Voucher Makan Malam Virtual (Aku GoFood-in Makanan Favoritmu) 🍕",
        "Janji Liburan Berdua setelah Kita Ketemu Nanti ✈️"
    ]
)

if kado_pilihan != "Pilih salah satu...":
    st.write(f"### Kamu memilih: **{kado_pilihan}**")
    
    # Tombol klaim kado
    if st.button("Klaim Kupon Sekarang 🚀"):
        st.write("🎉 **Kupon Berhasil Diklaim!**")
        st.info("Silakan screenshoot bagian ini, lalu kirim ke WhatsApp suamimu untuk langsung dicairkan! Ditunggu ya! ❤️")