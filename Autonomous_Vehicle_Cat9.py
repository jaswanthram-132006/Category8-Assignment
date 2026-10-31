def fuzzy_speed_control(distance):
    if distance <= 10:
        near = 1.0
    elif distance < 30:
        near = (30 - distance) / 20
    else:
        near = 0.0

    if distance <= 10 or distance >= 50:
        medium = 0.0
    elif distance < 30:
        medium = (distance - 10) / 20
    else:
        medium = (50 - distance) / 20

    if distance <= 30:
        far = 0.0
    elif distance < 50:
        far = (distance - 30) / 20
    else:
        far = 1.0

    low_speed = 20
    moderate_speed = 50
    high_speed = 80

    total = near + medium + far

    if total == 0:
        return 0.0

    speed = (
        near * low_speed
        + medium * moderate_speed
        + far * high_speed
    ) / total

    return speed


distance = float(input("Enter obstacle distance in meters: "))

speed = fuzzy_speed_control(distance)

print(f"Obstacle distance: {distance} meters")
print(f"Recommended speed: {speed:.2f} km/h")