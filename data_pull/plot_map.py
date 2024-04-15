import tkinter
import tkintermapview

#Tkinter window
root_tk = tkinter.Tk()
root_tk.geometry(f"{800}x{600}")
root_tk.title("GeoCaches Map view")

# create map widget
map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=600, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

map_widget.set_position(43.719987, -78.448507)
map_widget.set_zoom(7)

f = open("afew.txt",'r')

for line in f:
    try:
        line = line[line.find("-")+1:].replace("\n","")
        #print(line)
        coords = line.split(",")
        lat = coords[0]
        long = coords[1]
        #print("set coords")
        map_widget.set_position(float(lat),float(long),marker=True)
    except:
        pass

root_tk.mainloop()
