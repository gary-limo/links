import random
from datetime import time
import string 
from datetime import datetime, timedelta
import decimal

def DA(value_type='default'):
    if value_type == 'min':
        t = time(0, 0, 0)
    elif value_type == 'max':
        t = time(23, 59, 59, 999999)
    elif value_type == 'random':
        t = time(random.randint(0, 23), random.randint(0, 59), random.randint(0, 59), random.randint(0, 999999))
    else:
        return value_type

    return t.strftime('%H:%M:%S.%f')

def CF(length, value_type='default'):
    if value_type == 'min':
        return random.choice(string.ascii_uppercase)
    elif value_type == 'max':
        return ''.join(random.choices(string.ascii_uppercase, k=length))
    elif value_type == 'random':
        return ''.join(random.choices(string.ascii_uppercase, k=random.randint(1, length)))
    else:
       
        if len(value_type) > length:
            raise ValueError("Default value exceeds the specified length")
        return value_type
    
def CV(max_length, value_type='default'):
    if value_type == 'min':
        return ''
    elif value_type == 'max':
        return ''.join(random.choices(string.ascii_uppercase, k=max_length))
    elif value_type == 'random':
        random_length = random.randint(0, max_length)
        return ''.join(random.choices(string.ascii_uppercase, k=random_length))
    else:
        
        if len(value_type) > max_length:
            raise ValueError("Default value exceeds the maximum length")
        return value_type   

def DA(value_type='default'):
    min_date = datetime(1, 1, 1)
    max_date = datetime(9999, 12, 31)

    if value_type == 'min':
        return min_date.strftime('%Y-%m-%d')
    elif value_type == 'max':
        return max_date.strftime('%Y-%m-%d')
    elif value_type == 'random':
        random_days = random.randint(0, (max_date - min_date).days)
        random_date = min_date + timedelta(days=random_days)
        return random_date.strftime('%Y-%m-%d')
    else:
        
        try:
            default_date = datetime.strptime(value_type, '%Y-%m-%d')
            return default_date.strftime('%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid default date value")   

def TS(value_type='default'):
    min_date = datetime(1, 1, 1, 0, 0, 0, 0)
    max_date = datetime(9999, 12, 31, 23, 59, 59, 999999)

    if value_type == 'min':
        result_date = min_date
    elif value_type == 'max':
        result_date = max_date
    elif value_type == 'random':
        random_microseconds = random.randint(0, int((max_date - min_date).total_seconds() * 1_000_000))
        result_date = min_date + timedelta(microseconds=random_microseconds)
    else:
        
        try:
            result_date = datetime.strptime(value_type, '%Y-%m-%d+%H:%M:%S.%f')
        except ValueError:
            raise ValueError("Invalid default datetime value")

    return result_date.strftime('%Y-%m-%d %H:%M:%S.%f')          



def D(precision, scale, value_type='default'):
    if precision < scale:
        raise ValueError("Precision must be greater or equal to scale")

    max_val = decimal.Decimal('9' * (precision - scale) + '.' + '9' * scale)
    min_val = -max_val

    if value_type == 'min':
        return min_val
    elif value_type == 'max':
        return max_val
    elif value_type == 'random':
        random_number = random.randint(int(min_val * (10 ** scale)), int(max_val * (10 ** scale)))
        return decimal.Decimal(random_number) / (10 ** scale)
    else:
        default_val = decimal.Decimal(value_type)
        if not (min_val <= default_val <= max_val):
            raise ValueError(f"Default value must be within the range {min_val} to {max_val}")
        return default_val
    
def I1(value_type='default'):
    min_val, max_val = -128, 127

    if value_type == 'min':
        return min_val
    elif value_type == 'max':
        return max_val
    elif value_type == 'random':
        return random.randint(min_val, max_val)
    else:
        default_val = int(value_type)
        if default_val < min_val or default_val > max_val:
            raise ValueError("Default value must be between -128 and 127")
        return default_val

def I2(value_type='default'):
    min_val, max_val = -32768, 32767

    if value_type == 'min':
        return min_val
    elif value_type == 'max':
        return max_val
    elif value_type == 'random':
        return random.randint(min_val, max_val)
    else:
        default_val = int(value_type)
        if default_val < min_val or default_val > max_val:
            raise ValueError("Default value must be between -32768 and 32767")
        return default_val

def I(value_type='default'):
    min_val, max_val = -2147483648, 2147483647

    if value_type == 'min':
        return min_val
    elif value_type == 'max':
        return max_val
    elif value_type == 'random':
        return random.randint(min_val, max_val)
    else:
        default_val = int(value_type)
        if default_val < min_val or default_val > max_val:
            raise ValueError("Default value must be between -2147483648 and 2147483647")
        return default_val
    

def I8(value_type='default'):
    min_val, max_val = -9223372036854775808, 9223372036854775807

    if value_type == 'min':
        return min_val
    elif value_type == 'max':
        return max_val
    elif value_type == 'random':
        return random.randint(min_val, max_val)
    else:
        default_val = int(value_type)
        if default_val < min_val or default_val > max_val:
            raise ValueError("Default value must be between -9223372036854775808 and 9223372036854775807")
        return default_val

    


