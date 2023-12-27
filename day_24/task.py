# read input
with open("input.txt", "r") as file:
    lines = file.readlines()

# remove newline characters
lines = [line.strip() for line in lines]

hailstones = []
for line in lines:
    positions, velocities = line.split('@')
    # split positions on comma and cast to int
    positions = [int(pos) for pos in positions.split(',')]
    # split velocities on comma and cast to int
    velocities = [int(vel) for vel in velocities.split(',')]
    # append to hailstones
    hailstones.append((positions, velocities))
print(hailstones)

# Task 1

x_bounds = (200000000000000, 400000000000000)
y_bounds = (200000000000000, 400000000000000)


def check_ray_intersection(R1, D1, R2, D2):
    # Check if rays are parallel (cross product is zero)
    cross_product = D1[0] * D2[1] - D1[1] * D2[0]
    if cross_product == 0:
        return False  # Rays are parallel and do not intersect

    # Compute potential intersection point
    t = ((R2[0] - R1[0]) * D2[1] - (R2[1] - R1[1]) * D2[0]) / cross_product
    u = -((R1[0] - R2[0]) * D1[1] - (R1[1] - R2[1]) * D1[0]) / cross_product

    # Check if the intersection point is along the direction of both rays
    if t >= 0 and u >= 0:
        intersection = (R1[0] + t * D1[0], R1[1] + t * D1[1])
        if x_bounds[0] <= intersection[0] <= x_bounds[1] and y_bounds[0] <= intersection[1] <= y_bounds[1]:
            return True
    return False

num_intersections = 0
for i in range(len(hailstones)):
    for j in range(i + 1, len(hailstones)):
        if check_ray_intersection(hailstones[i][0], hailstones[i][1], hailstones[j][0], hailstones[j][1]):
            num_intersections += 1
print(num_intersections)


