import numpy as np

final_coefficients = []

for i in range(12):
    print("Group: " + str(i+1))

    b_sum = int(input("Enter the sum: "))
    b_2HighAndMid = int(input("Enter the second number: "))
    b_2MidAndLow = int(input("Enter the third number: "))

    a = np.array([[1, 1, 1], [0, 1, 2], [1, 2, 0]])
    b = np.array([b_sum, b_2HighAndMid, b_2MidAndLow])

    solution = np.linalg.solve(a, b)
    final_coefficients = np.concatenate([final_coefficients, solution])

print(final_coefficients)


# input from CTF challenge
"""

Var2 = strlen(param_1);

sVar2 == 36

param_1[2] + param_1[0] + param_1[1] == 227
param_1[1] + param_1[2] * 2 == 207
param_1[0] + param_1[1] * 2 == 239

param_1[5] + param_1[3] + param_1[4] == 289
param_1[4] + param_1[5] * 2 == 329
param_1[3] + param_1[4] * 2 == 249

param_1[8] + param_1[6] + param_1[7] == 256
param_1[7] + param_1[8] * 2 == 266
param_1[6] + param_1[7] * 2 == 195

param_1[11] + param_1[9] + param_1[10] == 284
param_1[10] + param_1[11] * 2 == 227
param_1[9] + param_1[10] * 2 == 346

param_1[14] + param_1[12] + param_1[13] == 260
param_1[13] + param_1[14] * 2 == 304
param_1[12] + param_1[13] * 2 == 279

param_1[17] + param_1[15] + param_1[16] == 201
param_1[16] + param_1[17] * 2 == 197
param_1[15] + param_1[16] * 2 == 251

param_1[20] + param_1[18] + param_1[19] == 260
param_1[19] + param_1[20] * 2 == 308
param_1[18] + param_1[19] * 2 == 271

param_1[23] + param_1[21] + param_1[22] == 195
param_1[22] + param_1[23] * 2 == 193
param_1[21] + param_1[22] * 2 == 241

param_1[26] + param_1[24] + param_1[25] == 254
param_1[25] + param_1[26] * 2 == 307
param_1[24] + param_1[25] * 2 == 243

param_1[29] + param_1[27] + param_1[28] == 225
param_1[28] + param_1[29] * 2 == 163
param_1[27] + param_1[28] * 2 == 223

param_1[32] + param_1[30] + param_1[31] == 256
param_1[31] + param_1[32] * 2 == 213
param_1[30] + param_1[31] * 2 == 313

param_1[35] + param_1[33] + param_1[34] == 284
param_1[34] + param_1[35] * 2 == 354
param_1[33] +  param_1[34] * 2 == 263

"""
