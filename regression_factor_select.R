# determine the proper factors of a regression model
# It seems that what I'm trying to do here was already done: step()
# preparations
library(car)
file <- file.choose()
data <- read.csv(file)

# functions defined below:
corr_check <- function(table, ivs, dv)
{
    # This function filter out ivs that not sig corr to dv.
    # table: data source csv file
    # ivs: independent variable column numbers (in range)
    # dv: dependent variable column number
    # return the valid ivs (column numbers of table)
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

count_combs <- function(rest_ivs)
{
    # count the total number of possible COMBINATIONS of ivs.
    # rest_ivs: valid ivs that selected by function corr_check
    # return: a list that contains iv COMBINATIONS
    count <- 0
    combs <- list()
    for (i in 1:length(rest_ivs))
    {
        n <- combn(rest_ivs, i)
        count <- count + ncol(n)
        combs <- c(combs, list(n))
    }
    cat("There are totally", count, "valid combinations.")
    return(combs)
}

kappa_combs_2 <- function(table, combs)
{
    # return the valid iv COMBINATIONS
    # table: source data table
    # combs: independent variable combination list
    # return: calculate the kappa of ivs COMBINATIONS
    # Main functionality done!
    cnt <- 0
    res_combs <- list()
    for (matrix in combs)
        for (col in 1: ncol(matrix))
        {
            # print(colnames(data)[matrix[, col]])
            comb_data <- table[, matrix[, col]]
            if (class(comb_data) != "numeric")
            {
                kappa_val <- kappa(cor(comb_data))
                if (kappa_val < 10)
                {
                    res_combs <- c(res_combs, list(comb_data))
                    cnt <- cnt + 1
                    print(c(colnames(data)[matrix[, col]], kappa_val))
                }
            }
        }
    print(c("Total vilid combination number:", cnt))
    return(res_combs)
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

linear_model_check <- function(table, selected, dvc)
{
    # yet done
    m_model <- lm(table[, dvc] ~ Scale_pop +
                                 Admin_hierarchy +
                                 Compact_da,
                                 data=table)
    print(summary(m_model))
    print(vif(m_model))
    print(sqrt(vif(m_model)) > 2)
}

#-------------------# Test area #-------------------#

c1 <- corr_check(data, 1:7, 8) # set column range to proper then run
c2 <- count_combs(c1)
c3 <- kappa_combs_2(data, c2)