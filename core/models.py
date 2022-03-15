from django.db import models
import datetime


class Appointment(models.Model):
    doctor_name = models.CharField(
        max_length=255,
        verbose_name="Doctor"
    )
    patient_name = models.CharField(
        max_length=255,
        verbose_name="Patient"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description"
    )
    date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Date"
    )

    class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"

    def __str__(self):
        return f'{self.doctor_name} - {self.patient_name}'

    def save(self, *args, **kwargs):
        date_today = datetime.datetime.now().date()

        if self.date < date_today:
            raise Exception("La fecha de la cita no puede ser en el pasado")

        super(Appointment, self).save(*args, **kwargs)
