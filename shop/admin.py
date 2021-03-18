from django.contrib import admin
from .models import Beat, BasicLicense, PremiumLicense, PremiumPlusLicense, UnlimitedLicense, ExclusiveLicense, Order, OrderItem, PageLink, ContactRequest


class BasicLicenseInline(admin.StackedInline):
    model = BasicLicense
    extra = 0


class PremiumLicenseInline(admin.StackedInline):
    model = PremiumLicense
    extra = 0


class PremiumPlusLicenseInline(admin.StackedInline):
    model = PremiumPlusLicense
    extra = 0


class UnlimitedLicenseInline(admin.StackedInline):
    model = UnlimitedLicense
    extra = 0


class ExclusiveLicenseInline(admin.StackedInline):
    model = ExclusiveLicense
    extra = 0


class BeatAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Beat', {'fields': ['title', 'keywords', 'video', 'bpm', 'beat_length', 'tone_type', 'thumbnail', 'mp3_file', 'wav_file']})
    ]
    inlines = [BasicLicenseInline, PremiumLicenseInline, PremiumPlusLicenseInline, UnlimitedLicenseInline, ExclusiveLicenseInline]




admin.site.register(Beat, BeatAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(PageLink)
admin.site.register(ContactRequest)




