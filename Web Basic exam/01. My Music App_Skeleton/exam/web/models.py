from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from exam.web.validators import validate_only_letters_numbers_underscore, validation_positive_float_price


class Profile(models.Model):
    USER_NAME_MAX_LEN = 15
    USER_NAME_MIN_LEN = 2

    username = models.CharField(
            max_length = USER_NAME_MAX_LEN,
            validators = (
                    MinLengthValidator(USER_NAME_MIN_LEN),
                    validate_only_letters_numbers_underscore,
            ),
    )

    email = models.EmailField()
    age = models.PositiveIntegerField(
            blank = True,
            null = True,
    )


class Album(models.Model):
    ALBUM_NAME_MAX_LEN = 30
    ARTIST_MAX_LEN = 30
    GENRE_MAX_LEN = 30
    PRICE_MIN_VALUE_VALIDATOR = 0

    POP_MUSIC = "Pop Music"
    JAZZ_MUSIC = "Jazz Music"
    R_B_MUSIC = "R&B Music"
    ROCK_MUSIC = "Rock Music"
    COUNTRY_MUSIC = "Country Music"
    DANCE_MUSIC = "Dance Music"
    HIP_HOP_MUSIC = "Hip Hop Music"
    OTHER = 'Other'

    GENRE = (POP_MUSIC,
             JAZZ_MUSIC,
             R_B_MUSIC,
             ROCK_MUSIC,
             COUNTRY_MUSIC,
             DANCE_MUSIC,
             HIP_HOP_MUSIC,
             OTHER,)

    name = models.CharField(
            max_length = ALBUM_NAME_MAX_LEN,
            unique = True,
    )

    artist = models.CharField(
            max_length = ARTIST_MAX_LEN,
    )

    genre = models.CharField(
            max_length = GENRE_MAX_LEN if max(len(g) for g in GENRE) > GENRE_MAX_LEN else max(len(g) for g in GENRE),
            choices = ((g, g) for g in GENRE),

    )

    description = models.TextField(
            null = True,
            blank = True,
    )

    image_url = models.URLField()

    price = models.FloatField(
            validators = (
                    MinValueValidator(PRICE_MIN_VALUE_VALIDATOR),

                    # validation_positive_float_price,


            ),

    )
