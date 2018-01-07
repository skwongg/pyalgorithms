"""
"Provide a function that returns if two files are exactly the same content-wise.
It should work for any file type. Only opening, reading and retrieving basic
file properties of the file (e.g. size) is allowed."
(Compare if 2 files are the same.)

We are looking for:
1. that it presents good software practices: documentation, testing, good
variable names, etc
2. is error-free
(If they copy and paste it, it won't have those things)

The snippet should be good enough quality to drop in a real system (so good software engineering practices, not too much memory consumption, etc.)
Don't hesitate to ask any questions. """

import os


def samesize(first_file, second_file):
    return (os.path.getsize(first_file) == os.path.getsize(second_file))

#naive solution
def compare_files_naive(first_file, second_file):
    if not samesize(first_file, second_file):
        return False
    with open(first_file) as first:
        with open(second_file) as second:
            return first.read() == second.read()


#chunked solution
def compare_file_chunks(first_file, second_file, chunksize):
    if not samesize(first_file, second_file):
        return False
    with open(first_file) as first:
        with open(second_file) as second:
            while True:
                chunkfirst = first.read(chunksize)
                chunksecond = second.read(chunksize)
                if not chunkfirst:
                    break
                elif chunkfirst == chunksecond:
                    continue
                else:
                    return False
            return True


#Raises AssertionError if below statements aren't true.
assert samesize('file1','file2') == True
assert samesize('file1','file3') == False
assert compare_files_naive('file1','file2') == True
assert compare_files_naive('file1','file3') == False
assert compare_file_chunks('file1','file2', 10) == True
assert compare_file_chunks('file1','file3', 10) == False


'''
Using only open, read and os methods these would be my pythonic
solutions. The chunked version is preferable for most cases simply
because it does not abuse memory. In a real practical solution,
I would use a hashing library to produce a Checksum that can be
checked agaisnt.

IE: if the checksum value was 'abc123xyz456', the
file compared against will return 'abc123xyz456' if indeed the same,
then every successive check can be compared to it in this way. Saving
memory because the hashed value is the only thing that needs to be
stored from the first file.
'''
