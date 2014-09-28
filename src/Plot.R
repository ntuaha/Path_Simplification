df = read.table('/Volumes/AhaStorage/A_Project/03_Path_Simplification/Path_Simplification/data/USD_S.csv',header=F,sep=",")
colnames(df) = c("data_dt","time_ind","buy_rate","sell_rate","type","type2","error")
library(ggplot2)
