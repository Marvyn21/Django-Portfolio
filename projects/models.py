from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class ProjectModel(models.Model):
    name = models.CharField(max_length=265, blank=False, null=False)
    languages = models.ManyToManyField("Language", verbose_name=_(""))
    technologies = models.ManyToManyField("Technology", verbose_name=_(""))

class Language(models.Model):
    name= models.CharField(_(""), max_length=50, blank=False, null=False)
    class Meta:
        verbose_name = _("Language")
        verbose_name_plural = _("Languages")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Language_detail", kwargs={"pk": self.pk})

class Technology(models.Model):
    name = models.CharField(_(""), max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = _("Technology")
        verbose_name_plural = _("Technologyies")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Technology_detail", kwargs={"pk": self.pk})
