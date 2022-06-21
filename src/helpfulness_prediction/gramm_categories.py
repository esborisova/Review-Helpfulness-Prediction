"""Function for counting the number of POSs in a string."""

from typing import List


def count_pos(text: str, nlp, pos_tags: List[str]) -> int:
    """
    Counts the number of specified grammatical categories in a string.

    Args:
        text (str): A srting with a text.
        nlp: A spaCy pipeline.
        pos_tags (List[str]): A list with POS tags.

    Returns:
        int: The number of POSs in a string.
    """
    doc = nlp(text)
    pos = [token.tag_ for token in doc if token.tag_ in pos_tags]
    pos_num = len(pos)
    return pos_num
