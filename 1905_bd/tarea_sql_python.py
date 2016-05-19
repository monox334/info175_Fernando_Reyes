#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

bdatos = sqlite3.connect('pos_empresa.db')

cursor = bdatos.cursor()

print ("La base de datos se abrio correctamente")

cursor = bdatos.execute("SELECT COUNT(*) FROM sale WHERE date LIKE \"2013%\";")
for row in cursor:
    print ("Venta total 2013 = ",row[0])
print 
print

cursor = bdatos.execute("SELECT product.name,AVG(sale_product.net_unit_price) AS \"Precio promedio de ventas por producto\" FROM sale_product JOIN product ON product.id = sale_product.product_id GROUP BY product.id LIMIT 10;")
for row in cursor:
    print ("nombre del producto = " ,row[0])
    print ("Precio promedio de venta = ",row[1],"\n")
		print
print
print

cursor = bdatos.execute("SELECT entity.names,entity.surnames,entity.company_name,SUM(gross_total) FROM sale JOIN entity ON entity.id = sale.entity_id GROUP BY entity_id LIMIT 10;")
print("total de ventas por cliente: ")
for row in cursor:
    print("nombres: ",row[0])
    print("apellidos: ",row[1])
    print("compañia: ",row[2])
    print("total de ventas: ",row[3],"\n")
		print
print
print

cursor = bdatos.execute("SELECT entity.names,entity.surnames,entity.company_name,SUM(gross_total) FROM sale JOIN entity ON entity.id = sale.entity_id WHERE sale.date BETWEEN '2014-01-01' AND '2014-12-31' GROUP BY entity_id LIMIT 1;")
print("total de ventas por cliente en el año 2014: ")
for row in cursor:
    print("nombres: ",row[0])
    print("apellidos: ",row[1])
    print("compañia: ",row[2])
    print("total de ventas : ",row[3],"\n")
		print

print
print

cursor = bdatos.execute("SELECT date, COUNT(*), SUM(gross_total) FROM sale WHERE date LIKE \"2013-11%\" GROUP BY date;")
print ("Total de ventas por fecha en noviembre del 2013:")
for row in cursor:
	print ("Fecha: ",row[0])
	print ("Cantidad de ventas: ",row[1])
	print ("Total ventas: ",row[2],"\n")
	print

print
print

cursor = bdatos.execute("SELECT product.name, sale_product.quantity, sale_product.gross_total FROM sale_product JOIN product ON sale_product.product_id = product.id ORDER BY sale_product.quantity DESC LIMIT 1;")
print ("Cantidad y montos totales por producto:")
for row in cursor:
	print ("Producto: ",row[0])
	print ("Cantidad: ",row[1])
	print ("Total ventas: ",row[2],"\n")
	print

print
print
