from django.db import models
from django import forms


class Beat(models.Model):
    title = models.CharField(max_length=30)
    keywords = models.CharField(blank=True, null=True, max_length=120)
    bpm = models.CharField(blank=True, null=True, max_length=120)
    beat_length = models.CharField(blank=True, null=True, max_length=120)
    tone_type = models.CharField(blank=True, null=True, max_length=120)

    video = models.CharField(blank=True, null=True, max_length=200, help_text="Youtube embed code")
    thumbnail = models.ImageField(blank=True, null=True, upload_to='beat_thumbnails')
    mp3_file = models.FileField(blank=True, null=True, upload_to='mp3_files')
    wav_file = models.FileField(blank=True, null=True, upload_to='wav_files')

    def __str__(self):
        return self.title


class License(models.Model):
    beat = models.ForeignKey(Beat, on_delete=models.CASCADE)

    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

    class Meta:
        abstract = True


class BasicLicense(License):
    title = models.CharField(default='Basic License', max_length=70, editable=False)

    price = models.DecimalField(default=29.90, decimal_places=2, max_digits=8)

    num_distribution_copies = models.CharField(default='2000', max_length=10)
    num_free_downloads = models.CharField(default='Unlimited', max_length=10)

    num_audio_streams = models.CharField(default='500000', max_length=10)
    num_music_videos = models.CharField(default='1', max_length=10)

    num_non_monetized_video_streams = models.CharField(default='500000', max_length=10)
    num_monetized_video_streams = models.CharField(default='1', max_length=10)

    broadcoasting_rights = models.BooleanField(default=True, choices=License.BOOL_CHOICES)
    num_radio_stations = models.CharField(default='2', max_length=10)

    allow_profit_performances = models.BooleanField(default=True, choices=License.BOOL_CHOICES)
    num_not_for_profit_performances = models.CharField(default='Unlimited', max_length=10)

    beats_publishing_percentage = models.CharField(null=True, blank=True, max_length=10)
    beats_hook_publishing_percentage = models.CharField(null=True, blank=True, max_length=10)
    top_lines_vocals_publishing_percentage = models.CharField(null=True, blank=True, max_length=10)


class PremiumLicense(License):
    title = models.CharField(default='Premium License', max_length=70, editable=False)

    price = models.DecimalField(default=49.90, decimal_places=2, max_digits=8)

    num_distribution_copies = models.CharField(default='10000', max_length=10)
    num_free_downloads = models.CharField(default='Unlimited', max_length=10)

    num_audio_streams = models.CharField(default='1000000', max_length=10)
    num_music_videos = models.CharField(default='1', max_length=10)

    num_non_monetized_video_streams = models.CharField(default='Unlimited', max_length=10)
    num_monetized_video_streams = models.CharField(default='1', max_length=10)

    broadcoasting_rights = models.BooleanField(default=True, choices=License.BOOL_CHOICES)
    num_radio_stations = models.CharField(default='2', max_length=10)

    allow_profit_performances = models.BooleanField(default=True, choices=License.BOOL_CHOICES)
    num_not_for_profit_performances = models.CharField(default='Unlimited', max_length=10)

    beats_publishing_percentage = models.CharField(null=True, blank=True, max_length=10)
    beats_hook_publishing_percentage = models.CharField(null=True, blank=True, max_length=10)
    top_lines_vocals_publishing_percentage = models.CharField(null=True, blank=True, max_length=10)


class PremiumPlusLicense(License):
    title = models.CharField(default='Premium Plus License', max_length=70, editable=False)

    price = models.DecimalField(default=99.90, decimal_places=2, max_digits=8)

    num_distribution_copies = models.CharField(default='100000', max_length=10)
    num_free_downloads = models.CharField(default='Unlimited', max_length=10)

    num_audio_streams = models.CharField(default='10000000', max_length=10)
    num_music_videos = models.CharField(default='2', max_length=10)

    num_non_monetized_video_streams = models.CharField(default='Unlimited', max_length=10)
    num_monetized_video_streams = models.CharField(default='2', max_length=10)

    broadcoasting_rights = models.BooleanField(default=True, choices=License.BOOL_CHOICES)
    num_radio_stations = models.CharField(default='2', max_length=10)

    allow_profit_performances = models.BooleanField(default=True, choices=License.BOOL_CHOICES)
    num_not_for_profit_performances = models.CharField(default='Unlimited', max_length=10)

    beats_publishing_percentage = models.CharField(null=True, blank=True, max_length=10)
    beats_hook_publishing_percentage = models.CharField(null=True, blank=True, max_length=10)
    top_lines_vocals_publishing_percentage = models.CharField(null=True, blank=True, max_length=10)


