snake_position = [100, 50]
snake_position[0] += 10
print(snake_position)  # Result: [110, 50]
# snake_body = [[4, 10], [3, 10]]
# defining first 4 blocks of snake body
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
snake_body.insert(0, list(snake_position))
# Result: snake_body = [[5, 10], [4, 10], [3, 10]]
print(snake_body)
snake_body.pop()
print(snake_body)
snake_position[0] += 10
print(snake_position)  # Result: [120, 50]
snake_body.insert(0, list(snake_position))
print(snake_body)
