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
