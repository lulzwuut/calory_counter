class MealTooBigError(Exception):
    """
    Raises an error if the input order contains more  than 2000 calories.
    """
    def __init__(self, calories):
        self.calories = calories
        self.message = 'Your meal contains ' + str(calories) + ' calories. That\'s more than 2000!'
        super().__init__(self.message)
