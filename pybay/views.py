from django.shortcuts import render

from .forms import CallForProposalForm
from pybay.faqs.models import Faq


def pybay_faq_index(request):
    faqs = Faq.objects.all()
    return render(request, 'frontend/faq.html', {'faqs': faqs})


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
