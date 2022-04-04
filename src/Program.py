import time
import copy

global jumlahSimpul
global waktuEksekusi
global listSolusiPuzzle
jumlahSimpul=0
waktuEksekusi=0
listSolusiPuzzle=[]

def makePuzzle(file):
    #Membuat puzzle dari input file txt dalam bentuk matriks
    Puzzle=[[0 for j in range (4)] for i in range (4)]
    lines=""
    with open(file) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            else:
                if (c=="\n"):
                    lines+=" "
                else:
                    lines+=c
    index=0
    for i in range (4):
        for j in range (4):
            if (lines[index+1]==" "):
                Puzzle[i][j]=int(lines[index])
                index+=2
            else:
                bil=lines[index]+lines[index+1]
                Puzzle[i][j]=int(bil)
                index+=3
    return Puzzle

def matriksToHuruf(puzzle):
    #mengubah matriks puzzle menjadi string huruf untuk mempercapat algoritma agar tidak mengecek elemen matriks satu persatu
    stringHuruf = ""
    Huruf = "abcdefghijklmnop"
    for i in range(4):
        for j in range(4):
            stringHuruf += Huruf[puzzle[i][j]-1]
    return stringHuruf

def sumOfWrongBlock(puzzle):
    #Menghitung jumlah block yang salah atau ongkos mencapai simpul tujuan dari simpul puzzle
    count=0
    for i in range (4):
        for j in range (4):
            if (puzzle[i][j]!=16):
                if puzzle[i][j]!=i*4+j+1:
                    count+=1
    return count

def valueX(puzzle):
    #mengembalikan nilai X 
    for i in range (4):
        for j in range (4):
            if puzzle[i][j]==16:
                if (i+j)%2==0: 
                    return 0
                else: #jika baris+kolom tidak habis dibagi 2 atau berada di daerah yang diarsir
                    return 1

def indexRowNullBlock(puzzle):
    #mengembalikan baris pada block yang kosong
    for i in range (4):
        for j in range (4):
            if puzzle[i][j]==16:
                return i

def indexColumnNullBlock(puzzle):
    #mengembalikan kolom pada block yang kosong
        for i in range (4):
            for j in range (4):
                if puzzle[i][j]==16:
                    return j

def kurang(puzzle,number):
    #mengembalikan nilai kurang dari bilangan number pada puzzle
    sum=number-1
    end=False
    for i in range (4):
        for j in range (4):
            if (sum==0 or puzzle[i][j]==number):
                end=True
                break
            else:
                if (puzzle[i][j]<number):
                    sum-=1
        if (end):
            break
    return sum

def sumOfKurangdanX(puzzle):
    #menghitung jumlah kurang ditambah X pada puzzle
    sum=0
    for i in range (16):
        sum+=kurang(puzzle,i+1)
    X=valueX(puzzle)
    sum+=X
    return sum

def moveUp(puzzle,i,j):
    #mengembalikan puzzle yang block kosongnya dipindahkan ke atas
    newpuzzle=copy.deepcopy(puzzle)
    if (i==0):
        return None
    else:
        temp=newpuzzle[i][j]
        newpuzzle[i][j]=newpuzzle[i-1][j]
        newpuzzle[i-1][j]=temp
        return newpuzzle

def moveRight(puzzle,i,j):
    #mengembalikan puzzle yang block kosongnya dipindahkan ke kanan
    newpuzzle=copy.deepcopy(puzzle)
    if (j==3):
        return None
    else:
        temp=newpuzzle[i][j]
        newpuzzle[i][j]=newpuzzle[i][j+1]
        newpuzzle[i][j+1]=temp
        return newpuzzle

def moveDown(puzzle,i,j):
    #mengembalikan puzzle yang block kosongnya dipindahkan ke bawah
    newpuzzle=copy.deepcopy(puzzle)
    if (i==3):
        return None
    else:
        temp=newpuzzle[i][j]
        newpuzzle[i][j]=newpuzzle[i+1][j]
        newpuzzle[i+1][j]=temp
        return newpuzzle

