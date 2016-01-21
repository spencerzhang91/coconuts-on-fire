# This project is for the freaking essay.
# There are three functions defined here: batch_corr, batch_kappa and draw.
library(car)
data <- read.csv("J:\\用地建设规模论文\\dataset.csv") # directory set to yours
print(data)

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
        fit <- lm(table[, i] ~ table[, dvc])
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
    multicol_all <- kappa(data.frame(vg1, vg2, vg3))
    multicol_vg1 <- kappa(vg1)
    multicol_vg2 <- kappa(vg2)
    multicol_vg3 <- kappa(vg3)
    
    for (item in c(multicol_all, multicol_vg1, multicol_vg2, multicol_vg3))
      print(item)
}

selected_multi_linear <- function(table, selected, dvc)
{
    # table: data source csv file
    # selected: selected independent varialbes number
    # dvc: dependent variable column number
    # No return value(s)
    m_model <- lm(table[, dvc] ~ table[, selected[1]] +
                                 table[, selected[2]] +
                                 table[, selected[3]])
    print(summary(m_model))
    print(vif(m_model))
    print(sqrt(vif(m_model)) > 2) # if there is any problem?
}

correlence_ivs <- function(table, ivcs, dvc)
{
    
}

# defines
selectedFactors <- data[,c(1, 3, 5)]
selected_num <- c(1, 3, 5) # selected independent variable column number
dependent <- data[, 7]

vargroup_1 <- data[, 1:2]
vargroup_2 <- data[, 3:4]
vargroup_3 <- data[, 5:7]

# result printing area:
print("=======correlence=======")
batch_corr(data, 1:7, 8)
print("=======Linear=======")
batch_linear(data, 1:7, 8)
print("=======multicollinearity=======")
multicollinearity(data, vargroup_1, vargroup_2, vargroup_3)
print("=======selectedFactors=======")
print(kappa(selectedFactors))
print("=======multi-factor linear regression model=======")
selected_multi_linear(data, selected_num, 8)

