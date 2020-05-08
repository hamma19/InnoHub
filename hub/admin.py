from django.contrib import admin, messages

# Register your models here.


from hub.models import *



class ProjectInline(admin.TabularInline):
    model= Projet
    fieldsets = [
        (None,{'fields':['nom_projet']})
    ]
    extra = 0


class StudentAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'mail',)
    fields = (('nom', 'prenom'), 'mail',)
    search_fields = ["nom","prenom"]
    ordering = ['-nom']
    inlines = [ProjectInline]


class ProjetDureeListFilter(admin.SimpleListFilter):
    title =('Duree')
    parameter_name='duree'


    def lookups(self,request,model_admin):
        return (
            ('1 month',("moins d'un mois")),
            ('3 months', ("Plus qu'un mois"))
        )
    def queryset(self,request,queryset):
        if self.value()=='1 month':
            return queryset.filter(duree__lte=30)
        if self.value()=='3 months':
            return queryset.filter(duree__gte=30,duree__lte=90)


class MemberShipInline(admin.StackedInline):
    model = MembershipInProject
    extra = 1


def set_valid(modeladmin,request,queryset):
    queryset.update(est_valide=True)

set_valid.short_description ="Valider"

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("nom_projet","description","duree","temps_allouee","besoins","est_valide","createur","superviseur")
    fieldsets = (
        ('Etat',{'fields':('est_valide',)}),
        ('A propos',{
            'classes':('collapse'),
            'fields':('nom_projet',('createur','superviseur'),'besoins','description')

        }),
        ('duree',{
            'fields': (('duree','temps_allouee'),)

        }),

    )

    def set_to_Nvalid(self,request,queryset):
        rows_NValid=queryset.filter(est_valide=False)
        if rows_NValid.count()>0:
            messages.error(request,"%s projects valid=false"%rows_NValid.count())
        else:
            rows_updated=queryset.update(est_valide=False)
            if rows_updated==1:
                message="1 project was"
            else:
                message="%s projects were" % rows_updated
            self.message_user(request,level='success',message="%s successfully marked as not valid"%message)

    set_to_Nvalid.short_description = "Refuser"

    inlines = [MemberShipInline]
    actions = [set_valid,'set_to_Nvalid']
    list_filter = ('createur','est_valide',ProjetDureeListFilter)
    list_per_page = 1  #PAGINATION
    actions_on_bottom = True
    actions_on_top = False







admin.site.register(Etudiant,StudentAdmin)
admin.site.register(Coach)
admin.site.register(Projet,ProjectAdmin)
admin.site.register(MembershipInProject)








