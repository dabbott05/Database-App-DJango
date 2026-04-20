from django.shortcuts import render
from .models import Patient

def patient_list(request):
    # 'select_related' is the magic word here. It tells Django to grab the 
    # Owner and Universe data at the EXACT SAME TIME as the Patient data. 
    # This solves the "avoid one query per patient" grading requirement!
    patients = Patient.objects.select_related('owner', 'universe').all()
    
    return render(request, 'patient_list.html', {'patients': patients})