import FunctonS3 as FS3

bookre=[]
reven=[]

while True:
    print('LIBRERIA IBS\n')
    print('(1)Registrar libros\n(2)Libros registrados\n(3)Registrar venta\n(4)Ver reporte de ventas\n(5)generar .txt\n(6)salir de la app')
    op=0
    op=int(input( ))

    if op==1:
        FS3.registerbook(bookre)
    elif op==2:
        FS3.listar_libros(bookre)
    elif op==3:
        FS3.registrar_ventas(reven)
    elif op==4:
        FS3.reporte_ventas(reven)
    elif op==5:
        FS3.generate_txt()
    elif op==6:
        break