def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)



def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return dna1 > dna2



def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    num_nucleotides = 0

    for char in dna:
        if char == nucleotide:
            num_nucleotides = num_nucleotides + 1

    return num_nucleotides



def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    """

    return dna2 in dna1



def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if the DNA sequence contains only nucleotides.

    >>> is_valid_sequence('CCABTGG')
    False
    >>> is_valid_sequence('CCATGG')
    True
    """

    is_nucleotide = True

    nucleotide = ['A', 'T', 'C', 'G']

    for char in dna:
        if char not in nucleotide:
            is_nucleotide = False

    return is_nucleotide



def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    Return DNA sequence from inserting dna2 into dna1 at the given index.

    >>> insert_sequence('CCGG', 'AT', 2)
    ’CCATGG’
    >>> insert_sequence('CCTTG', 'AA', 5)
    'CCTTGAA'
    """

    result = dna1[ :index] + dna2 + dna1[index: ]
    return result



def get_complement(nucleotide):
    """ (str) -> str

    Gives a complementary nucleotide given a nucleotide.

    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    >>> get_complement('T')
    'A'
    >>> get_complement('G')
    'C'
    >>> get_complement('B')
    """

    if nucleotide == 'A':
        return 'T'
    if nucleotide == 'C':
        return 'G'
    if nucleotide == 'T':
        return 'A'
    if nucleotide == 'G':
        return 'C'



def get_complementary_sequence(dna):
    """ (str) -> str

    Gives a complementary dna sequence given a dna sequence.

    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('CTG')
    'GAC'
    """

    complement_string = ''

    for char in dna:
        complement_string = complement_string + get_complement(char)

    return complement_string
        

        

    
    



    

    
            
                
    

    
