import streamlit as st
import random

# ===================
# Data Senyawa Kimia
# ===================
senyawa_kimia = {
    "Asam": {
        "Asam Sulfat (H₂SO₄)": {
            "Risiko": "Korosif, menyebabkan luka bakar parah pada kulit dan mata.",
            "Penanganan": "Gunakan sarung tangan tahan asam, pelindung mata, dan lab coat.",
            "APD": "Sarung tangan karet, Googles, Masker, Respirator, Jas lab,Sepatu tertutup."
        },
    "Asam Klorida (HCl)": {
            "Risiko": "Iritasi pada saluran pernapasan dan kulit.",
            "Penanganan": "Gunakan di area berventilasi baik, hindari uap.",
            "APD": "Sarung tangan, pelindung wajah, masker respirator."
        },
        "Asam Nitrat (HNO₃)": {
            "Risiko": "Korosif dan oksidator kuat.",
            "Penanganan": "Pisahkan dari bahan organik, gunakan di lemari asam.",
            "APD": "Sarung tangan tahan asam, pelindung mata, jas lab."
        },
        "Asam Asetat (CH₃COOH)": {
            "Risiko": "Iritasi kulit dan mata; bau menyengat.",
            "Penanganan": "Gunakan ruang berventilasi.",
            "APD": "Sarung tangan, pelindung mata."
        }
    },
    "Basa": {
        "Natrium Hidroksida (NaOH)": {
            "Risiko": "Sangat korosif; luka bakar kimia.",
            "Penanganan": "Hindari kontak; netralisasi jika tumpah.",
            "APD": "Sarung tangan, pelindung mata, jas lab."
        },
        "Kalium Hidroksida (KOH)": {
            "Risiko": "Korosif dan mengiritasi.",
            "Penanganan": "Gunakan dengan hati-hati di area berventilasi.",
            "APD": "Sarung tangan tahan kimia, pelindung mata."
        },
        "Kalsium Hidroksida (Ca(OH)₂)": {
            "Risiko": "Iritasi kulit dan mata.",
            "Penanganan": "Hindari kontak langsung.",
            "APD": "Sarung tangan, kacamata keselamatan."
        },
        "Amonia (NH₃)": {
            "Risiko": "Iritan saluran napas dan mata.",
            "Penanganan": "Gunakan di ruangan berventilasi.",
            "APD": "Masker respirator, pelindung mata, sarung tangan nitril."
        }
    },
    "Pelarut Organik": {
        "Ethanol (C₂H₅OH)": {
            "Risiko": "Mudah terbakar; uap mengiritasi.",
            "Penanganan": "Jauhkan dari api; ventilasi penuh.",
            "APD": "Sarung tangan, masker."
        },
        "Aseton (C₃H₆O)": {
            "Risiko": "Mudah terbakar; uap dapat pusing.",
            "Penanganan": "Gunakan ruangan berventilasi.",
            "APD": "Sarung tangan, pelindung mata."
        },
        "Toluena (C₇H₈)": {
            "Risiko": "Neurotoksik, iritatif.",
            "Penanganan": "Hindari inhalasi.",
            "APD": "Respirator, sarung tangan."
        },
        "Metanol (CH₃OH)": {
            "Risiko": "Sangat beracun jika tertelan atau terhirup.",
            "Penanganan": "Gunakan dengan ventilasi kuat dan hindari kontak.",
            "APD": "Respirator, sarung tangan tahan kimia."
        }
    },
    "Gas Berbahaya": {
        "Klorin (Cl₂)": {
            "Risiko": "Gas beracun; iritasi saluran napas.",
            "Penanganan": "Gunakan di bawah lemari asap.",
            "APD": "Respirator, pelindung mata, sarung tangan kimia."
        },
        "Klorida Hidrogen (HCl gas)": {
            "Risiko": "Gas korosif; iritasi parah.",
            "Penanganan": "Area ventilasi, hindari inhalasi.",
            "APD": "Respirator, pelindung muka."
        },
        "Sulfur Dioksida (SO₂)": {
            "Risiko": "Iritasi napas dan mata.",
            "Penanganan": "Gunakan masker dan ventilasi.",
            "APD": "Masker respirator, pelindung mata."
        },
        "Karbon Monoksida (CO)": {
            "Risiko": "Gas tidak berwarna/baunya; mematikan.",
            "Penanganan": "Detektor CO wajib digunakan.",
            "APD": "Ventilasi kuat; masker tidak efektif sendiri."
        },
        "Gas Ozon (O₃)": {
            "Risiko": "Iritasi paru-paru dan mata.",
            "Penanganan": "Batasi waktu paparan.",
            "APD": "Masker respirator, pelindung mata."
        }
    }
}
# ===================
# Sidebar Navigation
# ===================
st.sidebar.title("🔬 Navigasi")
page = st.sidebar.radio("Menu", ["Beranda", "Senyawa Kimia", "Quiz"])

# ===================
# 1. Halaman Beranda
# ===================
if page == "Beranda":
    st.title("💡 Pengenalan Risiko dan Penanganan Senyawa Kimia")
    st.markdown("""
🚨 Kimia bukan cuma soal rumus, tapi juga soal *keselamatan!*  
Kenalan yuk sama *senyawa-senyawa kimia penting*,  
pelajari potensi bahayanya, dan cari tahu cara aman ngadepinnya 💥🛡

Klik menu di samping buat mulai, dan uji wawasanmu di akhir lewat kuis seru!
""")
# ============================
# 2. Halaman Senyawa Kimia
# ============================
elif page == "Senyawa Kimia":
    st.title("🧪 Daftar Senyawa Berdasarkan Golongan")

    golongan = st.selectbox("Pilih Golongan Senyawa", list(senyawa_kimia.keys()))

    if golongan:
        st.subheader(f"📚 Senyawa dalam Golongan: {golongan}")
        for nama, info in senyawa_kimia[golongan].items():
            with st.expander(f"🔍 {nama}"):
                st.markdown(f"**Risiko:** {info['Risiko']}")
                st.markdown(f"**Penanganan:** {info['Penanganan']}")
                st.markdown(f"**APD:** {info['APD']}")

# ===================
# 3. Halaman Quiz
# ===================
elif page == "Quiz":
    st.title("🧠 Quiz Penanganan Senyawa Kimia")
    st.markdown("Jawablah pertanyaan berikut dengan memilih jawaban yang paling tepat.")

    all_questions = []
    for golongan in senyawa_kimia:
        for nama, data in senyawa_kimia[golongan].items():
            all_questions.append({
                "senyawa": nama,
                "question": f"Apa APD yang dibutuhkan saat menangani {nama}?",
                "answer": data["APD"],
                "options": [
                    data["APD"],
                    "Sarung tangan kain, masker kain",
                    "Tidak perlu APD",
                    "Topi dan jas hujan"
                ]
            })

    # Random satu pertanyaan
    question = random.choice(all_questions)

    st.subheader(question["question"])
    pilihan = st.radio("Pilih jawaban Anda:", question["options"])

    if st.button("Cek Jawaban"):
        if pilihan == question["answer"]:
            st.success("✅ Jawaban benar!")
        else:
            st.error(f"❌ Jawaban salah. Jawaban yang benar adalah: **{question['answer']}**")  
