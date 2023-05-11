# Задача 2
# @tutorial https://wordsofwonders.ru/question/obem-mirovogo-okeana-soglasno-vikipedii-1340-74-mln-km³-srednyaya-plotnost-1-024-g-sm³-predpolozhim-chto-v-1-tonne-vodi-mirovogo-2/answer/255126

CUBIC_METERS_IN_CUBIC_KILOMETER = 1e9
KILOGRAM_PER_CUBIC_METER_IN_GRAMS_PER_CUBIC_CENTIMETER = 1e3
MILLIGRAM_IN_KILOGRAM = 1e6
KILOGRAM_IN_TON = 1e3

ocean_volume_in_cubic_kilometers = 1340.74e6
ocean_volume_in_cubic_meters = (
    ocean_volume_in_cubic_kilometers * CUBIC_METERS_IN_CUBIC_KILOMETER
)

ocean_density_in_grams_per_cubic_centimeter = 1.024
ocean_density_in_kilogram_per_cubic_meter = (
    ocean_density_in_grams_per_cubic_centimeter
    * KILOGRAM_PER_CUBIC_METER_IN_GRAMS_PER_CUBIC_CENTIMETER
)

ocean_mass_in_kilogram = (
    ocean_volume_in_cubic_meters * ocean_density_in_kilogram_per_cubic_meter
)

gold_in_milligram_per_water_in_ton = 5e-3
gold_in_kilogram_per_water_in_ton = (
    gold_in_milligram_per_water_in_ton / MILLIGRAM_IN_KILOGRAM
)
gold_in_kilogram_per_water_in_kilogram = (
    gold_in_kilogram_per_water_in_ton / KILOGRAM_IN_TON
)

gold_mass_in_kilogram = ocean_mass_in_kilogram * gold_in_kilogram_per_water_in_kilogram

gold_density_in_grams_per_cubic_centimeter = 19.32
gold_density_in_kilogram_per_cubic_meter = (
    gold_density_in_grams_per_cubic_centimeter
    * KILOGRAM_PER_CUBIC_METER_IN_GRAMS_PER_CUBIC_CENTIMETER
)

gold_volume_in_cubic_meters = (
    gold_mass_in_kilogram / gold_density_in_kilogram_per_cubic_meter
)

result_in_meters = round(gold_volume_in_cubic_meters ** (1 / 3))

print(result_in_meters)
