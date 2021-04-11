from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):

    ADULT = 'ADULT'
    JUVENILE = 'JUVENILE'

    AGE_CHOICES = (
            (ADULT, 'ADULT'),
            (JUVENILE, 'JUVENILE'),
        )


    AM = 'AM'
    PM = 'PM'

    TIME_CHOICES = (
            (AM, 'AM'),
            (PM, 'PM'),
        )


    GRAY = 'GRAY'
    CINNAMON = 'CINAMMON'
    BLACK = 'BLACK'

    COLOR_CHOICES = (
            (GRAY, 'GRAY'),
            (CINNAMON, 'CINNAMON'),
            (BLACK, 'BLACK'),
        )


    X = models.DecimalField(
            help_text=_('Longitude coordinate for squirrel sighting point'),
            max_digits=30,
            decimal_places=10,
            blank = True,
        )

    Y = models.DecimalField(
            help_text=_('Latitude coordinate for squirrel sighting point'),
            max_digits =30,
            decimal_places = 10,
            blank = True,
        )
    Unique_Squirrel_ID = models.CharField(
            help_text=_("Identification tag for each squirrel sightings. The tag is comprised of 'Hectare ID' + 'Shift' + 'Date' + 'Hectare Squirrel Number'"),
            max_length=50,
            primary_key = True,
        )

    Shift = models.CharField(
            help_text=_('Value is either "AM" or "PM" to communicate whether or not the sighting session occurred in the morning or late afternoon'),
            max_length=2,
            choices=TIME_CHOICES,
            blank = True,
        )
    Date = models.IntegerField(
            help_text=_('Concatenation of the sighting session day and month'),
            null = True,
            blank = True,
        )

    Age = models.CharField(
            help_text=_('Value is either "Adult" or "Juvenile"'),
            max_length=20,
            choices=AGE_CHOICES,
            blank=True,
        )

    Primary_Fur_Color = models.CharField(
            help_text=_('Value is either "Gray," "Cinnamon" or "Black"'),
            max_length = 10,
            choices = COLOR_CHOICES,
            blank = True,
        )


    GROUND_PLANE = 'GROUND PLANE'
    ABOVE_GROUND = 'ABOVE GROUND'

    LOCATION= (
            (GROUND_PLANE, 'GROUND PLANE'),
            (ABOVE_GROUND, 'ABOVE GROUND'),
        )

    Location = models.CharField(
            help_text=_('Value is either "Ground Plane" or "Above Ground"'),
            choices = LOCATION,
            blank = True,
            max_length = 30,
        )

    Specific_Location = models.CharField(
            help_text=_('Additional commentary for squirrel location'),
            blank = True,
            max_length = 100,
        )

    Running = models.BooleanField(
            help_text=_('Squirrel was seen running; Then True'),
            default=False,
        )

    Chasing = models.BooleanField(
            help_text=_('Squirrel was seen chasing another squirrel; Then True'),
            default=False,
         )
    Climbing = models.BooleanField(
            help_text=_('Squirrel was seen climbing a tree or other environmental landmark; Then True'),
            default=False,
        )
    Eating = models.BooleanField(
            help_text=_('Squirrel was seen eating; Then True'),
            default=False,
        )

    Foraging = models.BooleanField(
            help_text=_('Squirrel was seen foraging for food; Then True'),
            default=False,
        )

    Other_Activities = models.CharField(
            help_text=_('Any other activities squirrel was doing?'),
            blank=True,
            max_length = 200,
        )

    Kuks = models.BooleanField(
            help_text=_('Squirrel was heard kukking, a chirpy vocal communication used for a variety of reasons; if no then False'),
            default=False,
        )


    Quaas = models.BooleanField(
            help_text=_('Squirrel was heard quaaing, an elongated vocal communication which can indicate the presence of a ground predator such as a dog; if no then False'),
            default=False,
        )

    Moans = models.BooleanField(
            help_text=_('Squirrel was heard moaning, a high-pitched vocal communication which can indicate the presence of an air predator such as a hawk'),
            default=False,
        )

    Tail_flags = models.BooleanField(
            help_text=_('Squirrel was seen flagging its tail; if no then False'),
            default=False,
        )

    Tail_twitching = models.BooleanField(
            help_text=_('Squirrel was seen twitching its tail; if no then False'),
            default=False,
        )

    Approaches = models.BooleanField(
        help_text=_('Squirrel was seen approaching human, seeking food;if no then False'),
        default=False,
        )

    Indifferent = models.BooleanField(
            help_text=_('Squirrel was indifferent to human presence; if no then False'),
            default=False,
        )
    Runs_from = models.BooleanField(
            help_text=_('Squirrel was seen running from humans, seeing them as a threat; if no then False'),
            default=False,
        )

    def __str__(self):
        return self.Unique_Squirrel_ID

