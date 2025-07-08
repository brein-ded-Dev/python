raise can be thought as a check for invalid input 
will crash program under normal circumstances with error message written inside the raise block 
crash can be avoided if raise is written inside try and catch 
**THIS IS WRONG.**

try - something might be wrong, 
somewhat like precaution is better than cure. 

except- in case errors are found by try or raise, the code will completely ignore anything written below in the try block and move to error handling at the except statement

in case of error handling with except, code other than the try block continues normally. 

assert- a boolean check that asserts if the answer is false there is a bug in the code and everything must stop at an instance. 
doomsday button when it comes to false. can be replaced with raise. (i personally think anyways)

logging - logs. flow of the program. separate library logging. 

