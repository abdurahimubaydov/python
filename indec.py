def reverseString(s: list) -> list:
    i, j = 0, len(s) - 1

    # tepadagi i va j lar indexlarni aniqlab oldik. 
    # i teng bo'ladi arrayning eng boshidagi songa
    # j esa teng bo'ladi arrayning eng oxiridagi songa 
    # har doim shunaqa bo'ladi


    while i < j: # masala bajariladi har doim i element kichik bolsa j dan
        s[i], s[j] = s[j], s[i] # bu yerda o'rinlarni almashtirib oldik, har qaytarishda oxiridagi 
        # elementni boshidagi element bilan almashtirish kerak bo'ladi
        i += 1 # bu almashtirib bogandan keyin, keyingi elementga yani (0 + 1)chi elementga o'tat
        j -= 1 # bu esa ( (len(s) - 1) - 1 )chi elementga otadi

    return s # oxirida esa qiymatni o'zini, ya'ni argumentni qaytaradi
print(reverseString(list('salom')))