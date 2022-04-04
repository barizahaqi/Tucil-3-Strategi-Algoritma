# Tugas Kecil 3 Strategi Algoritma
## Author
   Bariza Haqi (13520018)

## Deskripsi Singkat
   15-Puzzle adalah sebuah permainan puzzle yang terdiri dari 16 kotak dengan 15 kotak berisi angka 1 sampai 15
   dan 1 kotak kosong. Dalam permainan ini susunan awal puzzle adalah acak kemudian pemain diharuskan menyusun 
   puzzle sehigga tersusun dari angka 1-15 dengan kotak terakhir adalah kotak kosong.Terdapat salah satu cara 
   untuk menyelesaikan persoalan 15-puzzle yaitu dengan menggunakan algoritma branch and bound.
   Program ini dibuat dengan algoritma branch and bound untuk menemukan menyelesaikan persoalan 15-puzzle
   pada input puzzle yang diberikan. 
   Fitur yang tersedia dalam Program ini adalah menyelesaikan  persoalan 15-puzzle menggunakan algoritma 
   branch and bound dengan memperlihatkan urutan penyelesaiannya melalui GUI python. Program ini dilimit hanya
   bisa melakukan sampai 100000 simpul yang terbentuk agak program tidak terus berjalan tanpa batas.

## Instalasi
	1. Pastikan python, pip, PySimpleGUI, sudah terinstall (direkomendasikan menggunakan versi terbaru)
	2. Software IDE (Untuk menjalankan program)
	3. Direkomendasikan menggunakan Windows OS

## Penggunaan

 ### Melalui file
	1. Jika puzzle belum dibuat, buat file txt di folder test dan isi bilangan 1-16 dengan 16 merupakan kotak kosong secara acak dengan susunan seperti matriks dengan spasi tiap bilangan dan diakhiri newline pada baris terakhir
	2. Buka file Main.py di folder src kemudian akan muncul sebuah GUI
	3. Tekan tombol browse kemudian mundur dari folder src dan pilih folder test
	4. Pilih file txt yang telah dibuat
	5. Tekan tombol "Solve Puzzle" untuk menyelesaikan persoalan puzzle
	6. Pakai tombol previous dan next untuk mengganti urutan solusi jika puzzle dapat diselesaikan
	7. Untuk menyelesaikan puzzle lain tekan tombol reset terlebih dahulu
 ### Melalui VS Code
    1. Jika puzzle belum dibuat, buat file txt di folder test dan isi bilangan 1-16 dengan 16 merupakan kotak kosong secara acak dengan susunan seperti matriks dengan spasi tiap bilangan dan diakhiri newline pada baris terakhir
	2. Buka file Main.py melalui VS Code kemudian eksekusi kode dengan mengetik python Main.py di terminal pada folder src kemudian akan muncul sebuah GUI
	3. Tekan tombol browse kemudian mundur dari folder src dan pilih folder test
	4. Pilih file txt yang telah dibuat
	5. Tekan tombol "Solve Puzzle" untuk menyelesaikan persoalan puzzle
	6. Pakai tombol previous dan next untuk mengganti urutan solusi jika puzzle dapat diselesaikan
	7. Untuk menyelesaikan puzzle lain tekan tombol reset terlebih dahulu
	