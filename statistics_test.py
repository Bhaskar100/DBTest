from statistics import *
import statistics
print(dir(statistics))


# initializing list
li = [1, 2, 3, 3, 2, 2, 2, 1]

#  ------------------------------------ Mean -----------------------------------------------------
# using mean() to calculate average of list
# elements
print("The average of list values is : ", end="")
print(statistics.mean(li))


# ------------ Median -----------------------------------------------------------------------------
# tuple of positive integer numbers
data1 = (2, 3, 4, 5, 7, 9, 11)

# tuple of floating point values
data2 = (2.4, 5.1, 6.7, 8.9)

# tuple of a set of negative integers
data4 = (-5, -1, -12, -19, -3)

# tuple of set of positive
# and negative integers
data5 = (-1, -2, -3, -4, 4, 3, 2, 1)

print("Median of data-set 1 is % s" % (median(data1)))
print("Median of data-set 2 is % s" % (median(data2)))
print("Median of data-set 4 is % s" % (median(data4)))
print("Median of data-set 5 is % s" % (median(data5)))

# --------------------------- Mode ---------------------------------------

data1_mode = (2, 3, 3, 4, 5, 5, 5, 5, 6, 6, 6, 7)
print("Mode of data set 1 is % s" % (mode(data1_mode)))


# ----------------------------- Range ----------------------------------------


# Sample Data
arr = [1, 2, 3, 4, 5]

# Finding Max
Maximum = max(arr)
# Finding Min
Minimum = min(arr)

# Difference Of Max and Min
Range = Maximum - Minimum
print("Maximum = {}, Minimum = {} and Range = {}".format(
    Maximum, Minimum, Range))


# ------------------ Variance -------------------------------------

# tuple of a set of positive integers
# numbers are spread apart but not very much
sample1 = (1, 2, 5, 4, 8, 9, 12)

# tuple of a set of negative integers
sample2 = (-2, -4, -3, -1, -5, -6)


print("Variance of Sample1 is % s " % (variance(sample1)))
print("Variance of Sample2 is % s " % (variance(sample2)))


# ------------------ Standard Deviation -------------------------------

# numbers are spread apart but not very much
sample1 = (1, 2, 5, 4, 8, 9, 12)

# tuple of a set of negative integers
sample2 = (-2, -4, -3, -1, -5, -6)

print("The Standard Deviation of Sample1 is % s"
      % (stdev(sample1)))

print("The Standard Deviation of Sample2 is % s"
      % (stdev(sample2)))


