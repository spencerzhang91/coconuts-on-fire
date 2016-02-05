# determine the proper factors of a regression model
# It seems that what I'm trying to do here was already done: step()
# preparations
library(car)
file <- file.choose()
data <- read.csv(file)

# functions defined below:
corr_check <- function(table, ivs, dv)
{
    # This function filter out ivs that not sig corr to dv
    # table: data source csv file
    # ivs: independent variable column numbers (in range)
    # dv: dependent variable column number
    # No return value(s)
    rest_ivs <- NULL
    for (i in ivs)
    {
        relativity <- cor.test(data[, i], data[, dv])
        p_val <- relativity$p.val
        if (p_val < 0.005)
            rest_ivs <- c(rest_ivs, i)
        print(relativity)
    }
    return(rest_ivs)
}

count_combs <- function(ivs)
{
    # count the total number of possible combinations of ivnum ivs
    # ivs: an array that contains the valid combination of ivs
    # return: number of possible combinations
    count <- 0
    for (i in ivs)
    {
        n <- combn(ivs, i)
        count <- count + ncol(n)
    }
    return(count)
}

kappa_combs <- function(table, ivs, dv)
{
    # return the valid iv combinations
    # table: source data table
    # ivs: independent variable column number range
    # dv: dependent variable column number
    # return: calculate the kappa of ivs combinations
    # yet done   
}

vif_combs <- function(table, ivs, dv)
{
    # return the valid iv combinations
    # table: source data table
    # ivs: independent variable column number range
    # dv: dependent variable column number
    # return: calculate the vif of ivs combinations
    # yet done
}