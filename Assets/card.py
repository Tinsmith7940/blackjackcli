class Card:
    def __init__(self, suit,face, score=0, faceup=False):
        self.suit = suit
        self.face = face
        self.score = score
        self.faceup = faceup

    def get_suit(self):
        return self.suit
        
    def get_face_value(self):
        return self.face

    def get_score(self):
        return self.score 

    def get_orientation(self):
        return self.faceup 
    
    def set_orientation(self, faceup = False):
        self.faceup = faceup
