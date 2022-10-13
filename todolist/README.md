
**Tugas 4**

Heroku login: https://tugas2-pbp-arya.herokuapp.com/todolist/login/  Heroku register: https://tugas2-pbp-arya.herokuapp.com/todolist/register/  
Heroku main page: https://tugas2-pbp-arya.herokuapp.com/todolist/


1. csrf token beguna untuk keamanan data yang kita miliki. Dengan tidak adanya csrf pada form, akan memungkinkan adanya celah bagi pengguna lain untuk membobol form dan mengekspos data yang ada.
2. Pembuatan elemen form bisa juga dilakukan tanpa menggunakan form.as_table. Pembuatan form dapat menggunakan berbagai type yang ada, contohnya seperti "text", "password" dan lainnya. Elemen dari form yang sudah memiliki type kemudian harus diberikan value agar dapat dibedakan satu sama lain. Lalu setiap input yang ada harus diikuti dengan type "submit" agar elemen tersebut tersimpan pada database.
3. Untuk melakukan submisi kita membuat form registrasi yang dimana tersedia tombol submit (pada tugas ini tombol submit diberi value "Daftar"). Ketika user mendaftar, data yang diinput user akan dicek validasinya. Jika data yang diinput valid maka data tersebut akan di-save di database. Setelah data berhasil di-save, user kemudian akan di redirect ke halaman login untuk memasukkan data yang telah diinput tadi. Data yang sudah di-save tadi akan dirender oleh Django untuk ditampilkan sebagai halaman HTML.
4. Pertama saya membuat app baru bernama todolist. Kemudian hal pertama yang harus dilakukan adalah pathing pada urls.py agar web yang kita buat dapat diakses. Selanjutnya saya membuat data pada models.py sesuai dengan ketentuan yang ada pada dokumen tugas 4. Pengimplementasian login, register dan logout saya hanya meng-copy dari lab 3 dan mengganti data sesuai dengan data pada tugas 4 ini. Kemudian saya membuat html untuk menampilkan halaman todolist pada web. Lalu saya membuat halaman form yaitu addtask untuk menambahkan task pada todolist, dimana saya membuat addtask.html dengan elemen form mirip seperti halaman pada register. Kemudian dibuat routing agar semua hal yang telah saya buat tadi dapat diakses pada web.





**Akun Dummy**
Username: kentang22
Password: wortel123

Username: wortel22
Password: kentang123


**Tugas 5**
1. **Inline** merupakan style yang diterapkan langsung pada tag yang ingin kita style-kan. Kelebihan pada inline terletak pada prioritas dimana jika kita menggunakan style selain inline, maka style yang kita terapkan pada inline akan menjadi prioritas. Kekurangan inline terletak pada repetisi yang perlu kita lakukan apabila kita ingin melakukan style pada banyak tag yang sama sekaligus.
**Internal** merupakan style yang kita terapkan pada satu halaman html yang berlaku untuk seluruh halaman html itu saja. Kekurangannya terletak pada prioritas yang mana lebih diprioritaskan inline jika dibandingkan dengan internal. Kelebihannya adalah keefektifan jika ingin melakukan style pada 1 halaman html sekaligus.
**External** merupakan style yang kita terapkan pada seluruh halaman web kita sekaligus. Kekurangannya adalah kita harus memberikan selector pada tag yang ingin kita bedakan dengan tag lainnya dan kelebihannya adalah efektif dalam membuat style yang ingin diterapkan pada seluruh web sekaligus.

2. Tag <!DOCTYPE html> adalah sebuah deklarasi untuk mengidentifikasi jenis dokumen yang digunakan.
Tag <html>...</html> berfungsi sebagai root, dimana semua hal dalam tag tersebut akan diidentifiasi sebagai gambaran dari dokumen html.
Tag <head>...</head> berfungsi memberikan informasi mengenai dokumen-dokumen html.
Tag <Title>...</Title> berfungsi untuk memberikan title pada halaman html.
Tag<body>...</body> berfungsi memberikan isi dari suatu dokumen yang akan ditampilkan pada web browser.

3. Selector
Element selector berfungsi mengubah style untuk semua tag dari elemen tersebut.
ID selector berfunbgsi mengubah style untuk semua tag yang sudah kita berikan ID yang sama yang sudah kita jadikan sebagai selector.
Class Selector berfungsi mengubah tampilan html pada tag yang diberikan class.

4. Pertama saya mengimport bootstrap pada base.html agar bootstrap dapat digunakan pada html yang sudah saya buat.
Lalu saya menerapkan internal style pada setiap html yang saya buat dengan menggunakan tag <style></style>  untuk mengubah tiap-tiap html pada halaman web browser. Lalu saya menerapkan bootstrap pada pembuatan card yang dilakukan di todolist.html yang dimana terdapat 1 card untuk 1 task. Penerapan web responsive sudah diterapkan secara default dengan menerapkan tag meta 
<meta name="viewport" content="width=device-width, initial-scale=1.0">
Dengan menerapkan tag meta tersebut, bootstrap sudah secara default menerapkan responsive web.


**Tugas 6**

1. **Perbedaan antara Asynchrounus Programming dan Synchronus Programming**
Asynchronus programming adalah suatu proses jalannya sebuah program yang dapat bejalan secara bersamaan sehingga asynchronus programming dapat meningkatkan tingkat output program karena program dapat dijalankan secara bersamaan. Sedangkan synchronus programming merupakan kebalikan dari asynchronus programming dimana pada synchronus programming, program hanya dapat dijalankan satu per satu, seperti antrian, harus menunggu program sebelumnya menghasilkan output terlebih dahulu baru program selanjutnya kaan dijalankan.
2. **Event-Driven Programming**
Paradigma event-driven programming adalah suatu pemrogramman yang alur dari programnya ditentukan oleh suatu event yang dilakukan oleh user. Pada tugas ini penerapan paradigma event-driven programming ada pada tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task.
3. **Asynchronus Programming**
Penerapan asynchronus programming pada AJAX bisa diterapkan menggunakan async function sehingga setiap hal yang kita lakukan pada web page akan langsung ter-update tanpa kita harus me-refresh web page.
4. **Impelementasi Checklist**
Pertama saya membuat function yang mengembalikan data dalam bentuk json, yaitu function 'show_json'. Lalu saya membuat path agar 'show_json' dapat diakses pada web page. Lalu saya membuat tempalte html dimana diterapkannya AJAX. Kemudian saya buat views baru yang mengembalikan halaman html sesuai dengan user yang login. Kemudian saya membuat modal untuk menambahkan task dan view yang menambahkan task tersebut ke database.

```
<br></br>
<button><a href="{% url 'todolist:todoList' %}">Lihat dalam Tabel</a></button>
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" data-bs-whatever="@getbootstrap">Add task</button>

<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">New Task</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form id="formtask">
          {% csrf_token %}
          <div class="mb-3">
            <label for="recipient-name" class="col-form-label">Title:</label>
            <input type="text" class="form-control" id="field_title" name="title">
          </div>
          <div class="mb-3">
            <label for="message-text" class="col-form-label">Description:</label>
            <textarea class="form-control" id="field_desc" name="description"></textarea>
          </div>
        </form>
      </div>
        <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary" id="addtaskbutton" data-bs-dismiss="modal">Add</button>
      </div>
    </div>
  </div>
</div>
```

```
def add_task_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")

        new_todolist = TodoList(user=request.user, title=title, description=description)
        new_todolist.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
```

Dan terakhir saya menambahkan path untuk todolist/add/
