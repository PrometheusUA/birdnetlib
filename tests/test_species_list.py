from birdnetlib.species import SpeciesList
from datetime import datetime


def test_species_list_for_analyzers():
    lon = -120.7463
    lat = 35.4244
    week_48 = 18
    filter_threshold = 0.03

    species = SpeciesList()
    species_list = species.return_list_for_analyzer(
        lon=lon, lat=lat, week_48=week_48, threshold=filter_threshold
    )
    assert len(species_list) == 195

    # Using datetime
    date = datetime(year=2022, month=5, day=10)

    species_list = species.return_list_for_analyzer(
        lon=lon, lat=lat, date=date, threshold=filter_threshold
    )
    assert len(species_list) == 195

    # Using no date or week_48
    species_list = species.return_list_for_analyzer(
        lon=lon, lat=lat, threshold=filter_threshold
    )
    assert len(species_list) == 269

    # Adjust time threshold
    date = datetime(year=2022, month=5, day=10)
    filter_threshold = 0.1
    species_list = species.return_list_for_analyzer(
        lon=lon, lat=lat, date=date, threshold=filter_threshold
    )
    assert len(species_list) == 110


def test_species_list():
    lon = -120.7463
    lat = 35.4244
    week_48 = 18
    filter_threshold = 0.03

    species = SpeciesList()
    species_list = species.return_list(
        lon=lon, lat=lat, week_48=week_48, threshold=filter_threshold
    )
    assert len(species_list) == 195
    print(species_list[0])
    assert species_list[0]["scientific_name"] == "Cathartes aura"
    assert species_list[0]["common_name"] == "Turkey Vulture"
