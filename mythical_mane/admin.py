from django.contrib import admin
from .models import Universe, Owner, Patient, Employee, Visit, Diagnosis, ProcedureDefinition

@admin.register(Universe)
class UniverseAdmin(admin.ModelAdmin):
    list_display = ('universe_id', 'name')
    search_fields = ('name',)

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('owner_id', 'name', 'phone', 'email')
    search_fields = ('name', 'email', 'phone')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'name', 'color', 'dob', 'owner', 'universe')
    search_fields = ('name', 'color')
    list_filter = ('universe',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'job_role', 'specialty')
    search_fields = ('name', 'job_role')
    list_filter = ('job_role',)

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('visit_id', 'patient', 'vet', 'start_at', 'reason')
    list_filter = ('start_at', 'vet')
    date_hierarchy = 'start_at'

@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('diagnosis_id', 'name', 'code')
    search_fields = ('name', 'code')

@admin.register(ProcedureDefinition)
class ProcedureDefinitionAdmin(admin.ModelAdmin):
    list_display = ('procedure_id', 'name', 'standard_cost')
    search_fields = ('name',)