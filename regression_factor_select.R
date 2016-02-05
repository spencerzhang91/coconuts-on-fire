# determine the proper factors of a regression model
# It seems that what I'm trying to do here was already done: step()
# preparations
library(car)
file <- file.choose()
data <- read.csv(file)

count_combs <- function(ivnum)
{
    # count the total number of possible combinations of ivnum ivs.
    # ivnum: number of independent variables
    # return: number of possible combinations
    count <- 0
    for (i in 1:ivnum)
    {
        n <- combn(ivnum, i)
        count <- count + ncol(n)
    }
    return(count)
}

cor_combs <- function(table, ivs, dv)
{
    # table: source data table
    # ivs: independent variable column number range
    # dv: dependent variable column number
    # return: ivs that significantly correlated to dv
    # yet done
}

vif_combs <- function(table, ivs, dv)
{
    # table: source data table
    # ivs: independent variable column number range
    # dv: dependent variable column number
    # return: calculate the vif of ivs combinations
    # yet done
}

kappa_combs <- function(table, ivs, dv)
{
    # table: source data table
    # ivs: independent variable column number range
    # dv: dependent variable column number
    # return: calculate the kappa of ivs combinations
    # yet done   
}