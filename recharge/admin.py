from django.contrib import admin
from .models import Mobile_recharge,Dth_recharge,Metro_recharge,Datacard_recharge
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class Change(ImportExportModelAdmin):
	list_display =('id','Enter_Your_Mobile_Number','Recharge_Type','Operator','Circle','Recharge_Amount','Currentuser')
	search_fields =('Recharge_Type',)

class Change2(ImportExportModelAdmin):
	list_display =('id','Select_DTH_Operator','Customer_id','Recharge_Amount','Currentuser')
	search_fields =('Customer_id',)

class Change3(ImportExportModelAdmin):
	list_display =('id','Select_Metro_Type','Card_Number','Recharge_Amount','Currentuser')
	search_fields =('Card_Number',)

class Change4(ImportExportModelAdmin):
	list_display =('id','Data_Card_Number','Select_Datacard_Operator','Recharge_Amount','Currentuser')
	search_fields =('Data_Card_Number',)


admin.site.register(Mobile_recharge,Change)
admin.site.register(Dth_recharge,Change2)
admin.site.register(Metro_recharge,Change3)
admin.site.register(Datacard_recharge,Change4)
