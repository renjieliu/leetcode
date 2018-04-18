def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    dict = "abcdefghijklmnopqrstuvwxyz01234565789"
    output = ""
    output_r = ""
    for i in str(s).lower():
        if i in list(dict):
            output += i
            output_r = i+output_r

    if output_r ==output:
        return True
    else:
        return False

print(isPalindrome(""))

