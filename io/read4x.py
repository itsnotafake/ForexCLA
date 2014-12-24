##
# @brief Read a 4x data file.
#
# @param fileName The name of a .csv file.
# @param darray An empty array.
# @return True or False
#
# @author
#
# Reads a .csv file from the Data folder and allocates
# array elements, one per line. Each element is an
# array with format [xx, xx, xx, xx, xx].
def read_4xfile(fileName, darray):
    print("reading: " + "../Data/" + fileName + ".csv");
    return True