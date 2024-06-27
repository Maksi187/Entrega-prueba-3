#apv
#3 o 4 funciones app 


def registerbook(bookre):
    print("REGISTRAR LIBRO")
    nombrelibro=input("ingrese nombre del libro ")
    autorlibro=input("ingrese autor del libro ")
    genlibro=input("de que genero es su libro? ")
    preciouni=input("Ingrese valor del libro ")

    
    #dictionary
    bookre.append({
    'Nombre del libro': nombrelibro,
    'Autor': autorlibro,
    'Genero': genlibro,
    'Precio': preciouni
    })


    

def listar_libros(bookre):
    print('LISTADO DE LIBROS REGISTRADOS\n')
    print(bookre)
    

def registrar_ventas(reven):
    print('REGISTRAR VENTAS')
    nombrelibro=input("ingrese nombre del libro")
    cantventas=int(input('ingrese su numero de ventas'))
    preciouni=int(input('ingrese precio por unidad'))
    preciototal=cantventas * preciouni

    #venta
    reven.append({
        'Nombre del libro': nombrelibro,
        'Cantidad de ventas': cantventas,
        'Precio por unidad': preciouni,
        'Precio total': preciototal
    })
    
def reporte_ventas(reven):
    print('REPORTE DE VENTAS')
    print(reven)

def generate_txt():
    print('exportar regsitro a documento de texto')
    archive=reporte_ventas