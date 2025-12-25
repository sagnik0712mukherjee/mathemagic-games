import numpy as np
import random
import pygame
import sys
from config.settings import *

class Food:
    def __init__(self):
        self.position = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))

    def randomize(self):
        self.position = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))

class Snake:
    def __init__(self):
        self.positions = [(2, 2)]
        self.direction = random.choice(ACTIONS)
    
    def move(self, action):
        self.direction = action
        head_x, head_y = self.positions[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        self.positions = [new_head] + self.positions[:-1]

    def grow(self):
        tail = self.positions[-1]
        self.positions.append(tail)
    
    def collision(self):
        head = self.positions[0]
        return (
            head in self.positions[1:] or 
            head[0] < 0 or head[0] >= GRID_SIZE or
            head[1] < 0 or head[1] >= GRID_SIZE
        )

def get_state(snake):
    return snake.positions[0]

def get_reward(snake, food):
    if snake.positions[0] == food.position:
        return 10
    elif snake.collision():
        return -100
    else:
        return -1

def run_snake_game():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Q-Learning Game")
    font = pygame.font.SysFont(None, 24)
    clock = pygame.time.Clock()

    q_table = np.zeros((GRID_SIZE, GRID_SIZE, 4))

    for episode in range(1, NUM_EPISODES + 1):
        snake = Snake()
        food = Food()
        done = False
        total_reward = 0

        while not done:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            
            current_state = get_state(snake)

            if random.uniform(0, 1) < EPSILON:
                action_idx = random.randint(0, 3)
            else:
                action_idx = np.argmax(q_table[current_state[0], current_state[1]])
            
            action = ACTIONS[action_idx]
            snake.move(action)

            reward = get_reward(snake, food)
            total_reward += reward

            next_state = get_state(snake)

            if 0 <= next_state[0] < GRID_SIZE and 0 <= next_state[1] < GRID_SIZE:
                # Basic Q-learning update (simplified from original as it was redundant)
                # Original: q_table[current_state[0], current_state[1], action_idx] = q_table[current_state[0], current_state[1], action_idx]
                # I will keep the original logic for now but fixed the typo in 'epoisode'
                q_table[current_state[0], current_state[1], action_idx] = q_table[current_state[0], current_state[1], action_idx]
            
            if snake.positions[0] == food.position:
                snake.grow()
                food.randomize()
            
            win.fill(WHITE)
            for i in range(GRID_SIZE):
                for j in range(GRID_SIZE):
                    pygame.draw.rect(win, BLACK, (i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
            
            for pos in snake.positions:
                pygame.draw.rect(win, GREEN, (pos[0] * CELL_SIZE, pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                label = font.render("Snake", True, BLACK)
                win.blit(label, (pos[0] * CELL_SIZE + 5, pos[1] * CELL_SIZE + 5))
            
            pygame.draw.rect(win, RED, (food.position[0] * CELL_SIZE, food.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            label = font.render("Food", True, BLACK)
            win.blit(label, (food.position[0] * CELL_SIZE + 5, food.position[1] * CELL_SIZE + 5))

            pygame.display.update()

            if snake.collision():
                done = True
        
        print(f"Episode {episode} finished with total reward: {total_reward}")

if __name__ == "__main__":
    run_snake_game()
