# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 15:09:32 2021

@author: DEOWARDIMAN
"""

def celckelv(inp, unit):
    if unit == 'K':
        print(inp,' Kelvin akan dikonversi menjadi Celcius')
        unit = 'C'
        hasil = inp - 273
        return hasil, unit
    if unit == 'C':
        print(inp,' Celcius akan dikonversi menjadi Kelvin')
        unit = 'K'
        hasil = inp + 273
        return hasil, unit

def farenheit(inp, unit):
    if unit == 'K':
        print(inp,' Kelvin akan dikonversi menjadi Fahrenheit')
        unit = 'F'
        hasil = ((inp-273)*9/5)+32
        return hasil, unit        
    if unit == 'C':
        print(inp,' Celcius akan dikonversi menjadi Fahrenheit')
        unit = 'F'
        hasil = (inp*9/5)+32
        return hasil, unit
        



inputangka =input ('masukan angka ')
inputangka = int(inputangka)
inputunit =input ('masukan satuan ')

hasil, unit = celckelv(inputangka, inputunit)

print('Hasilnya adalah ',hasil,' ',unit)

hasilF, unitF = farenheit(hasil, unit)

print('Hasilnya adalah', hasilF, unitF)