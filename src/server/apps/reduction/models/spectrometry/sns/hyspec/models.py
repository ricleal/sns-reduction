from __future__ import unicode_literals

import logging

from django.db import models
from django.core.validators import RegexValidator

from server.apps.configuration.models.spectrometry.sns.hyspec import Configuration
from server.apps.reduction.models import abstract


logger = logging.getLogger(__name__)  # pylint: disable=C0103


class ReductionHYSPEC(abstract.Reduction):


    configuration = models.ForeignKey(
        Configuration,
        on_delete=models.CASCADE,
        related_name="regions",
        related_query_name="region"
    )

    q_3d_validator = [
        RegexValidator(
            regex='^-?\d+,-?\d+,-?\d+$',
            message='Use: Qx,Qy,Qz',
            code='invalid_projection'
        ),
    ]

    # Fields

    ub_a = models.DecimalField(
        "a",
        max_digits=5,
        decimal_places=2
    )
    ub_b = models.DecimalField(
        "b",
        max_digits=5,
        decimal_places=2
    )
    ub_c = models.DecimalField(
        "c",
        max_digits=5,
        decimal_places=2
    )
    ub_alpha = models.IntegerField(
        "alpha",
    )
    ub_beta = models.IntegerField(
        "beta",
    )
    ub_gamma = models.IntegerField(
        "gamma",
    )

    ub_u_vector = models.CharField(
        u"u\u20D7",
        max_length=12,
        blank=True,
        help_text="UB u vector.",
        validators=q_3d_validator,
    )

    ub_v_vector = models.CharField(
        u"v\u20D7",
        max_length=12,
        blank=True,
        help_text="UB v vector.",
        validators=q_3d_validator,
    )

    q1_projection = models.CharField(
        "Q1 projection",
        max_length=12,
        blank=True,
        validators=q_3d_validator,
    )

    q2_projection = models.CharField(
        "Q2 projection",
        max_length=12,
        blank=True,
        validators=q_3d_validator,
    )
    q3_projection = models.CharField(
        "Q3 projection",
        max_length=12,
        blank=True,
        validators=q_3d_validator,
    )

    @models.permalink
    def get_absolute_url(self):
        return ('reduction:reduction_detail', [self.pk])


class RegionHYSPEC(abstract.Region):
    '''
    Region can be low, medium or high Q
    This will be a formset from Reduction
    '''

    reduction = models.ForeignKey(
        ReductionHYSPEC,
        on_delete=models.CASCADE,
        related_name="regions",
        related_query_name="region",)

    '''

plotParameters.append({'Name':'HHL',
                       'Axis0':'Q1',
                       'Axis0_min':-3,
                       'Axis0_max':3,
                       'Axis0_Nsteps':200,
                       'Axis1':'Q2',
                       'Axis1_min':-2,
                       'Axis1_max':5,
                       'Axis1_Nsteps':200,
                       'Axis2':'Q3',
                       'Axis2_min':-.5,
                       'Axis2_max':.5,
                       'Axis3':'DeltaE',
                       'Axis3_min':-2.5,
                       'Axis3_max':5.5})
    '''

    name = models.CharField(
        "Name",
        max_length=128,
        blank=True,
        help_text="Name of this plot."
    )

    AXIS_CHOICES = (
        ('Q1', 'Q1'),
        ('Q2', 'Q2'),
        ('Q3', 'Q3'),
        ('DE', 'DeltaE'),
    )

    axis_0 = models.CharField("Axis",max_length=2, choices=AXIS_CHOICES)
    min_0 = models.DecimalField("Min", max_digits=10, decimal_places=2)
    max_0 = models.DecimalField("Max", max_digits=10, decimal_places=2)
    nsteps_0 = models.IntegerField("#Steps", default=200,)

    axis_1 = models.CharField("Axis",max_length=2, choices=AXIS_CHOICES)
    min_1 = models.DecimalField("Min", max_digits=10, decimal_places=2)
    max_1 = models.DecimalField("Max", max_digits=10, decimal_places=2)
    nsteps_1 = models.IntegerField("#Steps", default=200,)

    axis_2 = models.CharField("Axis",max_length=2, choices=AXIS_CHOICES)
    min_2 = models.DecimalField("Min", max_digits=10, decimal_places=2)
    max_2 = models.DecimalField("Max", max_digits=10, decimal_places=2)
    nsteps_2 = models.IntegerField("#Steps", default=200,)

    axis_3 = models.CharField("Axis",max_length=2, choices=AXIS_CHOICES)
    min_3 = models.DecimalField("Min", max_digits=10, decimal_places=2)
    max_3 = models.DecimalField("Max", max_digits=10, decimal_places=2)
    nsteps_3 = models.IntegerField("#Steps", default=200,)


    def __str__(self):
        return "Plot {}".format(self.name)
