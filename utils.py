import pickle

def load_model():
    with open('internship_success_model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


def select_skills(role):
    """
    Selects a list of skills based on the role specified.

    Args:
    role (str): The role for which skills need to be determined.

    Returns:
    list: A list of skills based on the specified role.
    """
    if role == "Backend":
        return ["Python", "Java", "SQL"]
    elif role == "Machine Learning":
        return ["Python", "SQL", "Machine Learning"]
    else:
        return ["HTML", "CSS", "JavaScript"]
    
def count_similar_elements(list1, list2):
    """
    Counts the number of similar elements between two lists.

    Args:
    list1 (list): The first list.
    list2 (list): The second list.

    Returns:
    int: The count of elements that are present in both lists.
    """
    count = 0  # Initialize the count of similar elements to 0
    for element in list1:  # Iterate through each element in the first list
        if element in list2:  # Check if the element is present in the second list
            count += 1  # Increment the count if the element is found in both lists
    return count  # Return the total count of similar elements

def encode_programming_level(x):
    """
    Encodes the programming level category into numerical representation.

    Args:
    x (str): The programming level category to be encoded.

    Returns:
    int: Encoded numerical representation (1 for 'Beginner', 2 for others).
    """
    if x == "Beginner":
        return 1
    else:
        return 2


def encode_education(x):
    """
    Encodes the education category into numerical representation.

    Args:
    x (str): The education category to be encoded.

    Returns:
    int: Encoded numerical representation (1 for 'student', 2 for others).
    """
    if x == "student":
        return 1
    else:
        return 2