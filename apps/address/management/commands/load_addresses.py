import requests
from address.models import City, Country, Township
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction


class Command(BaseCommand):
    """
        API information: https://github.com/dr5hn/countries-states-cities-database/tree/master
    """
    
    help = "This command will load country, city, and township data. You can specify which data to load using the flags --country, --city, --township. Example: python manage.py load_addresses --country --city --township"

    def add_arguments(self, parser):
        parser.add_argument(
            "--country",
            action="store_true",
            help="Load country data",
        )

        parser.add_argument(
            "--city",
            action="store_true",
            help="Load city data",
        )

        parser.add_argument(
            "--township",
            action="store_true",
            help="Load township data",
        )

    def handle(self, *args, **kwargs):
        country = kwargs.get("country")
        city = kwargs.get("city")
        township = kwargs.get("township")
        user = get_user_model().objects.filter(is_staff=True, is_superuser=True).first()
        if not user:
            raise CommandError("Superuser not found")

        try:
            if country:
                self.load_country(user)

            if city:
                self.load_city(user)

            if township:
                self.load_township(user)

        except Exception as e:
            raise CommandError(f"Error loading data: {e}")

    def load_country(self, user):
        """Load country data from the url and save it to the database"""

        # This url gets the github raw file of countries.json
        url = "https://raw.githubusercontent.com/dr5hn/countries-states-cities-database/refs/heads/master/json/countries.json"
        response = requests.get(url)

        try:
            countries = response.json()

            for country in countries:
                try:
                    with transaction.atomic():
                        check_country = Country.objects.filter(
                            alpha2Code=country["iso2"], alpha3Code=country["iso3"]
                        ).exists()

                        if not check_country:
                            country_obj = Country(
                                name=country["name"],
                                alpha2Code=country["iso2"],
                                alpha3Code=country["iso3"],
                                calling_code=country["phone_code"],
                            )
                            country_obj.save(user=user)

                            self.stdout.write(
                                self.style.SUCCESS(f"{country_obj.name} created")
                            )
                        else:
                            self.stdout.write(
                                self.style.WARNING(f"{country['name']} already exists")
                            )

                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(
                            f"Error processing country {country.get('name', 'unknown')}: {e}"
                        )
                    )

            self.stdout.write(self.style.SUCCESS("Countries loaded successfully"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error loading country data: {e}"))

    def load_city(self, user):
        """Load city data from the url and save it to the database"""

        # This url gets the github raw file of states.json
        url = "https://raw.githubusercontent.com/dr5hn/countries-states-cities-database/refs/heads/master/json/states.json"
        response = requests.get(url)

        try:
            cities = response.json()

            for city in cities:
                try:
                    with transaction.atomic():
                        country = Country.objects.filter(
                            alpha2Code=city["country_code"]
                        ).first()

                        check_city = City.objects.filter(
                            country=country, code=city["state_code"], name=city["name"]
                        ).exists()

                        if not check_city:
                            city_obj = City(
                                name=city["name"],
                                country=country,
                                code=city["state_code"],
                            )
                            city_obj.save(user=user)

                            self.stdout.write(
                                self.style.SUCCESS(f"{city_obj.name} created")
                            )
                        else:
                            self.stdout.write(
                                self.style.WARNING(f"{city['name']} already exists")
                            )

                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(
                            f"Error processing city {city.get('name', 'unknown')}: {e}"
                        )
                    )

            self.stdout.write(self.style.SUCCESS("Cities loaded successfully"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error loading city data: {e}"))

    def load_township(self, user):
        """Load township data from the url and save it to the database"""

        # This url gets the github raw file of cities.json
        url = "https://raw.githubusercontent.com/dr5hn/countries-states-cities-database/refs/heads/master/json/cities.json"
        response = requests.get(url)

        try:
            townships = response.json()

            for township in townships:
                try:
                    with transaction.atomic():
                        country = Country.objects.filter(
                            alpha2Code=township["country_code"]
                        ).first()

                        city = City.objects.filter(
                            name=township["state_name"], country=country
                        ).first()

                        if not city:
                            self.stdout.write(
                                self.style.ERROR(
                                    f"City {township['state_name']} not found"
                                )
                            )
                            continue

                        check_township = Township.objects.filter(
                            name=township["name"], city=city
                        ).exists()

                        if not check_township:
                            township = Township(
                                name=township["name"],
                                city=city,
                            )
                            township.save(user=user)

                            self.stdout.write(
                                self.style.SUCCESS(f"{township['name']} created")
                            )

                        else:
                            self.stdout.write(
                                self.style.WARNING(f"{township['name']} already exists")
                            )

                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(
                            f"Error processing township {township.name if hasattr(township, 'name') else 'unknown'}: {e}"
                        )
                    )

            self.stdout.write(self.style.SUCCESS("Townships loaded successfully"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error loading township data: {e}"))
