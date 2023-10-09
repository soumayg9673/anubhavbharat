from django.contrib import admin

from indrail import models as IRMdl

class RailwayDivAdmin(admin.TabularInline):
    model = IRMdl.Div
    extra = 0

@admin.register(IRMdl.Zone)
class RailwayZoneConfig(admin.ModelAdmin):
    list_display = ('code','name','divisions','railway_stations')
    inlines = [RailwayDivAdmin]

    def divisions(self, obj):
        return IRMdl.Div.objects.filter(zone=obj).count()

    def railway_stations(self, obj):
        return IRMdl.Station.objects.filter(zone=obj).count()


class RailwayStationAdmin(admin.TabularInline):
    model = IRMdl.Station
    extra = 0

@admin.register(IRMdl.Div)
class RailwayDivConfig(admin.ModelAdmin):
    search_fields = ['zone__name','name']
    list_display = ('name','zone','railway_stations')
    inlines = [RailwayStationAdmin]

    def railway_stations(self, obj):
        return IRMdl.Station.objects.filter(div=obj).count()

admin.site.register(IRMdl.StationCat)

class ShopAdmin(admin.TabularInline):
    model = IRMdl.Shop
    fields = ['name','plt1','plt2','is_open','is_active','is_verified']
    extra = 0

@admin.register(IRMdl.Station)
class RailwayStationConfig(admin.ModelAdmin):
    search_fields = ['code','name','zone__name','div__name']
    list_display = ('code','name','div','zone')
    fieldsets = (
        ('Railway Station', {'fields':('zone','div','code','name','cat')}),
    )
    inlines = [ShopAdmin]


class ShopLicAdmin(admin.TabularInline):
    model = IRMdl.ShopLic
    extra = 0

class ShopEmpAdmin(admin.TabularInline):
    model = IRMdl.ShopEmp
    extra = 0

@admin.register(IRMdl.Shop)
class ShopConfig(admin.ModelAdmin):
    fieldsets = (
        ('SHOP', {'fields':('org','name','shop_no','img','contact_no')}),
        ('INDIAN RAILWAYS', {'fields':('station','plt1','plt2','lat','lon')}),
        ('PAYMENT', {'fields':('is_cash','is_card','is_upi')}),
        ('STATUS', {'fields':('is_open','is_active','is_verified')}),
    )
    raw_id_fields = ['station']
    inlines = [ShopLicAdmin,ShopEmpAdmin]
