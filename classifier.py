import numpy as np

np.random.seed(1)

print("Loading Data ...")
Data = np.loadtxt("G:\Data\RF_Data.csv", delimiter=",")
print("Preparing Data ...")

x = np.transpose(Data[0:2047,:])
Label_1 = np.transpose(Data[2048:2049,:]); Label_1 = Label_1.astype(int);
Label_2 = np.transpose(Data[2049:2050,:]); Label_2 = Label_2.astype(int);
Label_3 = np.transpose(Data[2050:2051,:]); Label_3 = Label_3.astype(int);
y = encode(Label_3)
