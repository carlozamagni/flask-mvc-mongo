__author__ = 'cazamagni'


def academic_year():
    def validate(value):
        split_val = value.split('/')
        year_1 = int(split_val[0])
        year_2 = int(split_val[1])

        if year_1 == year_2 - 1:
            return True
        raise Exception('academic year must be in format: 2000/2001')

    return validate


def max_length(length):
    def validate(value):
        if len(value) <= length:
            return True
        raise Exception('%s must be at most %s characters long' % length)

    return validate