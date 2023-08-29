class Drag:
    def __init__(self) -> None:
        self.initial_x = None
        self.initial_y = None
        self.final_x = None
        self.final_y = None
        self.has_piece = None
        self.is_dragging = False

    def set_init_pos(self, x, y):
        self.initial_x = x
        self.initial_y = y

    def update_final_pos(self, x, y):
        self.final_x = x
        self.final_y = y

    def clear_drag(self):
        self.initial_x = None
        self.initial_y = None
        self.final_x = None
        self.final_y = None
        self.has_piece = None
        self.is_dragging = False

    def get_final_pos(self):
        return (self.final_x, self.final_y)

    def get_init_pos(self):
        return (self.initial_x, self.initial_y)
