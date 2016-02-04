# determine the proper factors of a regression model
ccombinations <- function(ivnum)
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