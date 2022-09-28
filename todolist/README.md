1. csrf token beguna untuk keamanan data yang kita miliki. Dengan tidak adanya csrf pada form, akan memungkinkan adanya celah bagi pengguna lain untuk membobol form dan mengekspos data yang ada.
2. Pembuatan elemen form bisa juga dilakukan tanpa menggunakan form.as_table. Pembuatan form dapat menggunakan berbagai type yang ada, contohnya seperti "text", "password" dan lainnya. Elemen dari form yang sudah memiliki type kemudian harus diberikan value agar dapat dibedakan satu sama lain. Lalu setiap input yang ada harus diikuti dengan type "submit" agar elemen tersebut tersimpan pada database.
3. Untuk melakukan submisi kita membuat form registrasi yang dimana tersedia tombol submit (pada tugas ini tombol submit diberi value "Daftar"). Ketika user mendaftar, data yang diinput user akan dicek validasinya. Jika data yang diinput valid maka data tersebut akan di-save di database. Setelah data berhasil di-save, user kemudian akan di redirect ke halaman login untuk memasukkan data yang telah diinput tadi. Data yang sudah di-save tadi akan dirender oleh Django untuk ditampilkan sebagai halaman HTML.
4. Pertama saya membuat app baru bernama todolist. Kemudian hal pertama yang harus dilakukan adalah pathing pada urls.py agar web yang kita buat dapat diakses. Selanjutnya saya membuat data pada models.py sesuai dengan ketentuan yang ada pada dokumen tugas 4. Pengimplementasian login, register dan logout saya hanya meng-copy dari lab 3 dan mengganti data sesuai dengan data pada tugas 4 ini. Kemudian saya membuat html untuk menampilkan halaman todolist pada web. Lalu saya membuat halaman form yaitu addtask untuk menambahkan task pada todolist, dimana saya membuat addtask.html dengan elemen form mirip seperti halaman pada register. Kemudian dibuat routing agar semua hal yang telah saya buat tadi dapat diakses pada web.





**Akun Dummy**
Username: kentang22
Password: wortel123

Username: wortel22
Password: kentang123