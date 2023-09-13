

class User:
    
    def __init__(self, u_name, u_data, r_data) -> None:
        self.user_name = u_name
        self.u_data = u_data
        self.r_data = r_data
    
        
    def __str__(self) -> str:
        return f"{self.user_name}\n {self.u_data}\n {self.r_data}"    