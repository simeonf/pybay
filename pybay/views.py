from django.shortcuts import render

from .forms import CallForProposalForm


def pybay_cfp_create(request):
    if request.method == 'POST':
        form = CallForProposalForm(request.POST)

        # Validate form
        if not form.is_valid():
            return render(request, 'cfp.html', {'form': form})

        # Create speaker and associated talk
        speaker, proposal = form.save_to_models()
        return render(request, 'cfp_submitted.html', {
            'speaker': speaker,
            'proposal': proposal,
        })

    else:
        form = CallForProposalForm()
        return render(request, 'cfp.html', {'form': form})
