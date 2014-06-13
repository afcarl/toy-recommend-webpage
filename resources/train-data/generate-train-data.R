#!/bin/env R

## Cateogry A: (A, B, C) = (6, 3, 1)
## Cateogry B: (A, B, C) = (1, 2, 7)
## Cateogry C: (A, B, C) = (1, 8, 1)

## train data
num.rows <- 10000
train.data.fraction <- 0.2

# generate data randomly
data.A <- data.frame(A=rpois(num.rows, 6), B=rpois(num.rows, 3), C=rpois(num.rows, 1), label="A")
data.B <- data.frame(A=rpois(num.rows, 1), B=rpois(num.rows, 2), C=rpois(num.rows, 7), label="B")
data.C <- data.frame(A=rpois(num.rows, 1), B=rpois(num.rows, 8), C=rpois(num.rows, 1), label="C")

# filter appropriate rows from the generated data
data <- subset( rbind(data.A, data.B, data.C), A + B + C <= 10)
# shuffle data
data <- data[sample(nrow(data)), ]
train.data.rows <- nrow(data) * train.data.fraction
train.data      <- data[1:train.data.rows, ]
test.data       <- data[(train.data.rows+1):nrow(data), ]

# save data
train.data.filename <- "train-data.tsv"
test.data.filename  <- "test-data.tsv"
write.table(x=train.data, file=train.data.filename, col.names=FALSE, row.names=FALSE)
write.table(x=test.data, file=test.data.filename, col.names=FALSE, row.names=FALSE)
