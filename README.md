Nama : Muhammad Derriel Ramadhan

NPM : 2406345186

Kelas : PBP F


https://muhammad-derriel-cihuyunited.pbp.cs.ui.ac.id/

1.  Apa perbedaan antara synchronous request dan asynchronous request?
    Perbedaan utama antara permintaan sinkronus (synchronous) dan asinkronus (asynchronous) terletak pada cara program menangani waktu tunggu. Dalam model sinkronus, proses bersifat memblokir (blocking); artinya, ketika sebuah permintaan dikirim (misalnya, untuk mengambil data dari server), seluruh aplikasi harus menunggu sampai permintaan itu selesai dan respons diterima sebelum dapat melanjutkan ke tugas berikutnya. Ini seperti antrean di mana Anda tidak bisa melakukan apa pun sampai orang di depan Anda selesai dilayani. Sebaliknya, model asinkronus bersifat tidak memblokir (non-blocking). Aplikasi mengirimkan permintaan dan dapat langsung melanjutkan tugas-tugas lain tanpa harus menunggu respons. Ketika respons akhirnya tiba, sebuah fungsi atau mekanisme (seperti callback atau promise) akan menanganinya di latar belakang. Ini membuat aplikasi tetap responsif dan efisien, sangat ideal untuk pengalaman pengguna yang lancar di web dan aplikasi modern.


2. Bagaimana AJAX bekerja di Django (alur request–response)?
    AJAX di Django bekerja dengan cara mengirimkan request HTTP secara asynchronous dari browser ke server tanpa me-refresh halaman. Proses dimulai ketika JavaScript di sisi klien menangkap aksi pengguna, seperti klik tombol atau submit form, lalu mengirimkan request (GET atau POST) ke endpoint tertentu di Django. Django menerima request tersebut pada *view* yang sesuai, memproses data, dan mengembalikan response biasanya dalam format JSON atau HTML parsial. Response ini kemudian diterima oleh JavaScript di sisi klien, yang memproses dan memperbarui bagian halaman yang relevan secara dinamis. Dengan cara ini, AJAX memungkinkan interaksi yang lebih cepat dan lancar karena request–response terjadi di latar belakang tanpa memblokir atau me-refresh seluruh halaman.

3.  Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
    Keuntungan menggunakan AJAX dibandingkan render biasa di Django terletak pada efisiensi dan pengalaman pengguna. Dengan AJAX, permintaan data atau perubahan konten dilakukan secara asynchronous tanpa me-refresh seluruh halaman, sehingga proses menjadi lebih cepat dan lancar. Hal ini mengurangi beban server dan penggunaan bandwidth karena hanya data atau bagian halaman yang diperlukan yang dikirimkan, bukan seluruh template HTML. Selain itu, AJAX membuat interaksi pengguna menjadi lebih responsif dan dinamis, karena perubahan dapat ditampilkan secara real-time tanpa mengganggu aktivitas lain di halaman, sehingga menghasilkan pengalaman yang lebih modern dan nyaman dibandingkan metode render penuh pada Django.

4.   Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
    Untuk memastikan keamanan saat menggunakan AJAX pada fitur Login dan Register di Django, perlu diterapkan beberapa langkah penting. Pertama, pastikan request AJAX menggunakan metode POST untuk mengirim data sensitif seperti username dan password, bukan GET. Kedua, aktifkan CSRF protection Django dengan menyertakan token CSRF di header request AJAX agar mencegah serangan Cross-Site Request Forgery. Ketiga, lakukan validasi dan sanitasi data di sisi server untuk mencegah serangan seperti SQL injection atau XSS. Keempat, gunakan HTTPS untuk mengenkripsi data selama transmisi agar terhindar dari serangan man-in-the-middle. Terakhir, implementasikan mekanisme autentikasi yang aman, seperti Django Authentication Framework, dan berikan respons error yang jelas namun tidak membocorkan informasi sensitif. Dengan langkah-langkah ini, AJAX pada Login dan Register dapat berjalan aman tanpa mengorbankan pengalaman pengguna.

5.  Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
    AJAX secara signifikan meningkatkan pengalaman pengguna (User Experience) pada website karena memungkinkan interaksi yang lebih cepat, responsif, dan dinamis tanpa perlu me-refresh seluruh halaman. Dengan AJAX, data atau konten dapat diperbarui secara real-time sesuai aksi pengguna, seperti memuat daftar produk, mengirim form, atau memperbarui status tanpa gangguan visual. Hal ini membuat website terasa lebih lancar dan modern, mengurangi waktu tunggu, serta menjaga konteks halaman yang sedang digunakan pengguna. Akibatnya, pengguna merasa interaksi lebih intuitif dan efisien, sehingga meningkatkan kenyamanan dan kepuasan saat menggunakan website.

