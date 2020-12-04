import django
from django.db import models


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=("leaved at " + str(self.leaved_at)
                    if self.leaved_at else "not leaved")
                   )

    def get_duration(self):
        now = django.utils.timezone.localtime().replace(microsecond=0)
        if self.leaved_at:
            return self.leaved_at - self.entered_at

        return now - self.entered_at

    def is_visit_long(self, minutes=60):
        threshold = django.utils.timezone.timedelta(minutes=minutes)
        if self.get_duration() > threshold:
            return True

        return False
