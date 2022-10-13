## Perbedaan Asynchronous dan Synchronous Programming

Pada *synchronous programming*, setiap *request* yang dibuat *client* harus diproses dan diberikan *response* terlebih dahulu sebelum *client* bisa membuat *request* lain.

Pada *asynchronous programming*, *client* bisa memberi beberapa *request* sebelum mendapat *response*. *Request*-*request* pada *asynchronous programming* diproses secara paralel.

## Event-Driven Programming

*Event* adalah sesuatu yang terjadi yang bisa terdeteksi oleh *website*, seperti saat pengguna mengeklik sebuah elemen, saat pengguna meletakkan *cursor*-nya pada sebuah elemen, atau saat halaman selesai dimuat. *Event-driven programming* adalah membuat program yang membuat *website* melakukan sesuatu setiap suatu jenis *event* terjadi.

Contoh implementasi ini pada tugas ini adalah melakukan AJAX POST berisi isi dari formulir untuk *event* ketika pengguna mengeklik tombol *submit* pada formulir pembuatan task baru.

## Asynchronous Programming pada AJAX

*Asynchronous programming* pada AJAX menggunakan *event-driven programming*. *File* HTML mengandung *script* yang berisi program Javascript yang akan memproses *request*-*request* pengguna dalam bentuk *event* yang ingin diberikan *response*.

Pengguna masih bisa memberi *request* saat *script* memproses *request* lain, sehingga ini termasuk *asynchronous programming*.

## Implementasi

1. Tambah *path* `json/` pada `urls.py` yang memanggil `show_json` pada `views.py`.
2. Tambah fungsi `show_json` pada `views.py` untuk mengembalikan *response* berupa representasi `json` dari semua instansi `Task`.
3. Pada `todolist.html`, ubah bagian *card* menjadi sebuah elemen dengan `id = "task-cards"`.
4. Pada `todolist.html`, tambah `script` berisi fungsi untuk melakukan `append` pada elemen dengan `id = "task-cards"` untuk setiap instansi `Task` menggunakan AJAX GET ke *path* `json/`.
4. Pada `todolist.html`, ubah tombol "Task baru" supaya tidak memanggil fungsi `create_task`, tetapi men-*toggle* `modal` untuk elemen `id = "modal-task-baru"`.
5. Pada `todolist.html`, buat elemen baru dengan `id = "modal-task-baru"` berisi *modal* untuk formulir pembuatan *task* baru. Tombol *submit*-nya melakukan POST ke *path* `add/`.
7. Tambah *path* `add/` pada `urls.py` yang memanggil `add_task` pada `views.py`.
8. Tambah fungsi `add_task` pada `views.py` untuk menambahkan instansi `Task` baru dari isi formulir dan mengembalikan *response* berupa representasi `json` dari instansi baru tersebut.
9. Pada `todolist.html`, tambah *script* yang memproses *event* setiap pengguna mengeklik tombol *submit* pada formulir pembuatan *task* baru yang akan melakukan AJAX POST ke fungsi `add_task` untuk memperbarui daftar instansi `Task` dan tampilan *card* tanpa melakukan *reload* seluruh halaman.