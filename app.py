
import streamlit as st
import pandas as pd

# Konfigurasi Halaman
st.set_page_config(
    page_title="Dapur Nusantara Logistics",
    page_icon="🚚",
    layout="wide"
)

# Custom CSS / Styling
st.markdown("""
    <style>
    .main-header {
        font-size: 28px;
        font-weight: bold;
        color: #FF4B4B;
        text-align: center;
        margin-bottom: 10px;
    }
    .card {
        padding: 20px;
        border-radius: 12px;
        background-color: #f8f9fa;
        border: 2px solid #e9ecef;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Judul Utama Aplikasi
st.markdown('<p class="main-header">🚚 Sistem Optimasi Rute & Logistik - Dapur Nusantara</p>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Aplikasi cerdas berbasis Berpikir Komputasional (Pilar Algoritma) untuk alokasi kurir katering kilat.</p>", unsafe_allow_html=True)
st.markdown("---")

# Layout Kolom (Form Input & Hasil)
col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.subheader("📥 Input Data Pesanan Baru")
    with st.form("form_pesanan"):
        id_pesanan = st.text_input("ID Pesanan", "P-01")
        jenis_makanan = st.selectbox("Jenis Makanan", ["Sensitif Es/Suhu (Es/Lumer)", "Makanan Hangat / Biasa"])
        lokasi = st.selectbox("Kondisi Lokasi Tujuan", ["Normal", "Area Macet Parah"])
        volume = st.selectbox("Volume / Jumlah Pesanan", ["Kecil/Sedang", "Sangat Besar / Banyak"])
        
        submitted = st.form_submit_button("🔍 Hitung Alokasi Kurir")

with col2:
    st.subheader("📊 Hasil Rekomendasi Alokasi")
    
    if submitted:
        if "Sensitif Es/Suhu" in jenis_makanan:
            kurir = "Kurir A (Motor - Cepat & Lincah)"
            prioritas = 1
            alasan = "Makanan sensitif suhu wajib menggunakan motor agar sampai < 30 menit."
        elif lokasi == 'Area Macet Parah' and volume == 'Kecil/Sedang':
            kurir = "Kurir A (Motor - Lincah di Kemacetan)"
            prioritas = 1
            alasan = "Lokasi macet parah dengan volume kecil paling efisien ditembus pakai motor."
        elif volume == 'Sangat Besar / Banyak':
            kurir = "Kurir B (Mobil Box - Kapasitas Besar)"
            prioritas = 2
            alasan = "Volume muatan besar wajib menggunakan Mobil Box."
        else:
            kurir = "Kurir B (Mobil Box)"
            prioritas = 2
            alasan = "Kondisi normal dengan muatan standar dialokasikan ke mobil box."

        st.markdown(f"""
            <div class="card">
                <h4>Pesanan: <b>{id_pesanan}</b></h4>
                <p><b>Rekomendasi Kurir:</b> <span style="color: #0066cc; font-weight: bold;">{kurir}</span></p>
                <p><b>Tingkat Prioritas:</b> Prioritas {prioritas}</p>
                <p><b>Analisis Algoritma:</b> {alasan}</p>
            </div>
        """, unsafe_allow_html=True)
        
        if prioritas == 1:
            st.error("⚠️ STATUS: PRIORITAS TINGGI (Wajib Kirim Duluan)")
        else:
            st.success("✅ STATUS: ANTRIAN STANDAR (Muatan Besar)")
    else:
        st.info("Silakan isi form di sebelah kiri lalu klik tombol **'Hitung Alokasi Kurir'**.")

st.markdown("---")

# Statistik / Metric Card
st.subheader("📈 Statistik Pengiriman Harian")
m1, m2, m3 = st.columns(3)
m1.metric(label="Total Pesanan Masuk", value="10 Pesanan", delta="Target Harian")
m2.metric(label="Kurir A (Motor)", value="7 Tugas", delta="Fokus Jalur Macet")
m3.metric(label="Kurir B (Mobil Box)", value="3 Tugas", delta="Kapasitas Besar", delta_color="off")

# Dataframe Interaktif Tabel 10 Pesanan
st.subheader("📋 Tabel Simulasi Alokasi 10 Pesanan Dapur Nusantara")

data_simulasi = {
    "ID Pesanan": [f"P-0{i}" if i < 10 else f"P-{i}" for i in range(1, 11)],
    "Jenis Makanan": ["Sensitif Suhu", "Biasa", "Biasa", "Sensitif Suhu", "Biasa", "Biasa", "Sensitif Suhu", "Biasa", "Biasa", "Biasa"],
    "Lokasi Tujuan": ["Normal", "Macet Parah", "Normal", "Macet Parah", "Normal", "Macet Parah", "Normal", "Normal", "Macet Parah", "Normal"],
    "Volume": ["Kecil", "Kecil", "Sangat Besar", "Kecil", "Kecil", "Sangat Besar", "Kecil", "Kecil", "Kecil", "Sangat Besar"],
    "Kurir Alokasi": [
        "Kurir A (Motor)", "Kurir A (Motor)", "Kurir B (Mobil)", 
        "Kurir A (Motor)", "Kurir A (Motor)", "Kurir B (Mobil)", 
        "Kurir A (Motor)", "Kurir A (Motor)", "Kurir A (Motor)", "Kurir B (Mobil)"
    ],
    "Prioritas": ["Prioritas 1", "Prioritas 1", "Prioritas 2", "Prioritas 1", "Prioritas 1", "Prioritas 2", "Prioritas 1", "Prioritas 2", "Prioritas 1", "Prioritas 2"]
}

df_simulasi = pd.DataFrame(data_simulasi)
st.dataframe(df_simulasi, use_container_width=True)