class UnlimitedLicense(License):
    title = models.CharField(default='Unlimited License', max_length=70, editable=False)

    price = models.DecimalField(default=199.90, decimal_places=2, max_digits=8)

    num_distribution_copies = models.CharField(default='Unlimited', max_length=10)
    num_free_downloads = models.CharField(default='Unlimited', max_length=10)

    num_audio_streams = models.CharField(default='Unlimited', max_length=10)
    num_music_videos = models.CharField(default='Unlimited', max_length=10)

    num_non_monetized_video_streams = models.CharField(default='Unlimited', max_length=10)
    num_monetized_video_streams = models.CharField(default='Unlimited', max_length=10)

    broadcoasting_rights = models.BooleanField(default=True, choices=License.BOOL_CHOICES)
    num_radio_stations = models.CharField(default='2s', max_length=10)

    allow_profit_performances = models.BooleanField(default=True, choices=License.BOOL_CHOICES)
    num_not_for_profit_performances = models.CharField(default='Unlimited', max_length=10)

    beats_publishing_percentage = models.CharField(null=True, blank=True, max_length=10)
    beats_hook_publishing_percentage = models.CharField(null=True, blank=True, max_length=10)
    top_lines_vocals_publishing_percentage = models.CharField(null=True, blank=True, max_length=10)


class ExclusiveLicense(License):
    title = models.CharField(default='Exclusive License', max_length=70, editable=False)

    price = models.DecimalField(default=499.90, decimal_places=2, max_digits=8)

    num_distribution_copies = models.CharField(default='Unlimited', max_length=10)
    num_free_downloads = models.CharField(default='Unlimited', max_length=10)

    num_audio_streams = models.CharField(default='Unlimited', max_length=10)
    num_music_videos = models.CharField(default='Unlimited', max_length=10)

    num_non_monetized_video_streams = models.CharField(default='Unlimited', max_length=10)
    num_monetized_video_streams = models.CharField(default='Unlimited', max_length=10)

    broadcoasting_rights = models.BooleanField(default=True, choices=License.BOOL_CHOICES)
    num_radio_stations = models.CharField(default='2s', max_length=10)

    allow_profit_performances = models.BooleanField(default=True, choices=License.BOOL_CHOICES)
    num_not_for_profit_performances = models.CharField(default='Unlimited', max_length=10)

    beats_publishing_percentage = models.CharField(default=50, max_length=10)
    beats_hook_publishing_percentage = models.CharField(default=35, max_length=10)
    top_lines_vocals_publishing_percentage = models.CharField(default=0, max_length=10)


class Order(models.Model):
    date_ordered = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, null=True)
    customer = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.transaction_id)


class OrderItem(models.Model):
    beat = models.ForeignKey(Beat, on_delete=models.SET_NULL, null=True)
    license = models.CharField(max_length=100, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    license_pdf = models.FileField(blank=True, null=True, upload_to='license_pdfs')

    def __str__(self):
        return str(f"{self.beat},  {self.license}")


class PageLink(models.Model):
    title = models.CharField(max_length=30)
    thumbnail = models.ImageField(blank=True, null=True, upload_to='page-link_thumbnails', help_text="Muss Querformat haben")

    def __str__(self):
        return self.title


class ContactRequest(models.Model):
    email_address = models.CharField(max_length=200, default="empty")
    subject = models.CharField(max_length=200, default="empty")
    content = models.CharField(max_length=2000, default="empty")
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
