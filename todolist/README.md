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

## Implementasi Tugas 4

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

## Perbedaan CSS Inline, Internal, dan External

| Inline | Internal | External |
|:- |:- |:- |
| Berupa atribut `style` pada *tag* suatu elemen. | Berupa *tag* `<style>` pada suatu *file* HTML. | Berupa *file* `.css` yang di-*import* ke *file* HTML. |
| Hanya mengatur *style* satu elemen. | Mengatur *style* semua elemen pada satu *file* HTML. | Mengatur *style* semua elemen pada satu *file* HTML dan *file* `.css` yang sama bisa digunakan di banyak *file* HTML. |

## Contoh Tag HTML5

- `<body>`: Isi konten atau badan dari *file* HTML.
- `<table>`: Tabel.
- `<thead>`: Kepala tabel.
- `<tbody>`: Isi konten atau badan tabel.
- `<tr>`: Baris tabel.
- `<td>`: Data tabel.
- `<input>`: Elemen yang bisa diinteraksikan oleh pengguna untuk memberi data masukan.
- `<nav>`: *Navigation bar*.
- `<br>`: *Line-break*.

## Contoh Selector CSS

- `.namaclass`: Menyeleksi elemen yang `class`-nya adalah `namaclass`.
- `#namaid`: Menyeleksi elemen yang `id`-nya adalah `namaid`.
- `namatag`: Menyeleksi elemen yang *tag*-nya adalah `namatag`.

## Implementasi Tugas 5

1. Masukkan *file* `bootstrap.css` dan `bootstrap.css.map` pada *folder* `css` yang ada di dalam *folder* `static`.
2. *Import* `bootstrap.css` pada `base.html`.
3. Memberi `<nav>` pada setiap *file* HTML untuk membuat *navigation bar* yang berisi informasi halaman dan tombol-tombol penting seperti tombol membuat *task* baru dan *logout* pada `todolist.html`.
4. Membuat `container` yang berisi tabel login, tabel formulir registrasi, dan tabel pembuatan *task* baru pada masing-masing *file* HTMLnya untuk memosisikan tabel-tabel tersebut pada tengah layar.
5. Mengatur `max-width` tabel-tabel tersebut supaya mempunyai lebar yang tertentukan, tetapi tetap responsif apabila layar lebih sempit.
6. Memberi *style* seperti warna pada setiap elemen.
7. Menambahkan gambar latar belakang dengan mencantumkan gambar pada *folder* `images` yang ada di dalam *folder* `static` dan meng-*import* gambar tersebut pada `base.html` sebagai gambar latar belakang.
8. Untuk setiap *task* pada `todolist.html`, tambahkan `<card>` untuk merepresentasikan setiap *task* sebagai satu *card* dengan *card*-*card* tersebut tersusun dari atas ke bawah.
9. Tambahkan *style* dan `container` untuk *card*-*card* tersebut supaya sama dengan elemen-elemen pada halaman lain.
10. Tambahkan `.card:hover` pada `style.css` untuk yang membesarkan ukuran *card* apabila *cursor* menyentuh *card* tersebut.