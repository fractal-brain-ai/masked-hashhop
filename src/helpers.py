from random import choices


class DnaTokenizer:
    """
    This is a trivial tokenizer for use in genomics-related problems,
    reproducing the following code:

    ```
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained("LongSafari/hyenadna-large-1m-seqlen-hf", trust_remote_code=True)
    ctxt_lines = 'ACTG' # -> [7,8,10,9]
    x = tokenizer(ctxt_lines, return_tensors='pt', add_special_tokens=False)['input_ids'] # Tensor [7,8,10,9]
    ```
    """

    def __init__(self):
        # 'ACTG'  -> [7,8,10,9]
        self.enc = {'A': 7, 'C': 8, 'T': 9, 'G': 10, }
        self.dec = {7: 'A', 8: 'C', 9: 'T', 10: 'G', }

    def encode(self, tokens: list[str]) -> list[int]:
        return [self.enc[t] for t in tokens]

    def decode(self, tokens: list[int]) -> list[str]:
        return [self.dec[t] for t in tokens]

    def str_encode(self, tokens: list[str]) -> list[str]:
        """
        Version of .encode but returning list[str]
        :param tokens:
        :return: string versions of int tokens; e.g. str_encode(['A','C']) = ['7','8']
        """
        return [str(self.enc[t]) for t in tokens]

    def str_decode(self, tokens: list[str]) -> str:
        """
        Converts into 'ACTG' string from tokens of the form: ['7', '8', '9', '10']
        Assumes tokens are int-convertable. Joins all the tokens into a single string.
        :param tokens:
        :return:
        """
        return ''.join(self.decode([int(s) for s in tokens]))


# helpers

def generate_random_intervals(n_numbers: int, total: int) -> tuple[int, ...]:
    """
    Generates `n_numbers` int's which in total are equal to `total`.

    Note:
    - numbers are roughly statistically equivalent

    :param total: required sum of all the numbers
    :param n_numbers: how many numbers to generate
    :return: generated numbers, not sorted in any way
    """
    z = range(0, total + 1)
    sel = [0] + sorted(choices(z, k=n_numbers - 1))
    sel.append(total)
    res = []
    for en in range(1, len(sel)):
        res.append(sel[en] - sel[en - 1])
    return tuple(res)


def fit_elems_into_context(context: list[str], elems: list[list[str]]) -> list[str]:
    """
    Sequences from `elems` will be imprinted onto `context` in order in which they appear in `elems`
    and in a non-overlapping way. The last sequence is always the suffix of the resulting context (make it empty if this
    behavior is not desired).

    Note:
    - this is "imprint" meaning tokens taken from `context` remain where they were in `context`

    :param context:
    :param elems:
    :return: imprinted context of the same length as `context`
    """
    total_len = sum(len(k) for k in elems)
    space = len(context) - total_len
    if space < 0:
        raise ValueError('Total length of elems to be imprinted is greater than context length!')

    # strategy: select random lengths of "spaces" between `elems`, where tokens will be copied from the context
    spaces = generate_random_intervals(n_numbers=len(elems), total=space)

    # fitting: space0,elem0,space1,elem1,...,spaceN,elemN
    res = []
    for i in range(len(elems)):
        at = len(res)
        res.extend(context[at:at + spaces[i]])
        res.extend(elems[i])
    return res
