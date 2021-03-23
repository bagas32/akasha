import os
import sys
from tabulate import tabulate

def basisData():
    a = raw_input("Masukan nama Enterprise/Database : ")
    print("-------------------------------------------------------")
    ## ini block entitas/table
    b = raw_input("Masukan Entitas/Table - 1 : ")
    c = raw_input("Masukan Entitas/Table - 2 : ")
    d = raw_input("Masukan Entitas/Table - 3 : ")
    print("-------------------------------------------------------")
    ## ini block entitas/column
    e = raw_input("Masukan Attribute/Column {} - 1 : ".format(b))
    f = raw_input("Masukan Attribute/Column {} - 2 : ".format(b))
    g = raw_input("Masukan Attribute/Column {} - 3 : ".format(b))
    print("-------------------------------------------------------")
    h = raw_input("Masukan Attribute/Column {} - 1 : ".format(c))
    i = raw_input("Masukan Attribute/Column {} - 2 : ".format(c))
    j = raw_input("Masukan Attribute/Column {} - 3 : ".format(c))
    print("-------------------------------------------------------")
    k = raw_input("Masukan Attribute/Column {} - 1 : ".format(d))
    l = raw_input("Masukan Attribute/Column {} - 2 : ".format(d))
    m = raw_input("Masukan Attribute/Column {} - 3 : ".format(d))
    print("-------------------------------------------------------")
    ## Ini Block Nilai Data
    print("Input Nilai data Atrr/Column pada Entitas/table {}".format(b))
    aa = raw_input("Masukan Nilai data Attr/Column {} : ".format(e))
    bb = raw_input("Masukan Nilai data Attr/Column {} : ".format(f))
    cc = raw_input("Masukan Nilai data Attr/Column {} : ".format(g))
    print("-------------------------------------------------------")
    print("Input Nilai data Atrr/Column pada Entitas/table {}".format(c))
    dd = raw_input("Masukan Nilai data Attr/Column {} : ".format(h))
    ee = raw_input("Masukan Nilai data Attr/Column {} : ".format(i))
    ff = raw_input("Masukan Nilai data Attr/Column {} : ".format(j))
    print("-------------------------------------------------------")
    print("Input Nilai data Atrr/Column pada Entitas/table {}".format(d))
    gg = raw_input("Masukan Nilai data Attr/Column {} : ".format(k))
    hh = raw_input("Masukan Nilai data Attr/Column {} : ".format(l))
    ii = raw_input("Masukan Nilai data Attr/Column {} : ".format(m))
    print("-------------------------------------------------------")
    ## Ini Block Primary Key/ Kunci Elemen
    print("Input Primary key Attr/Column pada table {} : ".format(b))
    print("berikut ini adalah list Primary key mu cok : ")
    dataCol1 = [[e],[f],[g]]
    print(tabulate(dataCol1))
    jj = raw_input("Pilih salah satu data tersebut dan inputkan disini : ")
    print("-------------------------------------------------------")
    print("Input Primary key Attr/Column pada table {} : ".format(c))
    print("berikut ini adalah list Primary key mu cok : ")
    dataCol2 = [[h],[i],[j]]
    print(tabulate(dataCol2))
    kk = raw_input("Pilih salah satu data tersebut dan inputkan disini : ")
    print("-------------------------------------------------------")
    print("Input Primary key Attr/Column pada table {} : ".format(d))
    print("berikut ini adalah list Primary key mu cok : ")
    dataCol3 = [[k],[l],[m]]
    print(tabulate(dataCol3))
    ll = raw_input("Pilih salah satu data tersebut dan inputkan disini : ")
    print("-------------------------------------------------------")
    print("-------------------------------------------------------")
    print("berikut ini adalah Record data yang sudah ente buat : ")
    palako = ['Enterprise', 'Entitas', 'Atribute', 'Nilai Data', 'Kunci Elemen/Primary Key']
    samadengan = "--//--"
    kosong = "---"
    dataHasil = [[a, kosong, kosong, kosong, kosong], 
    [samadengan, b, e, aa, jj],
    [samadengan, b, f, bb, samadengan],
    [samadengan, b, g, cc, samadengan],
    [samadengan, c, h, dd, kk],
    [samadengan, c, i, ee, samadengan],
    [samadengan, c, j, ff, samadengan],
    [samadengan, d, k, gg, ll],
    [samadengan, d, l, hh, samadengan],
    [samadengan, d, m, ii, samadengan]]
    print("---------------------------------------------")
    print(tabulate(dataHasil, palako))


basisData()