"""
Funciones para interactuar con la base de datos para el provedor.
https://towardsdatascience.com/creating-pdf-files-with-python-ad3ccadfae0f
https://pyfpdf.github.io/fpdf2/Tables.html
"""

"""
Se debe instalar el modulo FPDF con
python -m pip install fpdf2
"""

from time import process_time_ns
from fpdf import FPDF, HTMLMixin
from bd_conection import select

class PDF(FPDF, HTMLMixin):
    def __init__(self):
        self.pdf = FPDF(orientation = 'L')
    
    def add(self):
        self.pdf.add_page()

    def title(self, text):
        self.aux_conf(0.0, 0.0, 16, style="B")
        self.pdf.cell(300, 20, align='C', txt=text)

    def sub_title(self, text):
        self.aux_conf(0.0, 0.0, 11, c=(153,150,149))
        self.pdf.cell(300, 35, align='C', txt=text)

    def info_provedor(self, text, provedor):
        self.aux_conf(9, 40, 11)
        self.pdf.cell(0, 0, align="L", txt=text)
        self.aux_conf(30, 40, 11, style="U")
        self.pdf.cell(0, 0, align="L", txt=provedor)

    def fecha(self, text1, text2, fecha_pedido, fecha_pago):
        self.aux_conf(9 ,50, 11)
        self.pdf.cell(0, 0, align="L", txt=text1)
        self.aux_conf(41, 50, 11, style="U")
        self.pdf.cell(0, 0, align="L", txt=fecha_pedido)
        self.aux_conf(65, 50, 11)
        self.pdf.cell(0, 0, align="L", txt=text2)
        self.aux_conf(92, 50, 11, style="U")
        self.pdf.cell(0, 0, align="L", txt=fecha_pago)

    def condiciones_entrega(self, text, condicion):
        self.aux_conf(9, 55, 11)
        self.pdf.cell(0, 0, align="L", txt=text)
        self.aux_conf(50, 55, 11, style="U")
        self.pdf.cell(0, 0, align="L", txt=condicion)

    def escribir(self, x, y, text):
        self.aux_conf(x, y, 11)
        self.pdf.cell(0, 0, align="L", txt=text)
    
    def output(self, name):
        self.pdf.output('../Bases_de_Datos/Pedidos/{}.pdf'.format(name),'F')

    def aux_conf(self, x, y, size, font = "Arial",  style = "", c = (0,0,0)):
        self.pdf.set_xy(x,y)
        self.pdf.set_font(font, style=style, size=size)
        self.pdf.set_text_color(c[0],c[1],c[2])
    
    def tabla(self, TOTAL, data):
        cabecera = ["N°", "ARTÍCULO", "PRECIO UNITARIO", "CANTIDAD","PRECIO TOTAL"]
        # data = (
        #     ("First name", "Last name", "0","Age", "City"),
        #     ("Jules", "Smith", "34", "0","San Juan"),
        #     ("Mary", "Ramos", "45", "0","Orlando"),
        #     ("Carlson", "Banks", "19", "0","Los Angeles"),
        #     ("Lucas", "Cimon", "31", "0","Saint-Mahturin-sur-Loire"),
        #     ("First name", "Last name", "0","Age", "City"),
        #     ("Jules", "Smith", "34", "0","San Juan"),
        #     ("Mary", "Ramos", "45", "0","Orlando"),
        #     ("Carlson", "Banks", "19", "0","Los Angeles"),
        #     ("Lucas", "Cimon", "31", "0","Saint-Mahturin-sur-Loire"),
        # )
        # print(data)
        
        self.pdf.set_font("Times", size=10)
        line_height = self.pdf.font_size * 2.5
        self.pdf.ln(3)
        col_width = [self.pdf.epw*(2/28), self.pdf.epw*(17/28), self.pdf.epw*(3/28), self.pdf.epw*(3/28), self.pdf.epw*(3/28)]  # distribute content evenly
        for i in range(5):
            self.pdf.multi_cell(col_width[i], line_height, cabecera[i], border=1,
                new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)
        self.pdf.ln(line_height)
        for row in data:
            for i in range(len(row)):
                self.pdf.multi_cell(col_width[i], line_height, row[i], border=1,
                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)
            self.pdf.ln(line_height)
        for i in range(len(cabecera)):
            if i < 3 :
                self.pdf.multi_cell(col_width[i], line_height, "", border=0,
                    new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)
            elif i == 3:  
                self.pdf.multi_cell(col_width[i], line_height, "COSTO TOTAL", border=0,
                    new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)
            else:
                self.pdf.multi_cell(col_width[i], line_height, TOTAL, border=1,
                    new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)
        self.pdf.ln(line_height*5)

def escribir_pdf(provedor, lista_productos, fecha_pedido, fecha_pago, total, nombre):
    p = PDF()
    p.add()
    p.title("Empresa XYZ S.A")
    p.sub_title("NIC: XXXXXXXXXX")
    p.info_provedor("Proveedor: ", "{:30}".format(provedor))
    p.fecha("Fecha del Pedido: ", "Fecha de pago:" , fecha_pedido, fecha_pago)
    p.condiciones_entrega("Términos de entrega: ", "En las instalaciones de la empresa xyz")
    p.escribir(9, 67, "Sirvanse por este medio se piden los siguientes artículos")
    p.tabla(total, lista_productos)
    p.escribir(9, -20, "Elaborado Por:__________________________ Autorizado Por:__________________________ Recibido Por:__________________________")
    p.output(nombre)

def datos(tupla, fecha1, fecha2):
    while len(tupla) >= 0:
        sql = """SELECT provedor.nombre, producto.nombre, prodOfrecido.precioUnitario, producto.capacidad - producto.cantidad, (producto.capacidad - producto.cantidad) * prodOfrecido.precioUnitario, producto.codigoBarra
                FROM (provedor INNER JOIN prodOfrecido ON (provedor.codigo = prodOfrecido.idProvedor)) INNER JOIN Producto ON (Producto.codigoBarra = prodOfrecido.idProducto)
                WHERE prodOfrecido.idProducto IN %s"""
        ans = select(sql, [tupla])
        if len(ans) == 0: break
        dato = {}
        sub_total = 0
        for row in ans:
            key = str(row[0]).strip(" ")
            p_name, pre_uni, cant, total = str(row[1]).strip(" "), str(row[2]).strip(" "), str(row[3]).strip(" "), str(row[4]).strip(" ") 
            temp, sub_total = [0, p_name, pre_uni, cant, total], sub_total + int(total)
            if key in dato: 
                dato[key][0].append(temp)
                dato[key][1] += 1
                dato[key][2].append(str(row[5]).strip(" "))
            else: dato[key] = [[temp], 1, [str(row[5]).strip(" ")]]
        dat = sorted(dato.items(), key=lambda x: x[1][1], reverse=True)
        if len(dat) != 0:
            temp = dat[0]
            tupla = list(tupla)
            for i in range(len(temp[1][0])):
                temp[1][0][i][0] = str(i+1)
                print(temp[1][2][i])
                tupla.remove(int(temp[1][2][i]))
            tupla = tuple(tupla)
            escribir_pdf(temp[0], temp[1][0], fecha1, fecha2, str(sub_total),"Pedido_{}_{}".format(temp[0], fecha1))

