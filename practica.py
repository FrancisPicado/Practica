print("Bienvenido a la libreria Fran")
print("La Liberia Fran está celebrando el día del libro Por esta razón está ofreciendo paquetes de libros condescuentos a sus clientes en los diferentes géneros de literatura que ofrece.")
print("El descuento se aplica según el tipo de género a los paquetes, de acuerdo con la siguiente tabla:")
print()
print("  Genero         Descuento    Precio")
print("1.Narrativo       25%         11000 ")
print("2.Lírico          15%         9000  ")
print("3.Dramático       5%          14000 ")
print("4.Didáctico       3%          25000 ")
print()
libro= int(input("Ingrese el numero de genero literario del libro que desea comprar"))
cantidad=int(input("Ingrese la cantidad de libros a comprar "))
Nombre=input("Ingrese su nombre")
Narrativo=11000
Lírico=9000
Dramático=14000
Didáctico=25000

total=4
genero=""
preciounitario=0
Descuento=0
if (libro==1):
    total=(cantidad*Narrativo-(0.25*(cantidad*Narrativo)))
    genero="Narrativo"
    preciounitario=Narrativo
    Descuento=(0.25*(cantidad*Narrativo))
elif (libro==2):
    total=(cantidad*Lírico-(0.15*(cantidad*Lírico)))
    genero="Lírico"
    preciounitario=Lírico
    Descuento=(0.15*(cantidad*Lírico))
elif (libro==3):
    total=(cantidad*Dramático-(0.05*(cantidad*Dramático)))
    genero="Dramático"
    preciounitario=Dramático
    Descuento=(0.05*(cantidad*Dramático))
elif (libro==4):
    total=(cantidad*Didáctico-(0.03*(cantidad*Didáctico)))
    genero="Didáctico"
    preciounitario=Didáctico
    Descuento=(0.03*(cantidad*Didáctico))
else:
   print("error")

print() 
if(total != 0 ):
    print("*******Libreria Fran********")
    print() 
    print("   FACTURA DE CONTADO  ")
    print() 
    print("Nombre del cliente  ",Nombre)
    print() 
    print("Genero              ",genero)
    print() 
    print("cantidad de libros  ",cantidad)
    print() 
    print("Precio unitario     ",preciounitario)
    print() 
    print("Subtotal            ",(preciounitario*cantidad))
    print() 
    print("Descuento           ",Descuento)
    print() 
    print("Precio final        ",total)
print()    
print("****Gracias por comprar en nuestra libreria****")
