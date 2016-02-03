# This script is aimed at automaticly do a series of regression related analysises.
# For using library car, the newest version of R is needed.
# Still require some basic knowledge of R programming in order to reuse.
# Feb 2nd: a new function is brought to schedule

# preparations
library(car)
file <- file.choose()
data <- read.csv(file)

# functions defined below:
batch_corr <- function(table, ivcs, dvc)
{
    # This function calculates the correlence between a group of iv and one dv
    # table: data source csv file
    # ivcs: independent variable column numbers
    # dvc: dependent variable column number
    # No return value(s)
    for (i in ivcs)
    {
        relativity <- cor.test(data[, i], data[, dvc])
        print(c(colnames(table)[i], colnames(table)[dvc])) 
        print(relativity)
    }
}

batch_linear <- function(table, ivcs, dvc)
{
    # simple linear regression
    # table: data source csv file
    # ivcs: independent variable column numbers
    # dvc: dependent variable column number
    # No return value(s)
    for (i in ivcs)
    {
        fit <- lm(table[, dvc] ~ table[, i])
        print(c(colnames(table)[i], colnames(table)[dvc]))
        print(summary(fit))
    }
}

multicollinearity <- function(table, vg1, vg2, vg3)
{
    # This function solves the multicollinearity problem
    # table: data sourse csv file
    # vg1: independent variable group1 (population & constructed area)
    # vg2: independent variable group2 (3 compactness measurement indeces)
    # vg3: independent variable group3 (administrative indeces)
    multicol_all <- kappa(cor(data.frame(vg1, vg2, vg3)))
    multicol_vg1 <- kappa(cor(vg1))
    multicol_vg2 <- kappa(cor(vg2))
    multicol_vg3 <- kappa(cor(vg3))
    
    for (item in c(multicol_all, multicol_vg1, multicol_vg2, multicol_vg3))
      print(item)
}

selected_multi_linear_inter <- function(table, selected, dvc)
{
    # table: data source csv file
    # selected: selected independent varialbes number
    # dvc: dependent variable column number
    # No return value(s)
    m_model <- lm(table[, dvc] ~ Scale_pop +
                                 Admin_hierarchy +
                                 Compact_da,
                                 data=table)
    print(summary(m_model))
    print(vif(m_model))
    print(sqrt(vif(m_model)) > 2) # check if there is any multicollinearity problem
}

selected_multi_linear_no <- function(table, selected, dvc)
{
    # table: data source csv file
    # selected: selected independent varialbes number
    # dvc: dependent variable column number
    # No return value(s)
    m_model <- lm(table[, dvc] ~ 0 + Scale_pop +
                                 Admin_hierarchy +
                                 Compact_da,
                                 data=table)
    # it used to omit the intercept on line 78 but warning messages appeared as follows:
    # 'No intercept: vifs may not be sensible.' when doing VIF test
    print(summary(m_model))
    print(vif(m_model))
    print(sqrt(vif(m_model)) > 2) # if there is any problem?
}

correlence_ivs <- function(table, ivcs, dvc)
{
    # table: data source csv file
    # ivcs: independent variable column numbers
    # dvc: dependent variable column number
    # No return value(s)
    plot_data <- table[, c(dvc,ivcs)]
    scatterplotMatrix(plot_data, spread=FALSE, lty.smooth=2,
                      main="correlence matrix")
}

opt_factors <- function(table, ivcs, dvc)
{
    # A function that decides what is the best IVs of a regression model
    # table: data source csv file
    # ivcs: independent variable column numbers
    # dvc: dependent variable column number
    # return the relatively best factors of a regression model (in column numbers)
    # to be done within Feb 3rd
}

# Some concerned variables:
selectedFactors <- data[,c(1, 3, 5)]
selected_num <- c(1, 3, 5)
dependent <- data[, 7]

vargroup_1 <- data[, 1:2]
vargroup_2 <- data[, 3:4]
vargroup_3 <- data[, 5:7]

# result printing area, to reuse edit the arguments of function according to need
print("data source:")
print(file)
print("=======correlence=======")
batch_corr(data, 1:7, 8)

print("=======Linear=======")
batch_linear(data, 1:7, 8)

print("=======multicollinearity=======")
# multicollinearity(data, vargroup_1, vargroup_2, vargroup_3)

print("=======selectedFactors=======")
print(kappa(cor(selectedFactors), exact=T))

print("=======multi-factor linear regression model=======")
selected_multi_linear_inter(data, selected_num, 8)
selected_multi_linear_no(data, selected_num, 8)

print("All process successfully done.")