from django.utils import timezone
from django.db import models
from django.urls import reverse


def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


class TaskItem(models.Model):
    title = models.CharField(max_length=100,  unique=True)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(default=one_week_hence)

    def get_absolute_url(self):
        return reverse(
            "index", args=[]
        )

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    def save(self, *args, **kwargs):
        # get number of tasks that have an overlapping start date
        items_overlapping_start = TaskItem.objects.filter(start_date__gte=self.start_date,
                                                                          start_date__lte=self.due_date).count()

        # get number of tasks that have an overlapping end date
        items_overlapping_end = TaskItem.objects.filter(due_date__gte=self.start_date,
                                                                        due_date__lte=self.due_date).count()

        overlapping_items_present = items_overlapping_start > 0 or items_overlapping_end > 0

        if overlapping_items_present:
            return
        else:
            super(TaskItem, self).save(*args, **kwargs)  # Call the "real" save() method.



    class Meta:
        ordering = ["due_date"]