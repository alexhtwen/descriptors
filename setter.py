class Tree:
    '''Property Decorator範例'''
    def __init__(self, breed: str, age: int):   # constructor
        self.__breed = breed     # private attribute
        self.__age = age         # private attribute

    @property
    def breed(self) -> str:
        '''The breed property(getter).'''
        return self.__breed

    @breed.setter
    def breed(self, breed: str):
        '''The breed property(setter).'''
        if not isinstance(breed, str):
            raise TypeError('樹種必須是字串。')

        breeds = {'cedar': (0, 5_000), 'oak': (0, 300),
                    'beech': (0, 400), 'camphor': (0, 800),
                    'maple': (0, 500), 'phoebe': (0, 2_000)}

        breed = breed.strip().lower()
        if breed not in breeds:
            raise Exception(f"樹種名稱'{breed}'不正確。")
        self.__breed = breed

    @breed.deleter
    def breed(self):
        '''The breed property(deleter).'''
        if self.__age > 1_000:
            raise Exception('千年古樹禁止砍伐。')
        del self.__breed

    @property
    def age(self) -> int:
        '''The age property(getter).'''
        return self.__age

    @age.setter
    def age(self, age: int):
        '''The age property(setter).'''
        if not isinstance(age, int):
            raise TypeError('樹齡必須是整數。')
        # 以下的條件判斷只是「示意」，實際上該和breed一併考慮才對。
        if age > 15_000 or age < 0:
            raise Exception(f'樹齡數字{age}不合理。')
        self.__age = age

    @age.deleter
    def age(self):
        '''The age property(deleter).'''
        del self.__age