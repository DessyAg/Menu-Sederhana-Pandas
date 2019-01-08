
# Menu-Sederhana-Pandas- MySQL

Ketika code dijalankan maka tampilan utama akan seperti berikut :

Menu utama
 1. Lihat data
 2. Filter data
 3. Keluar
 Masukan Pilihan Anda
 
Kemudian jika memilih no 1 akan memunculkan data sebagai berikut :
 
 Masukan Pilihan Anda 1
                      Name  Type1   Type2  Total  HP  Attack  Defense  Sp.Atk  Sp.Def  Speed  Generation Legendary
0  1              Bulbasaur  Grass  Poison    318  45      49       49      65      65     45           1     False
1  2                Ivysaur  Grass  Poison    405  60      62       63      80      80     60           1     False
2  3               Venusaur  Grass  Poison    525  80      82       83     100     100     80           1     False
3  3  VenusaurMega Venusaur  Grass  Poison    625  80     100      123     122     120     80           1     False
4  4             Charmander   Fire     Bug    309  39      52       43      60      50     65           1     False

Menu 2 akan menampilkan data yang di kelompokan (Distinct) berdasarkan kolom Type2

1        Bug
2     Flying
3     Dragon
4     Normal
5      Ghost
6   Fighting
7       Fire
8     Ground
9        Ice
10   Psychic
11     Fairy
12     Grass
13  Electric
14     Steel
15      Dark
16      Rock
17     Water

Kemudian masukan pilihan data yang akan ditampilkan (misal : no 2)
Data akan di filter berdasarkan nomor 2 pada kolom Type2 yaitu Flying

masukan pilihan anda :2
                           Name   Type1   Type2  Total  HP  Attack  Defense  Sp.Atk  Sp.Def  Speed  Generation Legendary
0   6                  Charizard    Fire  Flying    534  78      84       78     109      85    100           1     False
1   6  CharizardMega Charizard Y    Fire  Flying    634  78     104       78     159     115    100           1     False
2  12                 Butterfree     Bug  Flying    395  60      45       50      90      80     70           1     False
3  16                     Pidgey  Normal  Flying    251  40      45       40      35      35     56           1     False
4  17                  Pidgeotto  Normal  Flying    349  63      60       55      50      50     71           1     False

Menu 3 : Keluar dari menu, Selesai


