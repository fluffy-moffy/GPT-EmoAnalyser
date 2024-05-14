import sys
import asyncio
import pygame
import pygame_textinput

from dynamic_circle_visualizer import DynamicCircle
from chatgpt_client import ChatGptClient
from emotion_accumulator import EmotionAccumulator


# Constants for screen
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize pygame and create the screen
def init_screen():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Emotion Viewer")
    return screen

# Main asynchronous function to run the event loop and rendering
async def main():
    screen = init_screen()
    clock = pygame.time.Clock()
    input_box = pygame.Rect(50, 550, 500, 40)
    textinput = pygame_textinput.TextInputVisualizer()
    response_data = {"positive": 50.0, "negative": 50.0}
    text_output = ""
    start_time = pygame.time.get_ticks()

    pygame.key.set_repeat(500, 30)
    chat_client = ChatGptClient()
    emotion_accumulator = EmotionAccumulator()

    # Create an instance of the DynamicCircle class
    dynamic_circle = DynamicCircle(screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 150)

    response_future = None
    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and not response_future:
                user_input = textinput.value
                if user_input:
                    response_future = asyncio.ensure_future(chat_client.chat_client(user_input))
                    textinput.value = ''

        if response_future and response_future.done():
            response = response_future.result()
            response_data = emotion_accumulator.analyze_emotion(response)
            print(response_data)
            text_output = response
            start_time = pygame.time.get_ticks()
            response_future = None

        textinput.update(events)
        screen.fill(WHITE)
        # Draw the dynamic circle with the current emotional data
        dynamic_circle.draw(response_data, start_time)
        screen.blit(textinput.surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, BLACK, input_box, 2)
        font = pygame.font.Font(None, 24)
        response_surface = font.render(text_output, True, BLACK)
        screen.blit(response_surface, (50, 500))
        pygame.display.flip()
        clock.tick(60)

        await asyncio.sleep(0)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    asyncio.run(main())
