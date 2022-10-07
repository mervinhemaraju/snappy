
from datetime import date

def format_today():
    """
    It returns today's date in the format YYYYMMDD
    :return: The current date in the format of YYYYMMDD
    """
    return date.today().strftime("%Y%m%d")

def remove_duplicate_ids(ids):
    """
    It takes a list of instances and returns a new list of instances with no duplicates
    
    :param instances: list of instances to be checked for duplicates
    :return: A list of instances
    """
    new_list = []
    
    for id in ids:
        
        is_present = any(x['volume_id'] == id['volume_id'] for x in new_list)

        if not is_present:
            new_list.append(id)
    
    return new_list