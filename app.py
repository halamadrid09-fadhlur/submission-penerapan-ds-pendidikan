import streamlit as st
import pandas as pd
from helper import preprocess_data
from prediction import predict
import constant

df = pd.DataFrame()

st.set_page_config(page_title="Dropout Dashboard", layout="wide")
st.title("Dashboard Prediksi Dropout Mahasiswa")
st.markdown(
    "Analisis performa dan prediksi status mahasiswa berdasarkan data historis."
)

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    df["Admission_grade"] = [
        int(
            st.number_input(
                "Admission Grade",
                value=100,
                min_value=0,
                max_value=200,
                help="Nilai penerimaan (antara 0 dan 200).",
            )
        )
    ]

with col2:
    df["Age_at_enrollment"] = [
        int(
            st.number_input(
                "Age at Enrollment",
                value=23,
                min_value=0,
                max_value=100,
                help="Usia siswa saat mendaftar.",
            )
        )
    ]

with col3:
    df["Application_mode"] = [
        int(
            st.selectbox(
                "Application Mode",
                options=list(constant.application_mode.keys()),
                format_func=lambda x: constant.application_mode[x],
                help="Metode aplikasi yang digunakan oleh siswa.",
            )
        )
    ]

with col4:
    df["Application_order"] = [
        int(
            st.number_input(
                "Application Order",
                value=0,
                min_value=0,
                max_value=9,
                help="Urutan pendaftaran siswa. (antara 0 - pilihan pertama; dan 9 pilihan terakhir).",
            )
        )
    ]

with col5:
    df["Course"] = [
        int(
            st.selectbox(
                "Course",
                options=list(constant.course.keys()),
                format_func=lambda x: constant.course[x],
                help="Program studi yang diambil oleh siswa.",
            )
        )
    ]

col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    df["Curricular_units_1st_sem_approved"] = int(
        st.number_input(
            "Curricular Units 1st Sem Approved",
            value=6,
            min_value=1,
            max_value=30,
            help="Jumlah satuan kurikulum yang disetujui oleh mahasiswa pada semester pertama.",
        )
    )

with col2:
    df["Curricular_units_1st_sem_credited"] = int(
        st.number_input(
            "Curricular Units 1st Sem Credited",
            value=0,
            min_value=0,
            max_value=20,
            help="Jumlah satuan kurikulum yang diambil oleh mahasiswa pada semester pertama.",
        )
    )

with col3:
    df["Curricular_units_1st_sem_enrolled"] = int(
        st.number_input(
            "Curricular Units 1st Sem Enrolled",
            value=6,
            min_value=1,
            max_value=30,
            help="Jumlah satuan kurikulum yang diambil oleh mahasiswa pada semester pertama.",
        )
    )

with col4:
    df["Curricular_units_1st_sem_evaluations"] = int(
        st.number_input(
            "Curricular Units 1st Sem Evaluations",
            value=8,
            min_value=0,
            max_value=50,
            help="Jumlah satuan kurikulum yang dievaluasi oleh mahasiswa pada semester pertama.",
        )
    )

with col5:
    df["Curricular_units_1st_sem_grade"] = float(
        st.number_input(
            "Curricular Units 1st Sem Grade",
            value=10.0,
            min_value=0.0,
            max_value=20.0,
            step=0.1,
            help="Nilai rata-rata unit kurikuler pada semester 1.",
        )
    )

with col6:
    df["Curricular_units_1st_sem_without_evaluations"] = int(
        st.number_input(
            "Curricular Units 1st Sem Without Evaluations",
            value=0,
            min_value=0,
            max_value=30,
            help="Jumlah unit kurikuler pada semester 1 tanpa evaluasi.",
        )
    )

col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    df["Curricular_units_2nd_sem_approved"] = int(
        st.number_input(
            "Curricular Units 2nd Sem Approved",
            value=6,
            min_value=1,
            max_value=30,
            help="Jumlah satuan kurikulum yang disetujui oleh mahasiswa pada semester kedua.",
        )
    )

with col2:
    df["Curricular_units_2nd_sem_credited"] = int(
        st.number_input(
            "Curricular Units 2nd Sem Credited",
            value=0,
            min_value=0,
            max_value=20,
            help="Jumlah satuan kurikulum yang diambil oleh mahasiswa pada semester kedua.",
        )
    )

with col3:
    df["Curricular_units_2nd_sem_enrolled"] = int(
        st.number_input(
            "Curricular Units 2nd Sem Enrolled",
            value=6,
            min_value=1,
            max_value=30,
            help="Jumlah satuan kurikulum yang diambil oleh mahasiswa pada semester kedua.",
        )
    )

with col4:
    df["Curricular_units_2nd_sem_evaluations"] = int(
        st.number_input(
            "Curricular Units 2nd Sem Evaluations",
            value=8,
            min_value=0,
            max_value=50,
            help="Jumlah satuan kurikulum yang dievaluasi oleh mahasiswa pada semester kedua.",
        )
    )

with col5:
    df["Curricular_units_2nd_sem_grade"] = float(
        st.number_input(
            "Curricular Units 2nd Sem Grade",
            value=10.0,
            min_value=0.0,
            max_value=20.0,
            step=0.1,
            help="Nilai rata-rata unit kurikuler pada semester 2.",
        )
    )

with col6:
    df["Curricular_units_2nd_sem_without_evaluations"] = int(
        st.number_input(
            "Curricular Units 2nd Sem Without Evaluation",
            value=0,
            min_value=0,
            max_value=30,
            help="Jumlah unit kurikuler pada semester 2 tanpa evaluasi.",
        )
    )

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    df["Daytime_evening_attendance"] = st.selectbox(
        "Daytime/Evening Attendance",
        options=list(constant.daytime_evening_attendance.keys()),
        format_func=lambda x: constant.daytime_evening_attendance[x],
        help="Apakah siswa menghadiri kelas pada siang hari atau malam hari.",
    )

