#Tests whether the new word differs by only number_of_changes and that the new word is in the dataset
def test(original, new, number_of_changes, dataset):
    if not isinstance(new, str) :
        raise Exception("New word is not a string")
    if dataset is None:
        raise Exception("Dataset is None")
    if number_of_changes < 0:
        raise Exception("Number of changes must be greater than 0")
    if number_of_changes > len(original):
        raise Exception("Number of changes must be less than or equal to the length of the original word")

    if len(original) != len(new):
        print("Lengths do not match")
        return False
    if new not in dataset:
        print("Word not in dataset")
        return False

    changes = calculate_changes(original, new)

    if changes > number_of_changes:
        print("Too many changes")
        return False

    return True

def calculate_changes(original, new):
    changes = 0
    for i in range(len(original)):
        if original[i] != new[i]:
            changes += 1
    return changes


def pretty_print(word_ladder):
    word_list = "\n\t".join(word_ladder)
    return """
=====================
\t{word_list}
=====================
  """.format(word_list=word_list)