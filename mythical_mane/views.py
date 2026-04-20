from django.shortcuts import render
from .models import Patient
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Patient, Owner

# --- Existing Patient View ---
def patient_list(request):
    patients = Patient.objects.select_related('owner', 'universe').all()
    return render(request, 'patient_list.html', {'patients': patients})

# --- New Owner CRUD Views ---

# 1. READ (List)
class OwnerListView(ListView):
    model = Owner
    template_name = 'owner_list.html'
    context_object_name = 'owners'

# 2. CREATE
class OwnerCreateView(CreateView):
    model = Owner
    template_name = 'owner_form.html'
    # These are the fields the user is allowed to fill out
    fields = ['name', 'phone', 'email', 'address', 'universe']
    # Where to redirect after successfully creating an owner
    success_url = reverse_lazy('owner_list')

# 3. UPDATE
class OwnerUpdateView(UpdateView):
    model = Owner
    template_name = 'owner_form.html' # Reuses the same form as Create!
    fields = ['name', 'phone', 'email', 'address', 'universe']
    success_url = reverse_lazy('owner_list')

# 4. DELETE
class OwnerDeleteView(DeleteView):
    model = Owner
    template_name = 'owner_confirm_delete.html'
    success_url = reverse_lazy('owner_list')


def patient_list(request):
    # 'select_related' is the magic word here. It tells Django to grab the 
    # Owner and Universe data at the EXACT SAME TIME as the Patient data. 
    # This solves the "avoid one query per patient" grading requirement!
    patients = Patient.objects.select_related('owner', 'universe').all()
    
    return render(request, 'patient_list.html', {'patients': patients})