with col2:
    df["Debtor"] = st.selectbox(
        "Debtor",
        options=list(constant.debtor.keys()),
        format_func=lambda x: constant.debtor[x],
        help="Apakah mahasiswa tersebut seorang debitur.",
    )

with col3:
    df["Displaced"] = st.selectbox(
        "Displaced",
        options=list(constant.displaced.keys()),
        format_func=lambda x: constant.displaced[x],
        help="Apakah mahasiswa tersebut merupakan mahasiswa yang dipindahkan.",
    )

with col4:
    df["Educational_special_needs"] = st.selectbox(
        "Educational Special Needs",
        options=list(constant.educational_special_needs.keys()),
        format_func=lambda x: constant.educational_special_needs[x],
        help="Apakah mahasiswa tersebut memiliki kebutuhan pendidikan khusus.",
    )
with col5:
    df["GDP"] = float(
        st.number_input(
            "GDP",
            value=0.0,
            help="Produk Domestik Bruto (GDP) negara.",
        )
    )

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    df["Fathers_occupation"] = st.selectbox(
        "Father's Occupation",
        options=list(constant.fathers_occupation.keys()),
        format_func=lambda x: constant.fathers_occupation[x],
        help="Pekerjaan ayah mahasiswa.",
    )

with col2:
    df["Fathers_qualification"] = st.selectbox(
        "Father's Qualification",
        options=list(constant.fathers_qualification.keys()),
        format_func=lambda x: constant.fathers_qualification[x],
        help="Kualifikasi pendidikan ayah mahasiswa.",
    )

with col3:
    df["Mothers_occupation"] = st.selectbox(
        "Mother's Occupation",
        options=list(constant.mothers_occupation.keys()),
        format_func=lambda x: constant.mothers_occupation[x],
        help="Pekerjaan ibu mahasiswa.",
    )

with col4:
    df["Mothers_qualification"] = st.selectbox(
        "Mother's Qualification",
        options=list(constant.mothers_qualification.keys()),
        format_func=lambda x: constant.mothers_qualification[x],
        help="Kualifikasi pendidikan ibu mahasiswa.",
    )

with col5:
    df["Gender"] = st.selectbox(
        "Gender",
        options=list(constant.gender.keys()),
        format_func=lambda x: constant.gender[x],
        help="Jenis kelamin mahasiswa.",
    )

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    df["Inflation_rate"] = float(
        st.number_input(
            "Inflation Rate",
            value=0.0,
            help="Tingkat inflasi negara.",
        )
    )
with col2:
    df["International"] = st.selectbox(
        "International",
        options=list(constant.international.keys()),
        format_func=lambda x: constant.international[x],
        help="Apakah mahasiswa tersebut internasional.",
    )
with col3:
    df["Marital_status"] = st.selectbox(
        "Marital Status",
        options=list(constant.marital_status.keys()),
        format_func=lambda x: constant.marital_status[x],
        help="Status pernikahan mahasiswa.",
    )

with col4:
    df["Nacionality"] = st.selectbox(
        "Nationality",
        options=list(constant.nationality.keys()),
        format_func=lambda x: constant.nationality[x],
        help="Kewarganegaraan mahasiswa.",
    )

with col5:
    df["Unemployment_rate"] = float(
        st.number_input(
            "Unemployment Rate",
            value=0.0,
            help="Tingkat pengangguran negara.",
        )
    )

col1, col2, col3, col4 = st.columns(4)
with col1:
    df["Previous_qualification"] = st.selectbox(
        "Previous Qualification",
        options=list(constant.previous_qualification.keys()),
        format_func=lambda x: constant.previous_qualification[x],
        help="Kualifikasi pendidikan sebelumnya mahasiswa.",
    )

with col2:
    df["Previous_qualification_grade"] = int(
        st.number_input(
            "Previous Qualification Grade",
            value=100,
            min_value=0,
            max_value=200,
            help="Nilai kualifikasi pendidikan sebelumnya (antara 0 dan 200).",
        )
    )

with col3:
    df["Scholarship_holder"] = st.selectbox(
        "Scholarship Holder",
        options=list(constant.scholarship_holder.keys()),
        format_func=lambda x: constant.scholarship_holder[x],
        help="Apakah mahasiswa tersebut penerima beasiswa.",
    )

with col4:
    df["Tuition_fees_up_to_date"] = st.selectbox(
        "Tuition Fees Up to Date",
        options=list(constant.tuition_fees_up_to_date.keys()),
        format_func=lambda x: constant.tuition_fees_up_to_date[x],
        help="Apakah mahasiswa tersebut membayar biaya kuliah tepat waktu.",
    )

if st.button("Predict Dropout"):
    # Preprocess the data
    preprocessed_data = preprocess_data(df)

    # Make predictions
    prediction = predict(preprocessed_data)

    st.subheader("Hasil Prediksi Dropout:")
    st.write(prediction)

    # Display the prediction
    if prediction == "Dropout":
        st.warning("Mahasiswa diprediksi akan dropout.")
    else:
        st.success("Mahasiswa diprediksi tidak akan dropout.")
else:
    st.info("Masukkan data mahasiswa untuk memprediksi kemungkinan dropout.")
    st.markdown(
        "Silakan isi semua kolom yang diperlukan dan klik tombol 'Predict Dropout' untuk melihat hasil prediksi."
    )
