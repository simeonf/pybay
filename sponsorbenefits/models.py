from django.db import models
from ordered_model.models import OrderedModel


class SponsorPackage(OrderedModel):
    text = models.CharField(max_length=255, help_text="Pre-conf, post conf, etc.")
    def __str__(self):
        return self.text


class SponsorCategory(OrderedModel):
    text = models.CharField(max_length=255, help_text="Diversity, Recruiting, Etc.")

    class Meta:
        verbose_name_plural = 'Sponsor categories'

    def __str__(self):
        return self.text


class SponsorLevel(OrderedModel):
    text = models.CharField(max_length=255, help_text="Champion, Partner, Etc")
    category = models.ForeignKey(SponsorCategory)
    price_text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Benefit(OrderedModel):
    package = models.ForeignKey(SponsorPackage)
    text = models.CharField(max_length=255, help_text="Job slot, Logo, etc")

    def __str__(self):
        return "%s - %s" % (self.package, self.text)

    def list_all_applies(self, all_levels):
        applies = self.benefitapplies_set.all()
        applies = {a.level: a for a in applies}
        for level in all_levels:
            yield applies.get(level, BenefitApplies.doesnotapply(level))


class BenefitApplies(models.Model):
    text = models.CharField(max_length=255, help_text="Number, description or checkmark")
    benefit = models.ForeignKey(Benefit)
    level = models.ForeignKey(SponsorLevel)

    @classmethod
    def doesnotapply(cls, level):
        return cls(text="", level=level)

    def __str__(self):
        return self.text


class AddOnBenefitRow(OrderedModel):
    title = models.CharField(max_length=255)
    price_text = models.CharField(max_length=255, default="", blank=True)


    def __str__(self):
        return self.title


class AlaCarteBenefitRow(OrderedModel):
    title = models.CharField(max_length=255)
    price_text = models.CharField(max_length=255, default="", blank=True)

    def __str__(self):
        return self.title


class ExplanationRow(OrderedModel):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title
