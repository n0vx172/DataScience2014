import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    identifier=record[0]
    sequence = record[1]
    sequence = sequence[:(len(sequence)-10)]
    key='trimmed nucleotide'
    mr.emit_intermediate(key,sequence)

def reducer(key, list_of_values):
    v=set(list_of_values)  
    for x in v:
        mr.emit(x)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
