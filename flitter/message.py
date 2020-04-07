class Message:
    def __init__(self, author, text):
        self.author = author
        self.text = text

    def is_by(self, user):
        return self.author == user
        
    
    
    def is_in(self, mentioned):
        split_text = self.text.lower().split(" ")
        if "@" + mentioned.lower() in split_text:
            return True 
        else:
            return False