def moveLeft(puzzle,i,j):
    #mengembalikan puzzle yang block kosongnya dipindahkan ke kiri
    newpuzzle=copy.deepcopy(puzzle)
    if (j==0):
        return None
    else:
        temp=newpuzzle[i][j]
        newpuzzle[i][j]=newpuzzle[i][j-1]
        newpuzzle[i][j-1]=temp
        return newpuzzle

def sumCost(puzzle,depthOfPuzzle):
    #mengembalikan nilai cost yaitu jumlah block yang salah ditambah kedalaman simpul
    return sumOfWrongBlock(puzzle)+depthOfPuzzle

def getIndexSmallestCost(listPuzzle):
    #mengembalikan indeks puzzle dengan nilai cost terkecil
    index=0
    smallestCost=listPuzzle[0][0]
    for i in range (1,len(listPuzzle)):
        if (smallestCost>listPuzzle[i][0]):
            smallestCost=listPuzzle[i][0]
            index=i
    return index

def matrixToList(matrix):
    #mengubah matriks menjadi list
    list=[]
    for i in range (4):
        for j in range (4):
            list.append(matrix[i][j])
    return list

def solvePuzzle(Puzzle):
    global jumlahSimpul
    global waktuEksekusi
    global listSolusiPuzzle

    listSolusiPuzzle=[]
    curNode=1 #simpul awal
    found=False
    solved=False
    mapPuzzle={} #dictionary berisi matriks puzzle dari simpulnya
    depthOfPuzzle={} #dictionary berisi kedalaman dari simpul
    parentNode = {} #dictionary berisi simpul parent dari simpul anaknya
    listString=[] #list berisi stringhuruf dari matriks puzzle
    mapPuzzle[curNode]=Puzzle
    stringHuruf=matriksToHuruf(Puzzle)
    listString.append(stringHuruf)
    depthOfPuzzle[curNode]=0
    cost=sumCost(Puzzle,depthOfPuzzle[curNode])
    parentNode[curNode]=None
    listPuzzle=[[cost, curNode]]
    start_time=time.time()
    while(not found):
        index=getIndexSmallestCost(listPuzzle)
        pick=listPuzzle.pop(index)
        node=pick[1]
        i=indexRowNullBlock(mapPuzzle[node])
        j=indexColumnNullBlock(mapPuzzle[node])
        movePuzzle=[]
        movePuzzle.append(moveUp(mapPuzzle[node],i,j))
        movePuzzle.append(moveRight(mapPuzzle[node],i,j))
        movePuzzle.append(moveLeft(mapPuzzle[node],i,j))
        movePuzzle.append(moveDown(mapPuzzle[node],i,j))
        for puzzle in movePuzzle:
            if (puzzle==None): #jika puzzle tidak ada
                continue
            stringHuruf=matriksToHuruf(puzzle)
            if (stringHuruf in listString): #jika puzzle sudah ada di listPuzzle atau sudah dieksekusi
                continue
            curNode+=1
            listString.append(stringHuruf)
            mapPuzzle[curNode]=puzzle
            parentNode[curNode]=node
            depthOfPuzzle[curNode]=depthOfPuzzle[node]+1
            cost=sumCost(puzzle,depthOfPuzzle[curNode])
            if (sumOfWrongBlock(puzzle)==0 ): #jika semua block puzzle sesuai
                found=True
                solved=True
                break
            listPuzzle.append([cost, curNode])
            if (curNode==100000): #membuat limit sampai 100000 agar program tidak hang terus menerus saat dijalankan
                found=True
                break
    end_time=time.time()
    jumlahSimpul=curNode
    waktuEksekusi=end_time-start_time
    if solved:
        listSolusiPuzzle.append(mapPuzzle[curNode])
        while(parentNode[curNode]!=None):
            curNode=parentNode[curNode]
            listSolusiPuzzle.append(mapPuzzle[curNode])
        listSolusiPuzzle.reverse() #susun puzzle sesuai dari awal puzzle