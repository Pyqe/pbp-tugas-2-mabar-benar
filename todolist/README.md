[Tautan aplikasi](https://pbp-tugas-2-mabar-benar.herokuapp.com/todolist/).

## Kegunaan `{% csrf_token %}`

Ini berguna untuk memastikan bahwa *user* yang meng-*submit* formulir tersebut adalah benar-benar *user* yang mengisi formulir tersebut, bukan pihak lain.

## Form Tanpa `{{form.as_table}}`

Formulir bisa dibuat dengan dua cara. Cara pertama adalah membuat *class* formulir tersebut dan menyalurkan instansi *class* tersebut ke *file* HTML, kemudian *file* HTML menampilkan formulir menggunakan `{{form.as_table}}`. Cara kedua adalah dengan membuat formulirnya langsung pada *file* HTML. Di dalam `<form>` berisi beberapa `<input>` yang bisa berisi `type = "text"` dan satu `<input>` yang berisi `type = submit`.

## Alur Data

1. *User* mengisi formulir.
2. *User* menekan *submit*.
3. Data yang diisi pada formulir tersalurkan sebagai atribut `request.POST`.
4. `views.py` melakukan `save()`.
5. Data baru akan tersimpan ke *database*.

## Implementasi

1. Lakukan `startapp` untuk membuat aplikasi baru bernama `todolist`.
2. Tambah `todolist` pada `INSTALLED_APPS` di dalam `settings.py` di *folder* `project_django`.
3. Tambah `path` baru untuk `todolist` di dalam `urls.py` di *folder* `project_django`.
4. Pada `urls.py` di *folder* `todolist`, tambah beberapa `path` supaya bisa memanggil fungsi-fungsi dari `views.py`.
5. Pada `views.py` di *folder* `todolist`, buat fungsi-fungsi berikut:
    - `show_todolist` untuk menampilkan halaman *to do list* menggunakan `todolist.html`.
    - `login_user` untuk *login* *user* menggunakan `login.html`.
    - `logout_user` untuk *logout* *user*.
    - `register` untuk membuat akun baru menggunakan `register.html`.
    - `create_task` untuk membuat *task* baru menggunakan `create-task.html`.
6. Membuat `models.py` yang mendefinisikan *class* `Task` yang digunakan oleh `views.py`.
7. Lakukan `makemigrations` dan `migrate`.
8. Membuat *file*-*file* HTML berikut:
    - `todolist.html` yang menampilkan tabel berisi semua *task*.
    - `login.html` yang memberikan formulir *login* *user*.
    - `register.html` yang memberikan formulir registrasi akun.
    - `create-task.html` yang memberikan formulir pembuatan *task* baru.
9. *Push* semua ke GitHub.