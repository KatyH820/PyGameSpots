# spots_game.py - view for the Spots game
import pygame
import spots


class SpotsGame:
    def __init__(self) -> None:
        self._running = True
        self._state = spots.SpotsState()

    def run(self) -> None:
        pygame.init()
        try:
            self._resize_display((600, 600))
            clock = pygame.time.Clock()
            while self._running:
                clock.tick(30)
                self._update_world()
                self._redraw()
        finally:
            pygame.quit()

    def _resize_display(self, size: (int, int)) -> None:
        # include pygame.RESIZABLE made the window resizeable
        pygame.display.set_mode(size, pygame.RESIZABLE)

    def _update_world(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._end_game()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self._on_mouse_button(event.pos)

        self._state.move_all_spots()

    def _redraw(self) -> None:
        surface = pygame.display.get_surface()
        surface.fill(pygame.Color(128, 128, 128))
        self._draw_spots()
        pygame.display.flip()

    def _draw_spots(self) -> None:
        for spot in self._state.all_spots():
            self._draw_spot(spot)

    def _draw_spot(self, spot: spots.Spot) -> None:
        frac_x, frac_y = spot.center()
        topleft_frac_x = frac_x - spot.radius()
        topleft_frac_y = frac_y - spot.radius()
        frac_width = spot.radius()*2
        frac_height = spot.radius() * 2
        surface = pygame.display.get_surface()
        surface_width = surface.get_width()
        surface_height = surface.get_height()
        topleft_pixel_x = topleft_frac_x * surface_width
        topleft_pixel_y = topleft_frac_y * surface_height
        pixel_width = frac_width * surface_width
        pixel_height = frac_height * surface_height
        pygame.draw.ellipse(surface, pygame.Color(255, 255, 0), pygame.Rect(
            topleft_pixel_x, topleft_pixel_y, pixel_width, pixel_height))

    def _end_game(self) -> None:
        self._running = False

    def _on_mouse_button(self, pos: (int, int)) -> None:
        surface = pygame.display.get_surface()
        surface_width = surface.get_width()
        surface_height = surface.get_height()
        pixel_x, pixel_y = pos
        frac_x = pixel_x / surface_width
        frac_y = pixel_y / surface_height
        self._state.handle_action((frac_x, frac_y))


if __name__ == '__main__':
    SpotsGame().run()
