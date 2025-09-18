from model import IsoCategory

# example marker sequences and isomer categories

yea_sequences = IsoCategory(
    name='yea',
    base_forms=[['AA', 'CC', 'TT']],
    permuted_allowed=False,
    result_marker='AAAAAA' + 'AAAAAA' + 'TTTTTT' + 'TTTTTT' + 'GGGGGG'
)

nay_sequences = IsoCategory(
    name='nay',
    base_forms=[['AA', 'CC', 'GG'], ['AA', 'TT', 'GG'], ['CC', 'TT', 'GG']],
    permuted_allowed=False,
    result_marker='GGGGGG' + 'GGGGGG' + 'CCCCCC' + 'CCCCCC' + 'TTTTTT'
)

# sequences used for Q,B,E
Q = 'AAAAAA' + 'CCCCCC' + 'TTTTTT' + 'GGGGGG'
B = 'CCCCCC' + 'TTTTTT' + 'CCCCCC'
E = 'GGGGGG' + 'TTTTTT' + 'GGGGGG'
