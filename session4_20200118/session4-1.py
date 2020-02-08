class Movie:
    def __init__(self, title, actor, director, genre):
        self.title = title
        self.actor = actor
        self.director = director
        self.genre = genre

    def book(self):
        print(self.title, '예약되었습니다.')


class ActionMovie(Movie):
    def __init__(self, title, actor, director, genre, blood, nation):
        super().__init__(title, actor, director, genre)
        # super(). 써서 슈퍼클래스 끌고옴. 클래스 밖의 클래스를 끌고오는거라 self 안씀.
        self.blood = blood
        self.nation = nation
    def book(self):
        #무비에서 override 한거.
        super().book()
        #override 아니고 액션무비 클래스에 새로 추가한 기능.
        print(self.title, "은 액션영화입니다.")
    def streeGetaway(self):
        print('스트레스가 해소되었습니다.')


malepicent = Movie("malepicent", "Angelina", "Hakyung", "Fantasy")
malepicent.book()


born = ActionMovie("Born", "Mathew", "Dohan", "Action", "yes", "america")
born.book()
born.streeGetaway()

