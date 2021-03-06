# 칵테일 레시피를 담은 함수. 칵테일 이름 리스트를 리턴합니다.
def cocktails():
    #  칵테일 이름, 칠링여부(1은 칠링 / 0은 칠링X), 가니쉬(있으면 이름 / 0은 X), 재료
    kir = ['kir', 0, 'twist lemon peel', ['white wine, 3', 'creme de cassis, 0.5']]
    negroni = ['negroni', 1, 'twist lemon peel', ['gin, 0.75', 'sweet vermouth, 0.75', 'campari, 0.75']]
    old_fashioned = ['old_fashioned', 0, 'sliced orange & cherry',
                     ['american whiskey, 1.5', 'cubed suger, 1', 'angostura bitters, 1', 'club soda, 0.5']]
    rusty_nail = ['rusty_nail', 1, 0, ['scotch whiskey, 0.75', 'drambuie, 0.5']]
    black_russian = ['black_russian', 1, 0, ['bodka, 1', 'kahlua, 0.5']]
    moscow_mule = ['moscow_mule', 1, 'sliced lemon', ['bodka, 1.5', 'lime juice, 0.5', 'ginger ale, 8fill']]
    bloody_mary = ['bloody_mary', 0, 'sliced lemon or celery',
                   ['worcester sauce, 1t', 'tabasco sauce, 1d', 'salt/pepper, 0.25t', 'bodka, 1.5',
                    'tomato juice, 8fill']]
    seabreeze = ['seabreeze', 1, 'wedge lemon', ['bodka, 1.5', 'cranberry juice, 3', 'grapefruit juice, 1.5']]
    cuba_libre = ['cuba_libre', 1, 'wedge lemon', ['rum, 1.5', 'lime juice, 0.5', 'cola, 8fill']]
    long_island_ice_tea = ['long_island_ice_tea', 1, 'wedge lemon',
                           ['bodka, 0.5', 'tequila, 0.5', 'gin, 0.5', 'rum, 0.5', 'triple sec, 0.5', 'sour mix, 1.5',
                            'cola, 8fill']]
    harvey_wallbanger = ['harvey_wallbanger', 1, 0, ['bodka, 1.5', 'orange juice, 8fill', 'galliano, 0.5']]
    tequila_sunrise = ['tequila_sunrise', 1, 0, ['tequila, 1.5', 'orange juice, 8fill', 'grenadine syrup, 0.5float']]
    mai_tai = ['mai_tai', 1, 'wedge pineapple & cherry',
               ['rum, 1.25', 'triple sec, 0.75', 'lime juice, 1', 'orange juice, 1', 'pineapple juice, 1',
                'grenadine syrup, 0.25']]
    blue_hawaiian = ['blue_hawaiian', 1, 'wedge pineapple & cherry',
                     ['rum, 1.5', 'blue curacao, 1', 'coconut flavored rum, 1', 'pineapple juice, 2.5']]
    pina_colada = ['pina_colada', 1, 'wedge pineapple & cherry',
                   ['rum, 1.25', 'pina colada mix, 2', 'pineapple juice, 2']]
    b_52 = ['b_52', 0, 0, ['kahlua, 1/3part', 'baileys, 1/3part', 'grand marnier, 1/3part']]
    pousse_cafe = ['pousse_cafe', 0, 0, ['brandy, 1/3part', 'creme de menthe, 1/3part', 'grenadine syrup, 1/3part']]
    manhattan = ['manhattan', 1, 'cherry', ['bourbon whisky, 1.5', 'sweet vermouth, 3/4', 'angostura bitters, 1dash']]
    dry_martini = ['dry_martini', 1, 'olive', ['gin, 2', 'dry vermouth, 1/3']]
    gochang = ['gochang', 1, 0, ['선운산 복분자 주, 2', 'triple sec, 0.5', 'sprite, 2']]
    sloe_gin_fizz = ['sloe_gin_fizz', 1, 'sliced lemon',
                     ['sloe gin, 1.5', 'lemon juice, 0.5', 'sugar, 1tsp', 'club soda, 8fill']]
    whisky_sour = ['whisky_sour', 1, 'sliced lemon & cherry',
                   ['bourbon whisky, 1.5', 'lemon juice, 0.5', 'sugar, 1tsp', 'club soda, 1']]
    singapore_sling = ['singapore_sling', 1, 'sliced orange & cherry',
                       ['gin, 1.5', 'lemon juice, 0.5', 'sugar, 1tsp', 'club soda, 8fill', 'cherry brandy, 0.5float']]
    honeymoon = ['honeymoon', 1, 0, ['kalbados, 3/4', 'benedictine DOM, 3/4', 'triple sec, 0.25', 'lemon juice, 0.5']]
    sidecar = ['sidecar', 1, 0, ['brandy, 1', 'cointreau or triple sec, 1', 'lemon juice, 0.25']]
    brandy_alexander = ['brandy_alexander', 1, 'nutmeg poweder', ['brandy, 3/4', 'creme de cacao, 3/4', 'milk, 3/4']]
    newyork = ['newyork', 1, 'twist lomon peel',
               ['bourbon whisky, 1.5', 'lime juice, 0.5', 'sugar, 1tsp', 'grenadine syrup, 0.5tsp']]
    margarita = ['margarita', 0, 'salt rimming', ['tequila, 1.5', 'triple sec, 0.5', 'lime juice, 0.5']]
    apple_martini = ['apple_martini', 0, 'sliced apple', ['vodka, 1', 'apple pucker, 1', 'lime juice, 0.5']]
    kiss_of_fire = ['kiss_of_fire', 0, 'sugar rimming',
                    ['vodka, 1', 'sloe gin, 0.5', 'dry vermouth, 0.5', 'lemon juice, 1tsp']]
    cosmopolitan = ['cosmopolitan', 1, 'twist lemon peel',
                    ['vodka, 1', 'triple sec, 0.5', 'lime juice, 0.5', 'cranberry juice, 0.5']]
    bacardi = ['bacardi', 1, 0, ['rum, 1.75', 'lime juice, 3/4', 'grenadine syrup, 1tsp']]
    daiquiri = ['daiquiri', 1, 0, ['rum, 1.75', 'lime juice, 3/4', 'sugar, 1tsp']]
    june_bug = ['june_bug', 1, 'wedge pineapple & cherry',
                ['midori, 1', 'coconut flavored rum, 0.5', 'banana liqueur, 0.5', 'pineapple juice, 2', 'sour mix, 2']]
    grasshopper = ['grasshopper', 1, 0, ['creme de menthe green, 1', 'creme de cacao white, 1', 'milk, 1']]
    apricot = ['apricot', 1, 0, ['apricot brandy, 1.5', 'gin, 1tsp', 'lemon juice, 0.5', 'orange juice, 0.5']]
    geumsan = ['geumsan', 1, 0, ['geumsan insam ju, 1.5', 'kahlua, 0.5', 'apple pucker, 0.5', 'lime juice, 1tsp']]
    jindo = ['jindo', 1, 0,
             ['jindo hongju, 1', 'creme de menthe white, 0.5', 'white grape juice, 3/4', 'raspberry syrup, 0.5']]
    puppy_love = ['puppy_love', 1, 'sliced apple',
                  ['andong soju, 1', 'triple sec, 1/3', 'apple pucker, 1', 'lime juice, 1/3']]
    healing = ['healing', 1, 'twist lemon peel',
               ['gam hong ro, 1.5', 'benedictine, 1/3', 'creme de cassis, 1/3', 'sour mix, 1']]

    all_cocktails = [kir, negroni, old_fashioned, rusty_nail, black_russian, moscow_mule, bloody_mary, seabreeze,
                     cuba_libre, long_island_ice_tea, harvey_wallbanger, tequila_sunrise, mai_tai, blue_hawaiian,
                     pina_colada, b_52, pousse_cafe, manhattan, dry_martini, gochang, sloe_gin_fizz, whisky_sour,
                     singapore_sling, honeymoon, sidecar, brandy_alexander, newyork, margarita, apple_martini,
                     kiss_of_fire, cosmopolitan, bacardi, daiquiri, june_bug, grasshopper, apricot, geumsan, jindo,
                     puppy_love, healing]

    return all_cocktails


