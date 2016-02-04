# determine the proper factors of a regression model
count_combs <- function(ivnum)
{
    # count the total number of possible combinations of ivnum ivs.
    # input: number of independent variables
    # output: number of possible combinations
    count <- 0
    for (i in 1:ivnum)
    {
        n <- combn(ivnum, i)
        count <- count + ncol(n)
    }
    return(count)
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