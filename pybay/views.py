from django.shortcuts import render

from .forms import CallForProposalForm
from symposion.sponsorship.models import Sponsor

from collections import defaultdict


def pybay_sponsors_list(request):
    active_sponsors = Sponsor.objects.filter(active=True).order_by('name')
    sponsor_map = defaultdict(list)

    for sponsor in active_sponsors:
        sponsor_map[sponsor.level.name].append(sponsor)

    return render(request, 'frontend/sponsors_list.html', {
        "bronze_sponsors": sponsor_map['Bronze'],
        "gold_sponsors": sponsor_map['Gold'],
        "silver_sponsors": sponsor_map['Silver'],
    })


def pybay_cfp_create(request):
    if request.method == 'POST':
        form = CallForProposalForm(request.POST)

        # Validate form
        if not form.is_valid():
            return render(request, 'frontend/cfp.html', {'form': form})

        # Create speaker and associated talk
        speaker, proposal = form.save_to_models()
        return render(request, 'frontend/cfp_submitted.html', {
            'speaker': speaker,
            'proposal': proposal,
        })

    else:
        form = CallForProposalForm()
        return render(request, 'frontend/cfp.html', {'form': form})
