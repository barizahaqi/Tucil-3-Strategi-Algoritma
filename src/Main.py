import Program as p
import PySimpleGUI as sg
import os

#Buat GUI
menu_column = [ #GUI bagian kanan
    [sg.Text('15 Puzzle Solver', size=(20, 1), justification='center', font=("Helvetica", 32))],
    [
        sg.Text("File Location"),
        sg.In(size=(30,1), enable_events=True, key="-File-"),
        sg.FileBrowse(initial_folder=os.path.dirname(os.path.abspath(__file__)), file_types=(("Text Files", "*.txt"),))
    ],
    [
        sg.Button("Solve Puzzle", key="-SOLVE-"),
        sg.Button("Reset", key="-RESET-")
    ],
    [sg.Text(key="-SUM-")],
    [sg.Text(key="-TIME-")],
    [sg.Text(key="-JUMLAH-")] 
    
]

puzzle_column = [#GUI bagian kiri
    [
        sg.Image(key="-PUZZLE1-", size=(118, 118)),
        sg.Image(key="-PUZZLE2-", size=(118, 118)),
        sg.Image(key="-PUZZLE3-", size=(118, 118)),
        sg.Image(key="-PUZZLE4-", size=(118, 118))
    ],
    [
        sg.Image(key="-PUZZLE5-", size=(118, 118)),
        sg.Image(key="-PUZZLE6-", size=(118, 118)),
        sg.Image(key="-PUZZLE7-", size=(118, 118)),
        sg.Image(key="-PUZZLE8-", size=(118, 118))
    ],
    [
        sg.Image(key="-PUZZLE9-", size=(118, 118)),
        sg.Image(key="-PUZZLE10-", size=(118, 118)),
        sg.Image(key="-PUZZLE11-", size=(118, 118)),
        sg.Image(key="-PUZZLE12-", size=(118, 118))
    ],
    [
        sg.Image(key="-PUZZLE13-", size=(118, 118)),
        sg.Image(key="-PUZZLE14-", size=(118, 118)),
        sg.Image(key="-PUZZLE15-", size=(118, 118)),
        sg.Image(key="-PUZZLE16-", size=(118, 118))
    ],
    [
        sg.Button("Previous", key="-PREVIOUS-"),
        sg.Button("Next", key="-NEXT-")
    ],
    [
        sg.Text(key="-LANGKAH-")
    ]
    
]

layout =[
    [
        sg.Column(puzzle_column,element_justification='c'),
        sg.VSeperator(),
        sg.Column(menu_column,element_justification='c'),
    ]
]

window =sg.Window("Program 15-Puzzle", layout)

puzzle=None
index=0
solved=False
imgFolder=os.path.dirname(os.path.abspath(__file__))+"\\"+"img" #untuk gui gambar puzzle
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: #keluar dari program
        break
    if event == "-File-": #menekan tombol Browse
        try:
            puzzle = p.makePuzzle(values["-File-"])
            list=p.matrixToList(puzzle)
            for i in range(16):
                if (list[i]==16):
                    window[f"-PUZZLE{i+1}-"].update("", size=(118, 118))
                else:
                    window[f"-PUZZLE{i+1}-"].update(imgFolder+"\\"+str(list[i])+".png")
        except:
            pass

    if event=="-SOLVE-":#menekan tombol Solve Puzzle
        if puzzle!=None:
            sumKurangX=p.sumOfKurangdanX(puzzle)
            sumtext="SUM(Kurang)+X: "+str(sumKurangX)
            window["-SUM-"].update(sumtext)
            if (sumKurangX%2==0):
                p.solvePuzzle(puzzle)
                waktu="Waktu Eksekusi: "+str(p.waktuEksekusi) + " s"
                jumlah="Jumlah Simpul: "+str(p.jumlahSimpul)
                window["-TIME-"].update(waktu)
                window["-JUMLAH-"].update(jumlah)
                solved=True
            else: #jika nilai kurang +x ganjil
                text="Puzzle Tidak bisa diselesaikan"
                window["-TIME-"].update(text)
            if (solved):
                window["-LANGKAH-"].update("Langkah ke-1")

    if event=="-RESET-":#menekan tombol Reset
        puzzle=None
        window["-SUM-"].update("")
        window["-TIME-"].update("")
        window["-JUMLAH-"].update("")
        window["-LANGKAH-"].update("")
        solved=False
        index=0
        for i in range(16):
                window[f"-PUZZLE{i+1}-"].update("", size=(118, 118))

    if event=="-PREVIOUS-": #menekan tombol Previous
        if solved:
            if (index!=0):
                index-=1
                list=p.matrixToList(p.listSolusiPuzzle[index])
                for i in range(16):
                    if (list[i]==16):
                        window[f"-PUZZLE{i+1}-"].update("", size=(118, 118))
                    else:
                        window[f"-PUZZLE{i+1}-"].update(imgFolder+"\\"+str(list[i])+".png")
                window["-LANGKAH-"].update(f"Langkah ke-{index+1}")
                
    if event=="-NEXT-": #menekan tombol Next
        if solved:
            if (index!=len(p.listSolusiPuzzle)-1):
                index+=1
                list=p.matrixToList(p.listSolusiPuzzle[index])
                for i in range(16):
                    if (list[i]==16):
                        window[f"-PUZZLE{i+1}-"].update("", size=(118, 118))
                    else:
                        window[f"-PUZZLE{i+1}-"].update(imgFolder+"\\"+str(list[i])+".png")
                window["-LANGKAH-"].update(f"Langkah ke-{index+1}")
                

    