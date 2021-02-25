import pandas as pd

data_sum = [6,4,-3,13,3,-6,36]

try:
    main_data = pd.read_csv('data.csv')
except:
    main_data = pd.DataFrame([],columns=["s1","s2","s3","s4","s5","s6","age"])
##print(data)
##data.to_csv('data.csv')
result_df = pd.DataFrame(data_sum,columns=["s1","s2","s3","s4","s5","s6","age"])
main_data.append(result_df)
######реализовать полиномиальную регрессию https://www.machinelearningmastery.ru/polynomial-regression-bbe8b9d97491/
