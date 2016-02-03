# determine the proper factors of a regression model
combinations <- function(ivnum)
{
    
    count <- 0
    for (i in 1:ivnum)
    {
        n <- combn(ivnum, i)
        count <- count + ncol(n)
    }
    return(count)
}