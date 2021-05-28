# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line


def farm_action(weather, time_of_day, milking_status, location, season, slurry, grass_status):
    if location == 'pasture' and ((time_of_day == 'night' or weather == 'rainy') or (milking_status == True or (slurry == True and (weather == 'rainy' or weather == 'neutral')) or (grass_status == True and season == 'spring' and weather == 'sunny'))):
        print('take cows to cowshed')
    if milking_status == True:
        print('milk cows')
    elif slurry == True and (weather == 'rainy' or weather == 'neutral'):
        print('fertilize pasture')
    elif grass_status == True and season == 'spring' and weather == 'sunny':
        print('mow grass')
    else:
        print('wait')
    if location == 'pasture' and (milking_status == True or (slurry == True and (weather == 'rainy' or weather == 'neutral')) or (grass_status == True and season == 'spring' and weather == 'sunny')):
        print('take cows back to pasture')