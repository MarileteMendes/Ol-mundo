root.title("Estutura Base")

#Telas com cores diversas de proporções diferentes

frame_pagina = tk.Frame(root, bg= "tomato")
frame_pagina.place (relx= 0.1, rely=0, relwidth= 0.8, relheight=0.04)

frame_first = tk.Frame(root, bg= "lightblue")
frame_first.place (relx= 0.1, rely= 0.20,  relwidth= 0.8, relheight=0.1)

frame_second = tk.Frame(root, bg= "green")
frame_second.place (relx= 0.1, rely=0.30,  relwidth= 0.8, relheight=0.4)

frame_third= tk.Frame(root, bg= "yellow")
frame_third.place (relx= 0.1, rely= 0.73,  relwidth= 0.8, relheight=0.2)

#Nome de cada tela

label_pagina = tk.Label(frame_pagina, text= "Página de Código", font=("Impact", 12), bg="tomato")
label_pagina.place(relx=0.5, rely=0.4, anchor="center")

label_first= tk.Label(frame_first, text= "Primeiro Frame", font=("Roboto", 12), bg="lightblue")
label_first.place(relx=0.5, rely=0.4, anchor="center")


label_second= tk.Label(frame_second, text= "Segundo Frame", font=("Roboto", 12), bg="green")
label_second.place(relx=0.5, rely=0.4, anchor="center")

label_third= tk.Label(frame_third, text= "Terceiro Frame", font=("Roboto", 12), bg="yellow")
label_third.place(relx=0.5, rely=0.4, anchor="center")

root.mainloop()
