https://tugas2-pbp-arya.herokuapp.com/katalog/
1. ![messageImage_1663203573997](https://user-images.githubusercontent.com/112262877/190289471-f0f86209-b1fc-4dd0-a560-b4f949d6e24b.jpg)
2. Virtual Environment digunakan untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada di device yang kita gunakan.
   Bisa saja membuat aplikasi web berbasis django tetapi jika ada package ataupun dependencies yang memiliki update baru, maka jika kita tidak menggunakan virtual environment,
   package atau dependencies tersebut akan auto terupdate pada aplikasi web berbasis django kita.
3. 1)Membuat fungsi pada views.py dengan mengimport class dari models.py lalu membuat variabel untuk menyimpan hasil query dari seluruh data yang ada dari class pada models.py.
   2)Mengimport fungsi yang ada di views.py di urls.py untuk membuat routingnya kemudian menambahkan aplikasi ke urls.py yang ada pada project-django.
   3)Melakukan mapping dengan menggunakan sintaks dari django yaitu {{data}} dengan data berupa data yang ingin ditampilkan dari models.py  
   4)Mendeploy ke heroku dengan mendapatkan API key dari heroku, lalu menambahkan API key serta heroku app_name ke secrets pada repository github account kita. Lalu menjalankan
     kembali workflow yang gagal pada github bagian actions.
