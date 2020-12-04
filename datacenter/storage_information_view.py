from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.utils import format_duration
from django.shortcuts import render


def storage_information_view(request):

    non_closed_visits = []
    for visitor in Visit.objects.filter(leaved_at=None):
        duration = format_duration(visitor.get_duration())
        non_closed_visits.append({
            'who_entered': visitor.passcard,
            'entered_at': visitor.entered_at,
            'duration': duration,
            'is_strange': visitor.is_visit_long(),
        })

    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
