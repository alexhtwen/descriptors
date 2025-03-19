'''Alex Van 溫華添 世凡'''
class Me:    # Pythonista
    email = 'alexhtwen@gmail.com'
    github = 'https://github.com/vtvan'
    phone = '+886 918-800878'
    @staticmethod      # 妙玉
    def greet(hi: str) -> None:
        print(f'{hi} from {__doc__}')

Me.greet('"Χαίρετε, Κόσμε! 安世"')