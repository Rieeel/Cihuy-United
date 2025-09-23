Nama : Muhammad Derriel Ramadhan

NPM : 2406345186

Kelas : PBP F


https://muhammad-derriel-cihuyunited.pbp.cs.ui.ac.id/

1.  Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
    Django AuthenticationForm adalah kelas siap pakai (build in) yang disediakan Django untuk menangani proses login pengguna secara aman dan efisien. Keunggulan utamanya terletak pada kemudahan implementasi, keamanan bawaan yang solid (termasuk proteksi CSRF), serta kemampuannya untuk secara otomatis memvalidasi kredensial (username dan password) dan memeriksa status aktif akun. Meskipun demikian, keterbatasannya adalah fleksibilitas, karena secara default ia dirancang untuk login berbasis username, sehingga fungsionalitas seperti login via email atau penambahan khusus lainnya.


2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
    Seperti yang sudah di ajarkan didalam kelas, Autentikasi adalah proses memverifikasi identitas pengguna, menjawab pertanyaan "Siapa Anda?" Ini umumnya dilakukan dengan memeriksa kredensial, seperti nama pengguna dan kata sandi, untuk memastikan pengguna adalah orang yang mereka klaim. Sebaliknya, otorisasi adalah proses menentukan hak akses atau izin pengguna, menjawab pertanyaan "Apa yang bisa Anda lakukan?" Proses ini terjadi setelah autentikasi berhasil dan berfungsi untuk membatasi tindakan pengguna sesuai dengan peran atau hak istimewa mereka dalam sistem. Contohnya, setelah Anda berhasil diautentikasi (masuk), sistem akan mengotorisasi Anda untuk melihat atau mengedit file tertentu berdasarkan izin yang telah diberikan. Secara ringkas, autentikasi adalah tentang identifikasi, sedangkan otorisasi adalah tentang izin.

3.  Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
    Keduanya, session dan cookies, berfungsi untuk menyimpan state pada aplikasi web, namun dengan perbedaan mendasar pada lokasi penyimpanannya. Cookies menyimpan data dalam jumlah kecil langsung di sisi klien (web pengguna), yang membuatnya sederhana, cepat, dan tidak membebani server. Namun, hal ini juga menimbulkan risiko keamanan karena data dapat diakses dan diubah oleh klien, serta menimbulkan masalah privasi. Sebaliknya, session menyimpan data di sisi server, yang hanya menyimpan session ID di cookie klien sebagai penunjuk. Metode ini jauh lebih aman untuk menyimpan informasi sensitif dan memungkinkan penyimpanan data dalam jumlah yang jauh lebih besar, tetapi menuntut lebih banyak sumber daya server dan menghadirkan tantangan dalam hal skalabilitas saat aplikasi berkembang. Oleh karena itu, pemilihan antara keduanya tergantung pada jenis data yang akan disimpan: cookies cocok untuk data non-sensitif dan sederhana, sementara session lebih ideal untuk informasi yang bersifat krusial dan kompleks.

4.  Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
    penggunaan cookies secara default tidaklah aman dan memiliki risiko signifikan, termasuk potensi pencurian data melalui serangan Cross-Site Scripting (XSS), pembajakan sesi melalui Cross-Site Request Forgery (CSRF), dan intersepsi data sensitif dalam serangan Man-in-the-Middle (MITM) jika tidak menggunakan HTTPS. Namun, kerangka kerja seperti Django secara proaktif mengatasi risiko-risiko ini dengan menerapkan langkah-langkah keamanan bawaan yang kuat. Django secara otomatis menggunakan session ID yang disimpan di cookie yang aman dan HttpOnly, mencegah akses oleh skrip berbahaya. Selain itu, Django menyertakan sistem perlindungan CSRF yang terintegrasi, yang menambahkan token unik pada setiap permintaan, serta mendorong penggunaan Secure Flag untuk memastikan transmisi cookie hanya melalui koneksi HTTPS yang terenkripsi, sehingga secara efektif memitigasi sebagian besar risiko keamanan yang terkait dengan penggunaan cookie.

5.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    cara saya mengimplementasikan checklist diatas berawal dari implementasi berawal dari import semua package yang dibutuhkan lalu membuat beberapa fungsi yaitu tombol login logout register dan membuat masing masing html buat tombol tersebut,lalu tombol tersebut di isi link menuju ke html yang sudah kita buat serta kita membuat models baru bernama users, setelah kita migrate, kita menambahkan decoration @login_required pada add product dan show product dan untuk login nya kita simpan di cookies, dengan begitu website kita lebih aman ketimbang pertama kali launching.

