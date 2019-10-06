def isPalindrome(text):
    text = text.lower()
    lengthtext = len(text)
    if lengthtext % 2 == 0:
        numhalf = int(lengthtext / 2)
        firsthalf = text[0:numhalf]
        lasthalf = text[numhalf:lengthtext]
        if firsthalf == lasthalf[::-1]:
            print(text, "is a palindrome.")
        else:
            print(text, "is not a palindrome.")
    elif lengthtext % 2 != 0:
        numhalf1 = int((lengthtext - 1) / 2)
        numhalf2 = int((lengthtext + 1)/2)
        firsthalf = text[0:numhalf1]
        lasthalf = text[numhalf2:lengthtext]
        if firsthalf == lasthalf[::-1]:
            print(text, "is a palindrome.")
        else:
            print(text, "is not a palindrome.")
    else:
        print("Invalid text input.")
    return;

isPalindrome("Racecar")
isPalindrome("Connor")
