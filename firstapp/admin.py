from django.contrib import admin, messages

from.models import Student
from.models import Coach
from.models import Project
from.models import MembershipInProject

class ProjectInLine(admin.TabularInline):
    model = Project
    fieldsets = [
        (None, {'fields': ['nom_du_projet']})
    ] #list columns
    extra = 1

class StudentAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email')
    fields = (('nom', 'prenom'), 'email')
    search_fields = ['nom', 'prenom']
    inlines = [ProjectInLine, ]

admin.site.register(Student, StudentAdmin)

class MembershipInline(admin.TabularInline):
    model = MembershipInProject
    extra = 2
class ProjetDureeListFilter(admin.SimpleListFilter):
    title = ('Duree')
    parameter_name = 'duree'

    def lookups(selfself, request, model_admin):
        return (
            ('1 month', ("moins d'un mois")),
            ('3 mois', ("Plus que 3 mois"))
        )
    def queryset (self, request, queryset):
        if self.value() == '1 month':
            return queryset.filter( duree_du_projet__lte = 30)
        if self.value() == '3 mois':
            return queryset.filter( duree_du_projet__lte = 90, duree_du_projet__gte = 30)

def set_Valid(modeladmin, request, queryset):
    queryset.update(est_valide=True)

set_Valid.short_description = "Valider"

class ProjectAdmin(admin.ModelAdmin):
    def set_to_Nvalid(self, request, queryset):
        rows_NValid = queryset.filter(est_valide=False)
        if rows_NValid.count() > 0:

          # messages.error(request, "%s projects valid= false"% rows_NValid.count())

            self.message_user(request,level="error", message="%s projects_valid=false" %rows_NValid.count())

        else:
            rows_updated = queryset.update(est_valide=False)
            if rows_updated == 1:
                message = "1 project was "
            else:
                message = "%s projects were" % rows_updated
            self.message_user(request,level="success", message="%s successfully marked as valid" %message)
    set_to_Nvalid.short_description = "Refuser"
    actions = [set_Valid,set_to_Nvalid]
    list_display = ('nom_du_projet','description','duree_du_projet','temps_alloue_par_le_createur','besoins','est_valide','createur','superviseur')
    fieldsets = (
    ('Etat',{'fields':('est_valide',)}),
    ('A propos',{
    'fields':('nom_du_projet',('createur','superviseur'),'besoins','description')
    }),
    ('duree',{
    'fields': (('duree_du_projet','temps_alloue_par_le_createur'),)

    }),
)
    inlines = (MembershipInline,)
    list_filter = ('createur', 'est_valide', ProjetDureeListFilter)
    list_per_page = 1
    actions_on_bottom = True
admin.site.register(Project, ProjectAdmin)

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email')
    fields = (('nom', 'prenom'), 'email')
    search_fields = ['nom', 'prenom']
    inlines = [ProjectInLine, ]
