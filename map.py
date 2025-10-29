import os
import check_input

class Map:
    
    _instance = None
    _initialized = False
    
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if Map._initialized:
            return
        
        
        map_layout = []
            
        with open('map.txt', 'r') as file:
            for line in file:
                items = list(line.strip('\n'))
                map_layout.append(items)
                
        
        self.map = map_layout
        self.revealed = [[False for _ in row] for row in self.map]
        Map._initialized = True
        
            
    def __getitem__(self, row):
        return self.map[row]
    
    def __len__(self):
        return len(self.map)
    
    def show_map(self, loc):
    
        try:
            r, c = loc
            if not (isinstance(r, int) and isinstance(c, int)):
                raise Exception()
            if not (0 <= r < len(self.map) and 0 <= c < len(self.map[0])):
                raise Exception()
        except Exception:
            row_prompt = f"Enter row (0-{len(self.map)-1}): "
            col_prompt = f"Enter column (0-{len(self.map[0])-1}): "
            r = check_input.get_int_range(row_prompt, 0, len(self.map) - 1)
            c = check_input.get_int_range(col_prompt, 0, len(self.map[0]) - 1)

        rows = []
        for ri in range(len(self.map)):
            line_chars = []
            for ci in range(len(self.map[0])):
                if ri == r and ci == c:
                    line_chars.append("*")
                elif self.revealed[ri][ci]:
                    line_chars.append(self.map[ri][ci])
                else:
                    line_chars.append("x")
            rows.append("".join(line_chars))
        return "\n".join(rows)

    def reveal(self, loc):
        # Validate loc; if invalid interactively prompt via check_input.get_int_range
        try:
            r, c = loc
            if not (isinstance(r, int) and isinstance(c, int)):
                raise Exception()
            if not (0 <= r < len(self.map) and 0 <= c < len(self.map[0])):
                raise Exception()
        except Exception:
            row_prompt = f"Enter row (0-{len(self.map)-1}): "
            col_prompt = f"Enter column (0-{len(self.map[0])-1}): "
            r = check_input.get_int_range(row_prompt, 0, len(self.map) - 1)
            c = check_input.get_int_range(col_prompt, 0, len(self.map[0]) - 1)

        self.revealed[r][c] = True

    def remove_at_loc(self, loc):
        # Validate loc; if invalid interactively prompt via check_input.get_int_range
        try:
            r, c = loc
            if not (isinstance(r, int) and isinstance(c, int)):
                raise Exception()
            if not (0 <= r < len(self.map) and 0 <= c < len(self.map[0])):
                raise Exception()
        except Exception:
            row_prompt = f"Enter row (0-{len(self.map)-1}): "
            col_prompt = f"Enter column (0-{len(self.map[0])-1}): "
            r = check_input.get_int_range(row_prompt, 0, len(self.map) - 1)
            c = check_input.get_int_range(col_prompt, 0, len(self.map[0]) - 1)

        self.map[r][c] = "n"
