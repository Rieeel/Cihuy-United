Nama : Muhammad Derriel Ramadhan

NPM : 2406345186

Kelas : PBP F


https://muhammad-derriel-cihuyunited.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
    Pertama kita nyalain dulu python env nya lalu membuat project django baru dengan django-admin startproject (nama project) lalu kita semua terlebih dahulu seperti allowed host,env prod,env,database dan pws nya , setelah itu kita buat django start app main dan mengganti models dengan apa yag disuruh lalu kita routing main agar bisa dijalankan setelah itu kita buat fungsi dalam views untuk menampilkan nama apps dll setelah itu kita deploy ke pws

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

    Permintaan klien ke aplikasi web Django dimulai saat browser meminta URL-> yang pertama kali ditangani oleh urls.py untuk menemukan pola URL yang cocok -> lalu mengarahkannya ke fungsi atau kelas yang sesuai dalam views.py -> Views.py kemudian menjadi pusat logika, di mana ia dapat berinteraksi dengan basis data melalui models.py untuk mengambil, menyimpan, atau memanipulasi data yang diperlukan ->  Setelah data siap, views.py merendernya ke dalam berkas HTML (template), yang berisi placeholder untuk menampilkan data tersebut -> Setelah template terisi penuh, Django mengirimkan halaman HTML yang sudah selesai sebagai respons kembali ke browser klien, sehingga pengguna dapat melihat halaman web yang diminta.
3.  Jelaskan peran settings.py dalam proyek Django!
    tugas adalah Setting.py mendefinisikan koneksi ke database, mendaftarkan semua aplikasi yang aktif (INSTALLED_APPS), dan mengelola pengaturan keamanan krusial seperti SECRET_KEY dan DEBUG. Selain itu, file ini juga mengontrol bagaimana template (HTML) ditemukan dan di-render, menangani lokasi file statis (CSS, JavaScript), dan menentukan konfigurasi URL utama, sehingga secara efektif menjadi pusat kendali yang menentukan seluruh perilaku dan arsitektur aplikasi web Anda.
4.  Bagaimana cara kerja migrasi database di Django?
    Migrasi database di Django dilakukan dalam dua langkah. Pertama, perintah makemigrations dijalankan setelah kode model (models.py) diubah, yang bertugas mendeteksi perubahan tersebut dan membuat file Python yang berisi instruksi migrasi, tanpa menyentuh database. Kedua, perintah migrate kemudian menerjemahkan instruksi dari file tersebut ke dalam perintah SQL dan menerapkannya langsung pada database, secara fisik mengubah strukturnya. Seluruh proses ini dicatat dalam tabel django_migrations, memastikan konsistensi dan keamanan antara kode model dan struktur database.
5.  Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    Menurut saya framework Django merupakan salah satu framework yang beginner-friendly dimana kita juga udah menggunakan python di semester 1 dan beginner seperti mahasiswa bisa dengan mudah tanpa perlu external library.Selain itu, strukturnya yang jelas dengan pola MVT (Model-View-Template) membantu pemula memahami pemisahan tugas dalam kode, sementara dokumentasinya yang lengkap dan komunitasnya yang aktif mempermudah proses belajar
6.  Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
    Tidak ada,Semua tutorial sudah lengkap + mudah di mengerti.