from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title


class UrTube:

    def __init__(self):
        self.videos = []
        self.users = []
        self.current_user = None

    def log_in(self, nickname, password):
        for u in self.users:
            if nickname in u.nickname and password in u.password:
                self.current_user = u.nickname
                return u.nickname

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user not in self.users:
            self.users.append(new_user)
            self.current_user = new_user
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for a in args:
            if a not in self.videos:
                self.videos.append(a)

    def get_videos(self, poisk):
        lp = []
        for v in self.videos:
            if str(poisk).lower() in str(v).lower():
                lp.append(v.title)
        return lp

    def watch_video(self, vid_name):
        if self.current_user is None:
            print('Войти в аккаунт чтобы смотреть видео')
            return
        for v in self.videos:
            if vid_name == v.title:
                if v.adult_mode and self.current_user.age >= 18:
                    while v.time_now < v.duration:
                        v.time_now += 1
                        print(v.time_now, end=' ')
                        sleep(1)
                    v.time_now = 0
                    print('Конец видео')
                else:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                break


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
