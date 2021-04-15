import json

from django.shortcuts import render, redirect
from pyxlsb2 import open_workbook
from .models import Inventory
from .forms import ExcelForm

def home_view(request):
    return render(request, 'inventory/home.html')

def add_view(request):
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form = ExcelForm(request.POST, request.FILES) # Bound form
        if form.is_valid():
            excel_file = request.FILES['file']
            
            new_file = form.save(commit=False) # Guardar los datos en la base de datos
            
            lstRows = []
            totalQty = 0
            promedio = 0.0
            with open_workbook(excel_file) as wb:                
                with wb.get_sheet_by_index(0) as sheet:                    
                    for row in sheet.rows():
                        invent = []
                        for c in row:
                            invent.append(c.value)
                        lstRows.append(invent)

            items = 0
            for row in lstRows:
                items += 1
                Inventory.objects.create(serie=int(row[0]), number_elements=int(row[1]), price=row[2])
                totalQty += row[1]
                promedio += row[2]

            promedio = promedio / items
            
            summary = {'elementos' : totalQty, 'precio_promedio' : promedio}

            new_file.summary = json.dumps(summary)
            new_file.save()

            return redirect('home')
    else:
        form = ExcelForm() # Unbound form
    
    return render(request, 'inventory/form_file.html', {'form': form})

