from geopy import distance
import json
# 51°30′26″N 0°7′39″W
LONDON_LATITUDE = 51 + (30 / 60) + (26 / 60 / 60)
# 0°7′39″W
LONDON_LONGITUDE = -((7 / 60.0) - (39 / 60.0 / 60.0))
LONDON_COORDS = (LONDON_LATITUDE, LONDON_LONGITUDE)

def users_in_radius(users, radius):

    valid_users = list()

    for user in users:
        user_lat = user["latitude"]
        user_lon = user["longitude"]

        user_coords = (user_lat, user_lon)

        distance_from_london = distance.distance(LONDON_COORDS, user_coords).miles

        if distance_from_london <= radius:
            # add user to valid list
            valid_users.append(user)
    
    return valid_users