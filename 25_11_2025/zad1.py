zmienna = 2.1

if isinstance(zmienna, int) or isinstance(zmienna, float):
    if (isinstance(zmienna, float) and zmienna.is_integer()) or isinstance(zmienna, int):
        print('Zmienna jest liczbą całkowitą')
    else:
        print('Zmienna jest liczbą zmiennoprzecinkową')
else:
    print('Zmienna jest ciągiem znaków')
