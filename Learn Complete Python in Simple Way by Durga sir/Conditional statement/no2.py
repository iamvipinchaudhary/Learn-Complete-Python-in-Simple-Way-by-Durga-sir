# Number to words between 0 to 99

words_upto_19 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
words_for_tens = ['', '', 'Twenty', 'Thirty', 'Fourty',
                  'Fifty', 'Sixty', 'seventy', 'eighty', 'ninty']
n = int(input('Enter a number from 0 to 99:'))
output = ''
if n == 0:
    output = 'ZERO'
elif n <= 19:
    output = words_upto_19[n]
elif n <= 99:
    output = words_for_tens[n//10]+" "+words_upto_19[n % 10]
else:
    output = 'Please enter a value from 0 to 99 only'
print(output)
